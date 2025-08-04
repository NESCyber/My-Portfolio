from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from datetime import datetime
import json

app = Flask(__name__)
CORS(app)

# Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "hangoutmitnick@gmail.com"  # Replace with your Gmail
SENDER_PASSWORD = "rxow neoe qzfu ribk"  # Replace with your actual Gmail app password
RECIPIENT_EMAIL = "hangoutmitnick@gmail.com"  # Replace with your email

# Create data directory if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

def send_email(name, email, subject, message):
    """Send email notification"""
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = f"Portfolio Contact: {subject}"
        
        # Email body
        body = f"""
        New message from your portfolio website!
        
        Name: {name}
        Email: {email}
        Subject: {subject}
        Message: {message}
        
        Sent at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        text = msg.as_string()
        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, text)
        server.quit()
        
        return True
    except Exception as e:
        print(f"Email error: {e}")
        return False

def save_message(name, email, subject, message):
    """Save message to local file"""
    try:
        message_data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
            'timestamp': datetime.now().isoformat()
        }
        
        # Load existing messages
        messages = []
        if os.path.exists('data/messages.json'):
            with open('data/messages.json', 'r') as f:
                messages = json.load(f)
        
        # Add new message
        messages.append(message_data)
        
        # Save updated messages
        with open('data/messages.json', 'w') as f:
            json.dump(messages, f, indent=2)
        
        return True
    except Exception as e:
        print(f"Save error: {e}")
        return False

@app.route('/')
def index():
    """Serve the main portfolio page"""
    return render_template('index.html')

@app.route('/api/contact', methods=['POST'])
def contact():
    """Handle contact form submissions"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'email', 'subject', 'message']
        for field in required_fields:
            if not data.get(field):
                return jsonify({
                    'success': False,
                    'message': f'{field.capitalize()} is required'
                }), 400
        
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        
        # Basic email validation
        if '@' not in email or '.' not in email:
            return jsonify({
                'success': False,
                'message': 'Please enter a valid email address'
            }), 400
        
        # Save message locally
        save_success = save_message(name, email, subject, message)
        
        # Send email notification
        email_success = send_email(name, email, subject, message)
        
        if save_success:
            return jsonify({
                'success': True,
                'message': 'Message sent successfully!'
            }), 200
        else:
            return jsonify({
                'success': False,
                'message': 'Failed to save message'
            }), 500
            
    except Exception as e:
        print(f"Contact error: {e}")
        return jsonify({
            'success': False,
            'message': 'An error occurred while processing your request'
        }), 500

@app.route('/api/messages', methods=['GET'])
def get_messages():
    """Get all saved messages (for admin purposes)"""
    try:
        if os.path.exists('data/messages.json'):
            with open('data/messages.json', 'r') as f:
                messages = json.load(f)
            return jsonify({
                'success': True,
                'messages': messages
            }), 200
        else:
            return jsonify({
                'success': True,
                'messages': []
            }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'message': 'Failed to retrieve messages'
        }), 500

@app.route('/admin')
def admin():
    """Admin page to view messages"""
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 