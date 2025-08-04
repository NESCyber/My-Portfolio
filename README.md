# Portfolio Website

A Flask-based portfolio website with contact form functionality and email notifications.

## Features

- Responsive portfolio website
- Contact form with email notifications
- Message storage in JSON format
- Admin panel to view messages
- Email integration with Gmail SMTP

## Prerequisites

Before running this application, make sure you have:

1. **Python 3.7 or higher** installed on your system
2. **Git** (optional, for cloning the repository)
3. **Gmail account** with App Password enabled (for email notifications)

## Step-by-Step Setup Guide

### Step 1: Clone or Download the Project

If you have Git installed:
```bash
git clone <repository-url>
cd "My portfolio"
```

Or simply download and extract the project files to your desired location.

### Step 2: Set Up Python Virtual Environment

**For Windows:**
```bash
# Navigate to the project directory
cd "My portfolio"

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
venv\Scripts\activate
```

**For macOS/Linux:**
```bash
# Navigate to the project directory
cd "My portfolio"

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate
```

### Step 3: Install Dependencies

With the virtual environment activated, install the required packages:
```bash
pip install -r requirements.txt
```

This will install:
- Flask 2.3.3
- Flask-CORS 4.0.0
- Werkzeug 2.3.7

### Step 4: Configure Email Settings (Optional)

If you want to enable email notifications:

1. **Enable 2-Factor Authentication** on your Gmail account
2. **Generate an App Password**:
   - Go to Google Account settings
   - Navigate to Security
   - Under "2-Step Verification", select "App passwords"
   - Generate a new app password for "Mail"
3. **Update the email configuration** in `app.py`:
   ```python
   SENDER_EMAIL = "your-email@gmail.com"  # Replace with your Gmail
   SENDER_PASSWORD = "your-app-password"  # Replace with your app password
   RECIPIENT_EMAIL = "your-email@gmail.com"  # Replace with your email
   ```

**Note:** If you don't configure email settings, the contact form will still work and save messages locally, but email notifications won't be sent.

### Step 5: Run the Application

With the virtual environment activated, run the Flask application:
```bash
python app.py
```

You should see output similar to:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://[your-ip]:5000
```

### Step 6: Access the Application

Open your web browser and navigate to:
- **Main Portfolio**: http://localhost:5000 or http://127.0.0.1:5000
- **Admin Panel**: http://localhost:5000/admin or http://127.0.0.1:5000/admin

## Project Structure

```
My portfolio/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── data/                 # Data storage directory
│   └── messages.json     # Contact form messages
├── static/               # Static files (CSS, JS, images)
│   ├── styles.css
│   ├── script.js
│   ├── profile.jpg
│   └── pro1.jpg
└── templates/            # HTML templates
    ├── index.html        # Main portfolio page
    └── admin.html        # Admin panel
```

## Features Usage

### Contact Form
1. Navigate to the main page
2. Fill out the contact form with your name, email, subject, and message
3. Submit the form
4. Messages are saved locally and sent via email (if configured)

### Admin Panel
1. Navigate to `/admin` to view all submitted messages
2. Messages are displayed with timestamps
3. No authentication required (for development purposes)

## Troubleshooting

### Common Issues

1. **Port already in use**:
   - Change the port in `app.py`: `app.run(debug=True, host='0.0.0.0', port=5001)`

2. **Email not sending**:
   - Check your Gmail app password
   - Ensure 2-factor authentication is enabled
   - Verify SMTP settings

3. **Module not found errors**:
   - Make sure virtual environment is activated
   - Run `pip install -r requirements.txt` again

4. **Permission errors**:
   - Run as administrator (Windows)
   - Check file permissions (macOS/Linux)

### Stopping the Application

To stop the Flask application:
- Press `Ctrl + C` in the terminal where the app is running

### Deactivating Virtual Environment

When you're done working on the project:
```bash
deactivate
```

## Development

- The application runs in debug mode by default
- Changes to Python files will automatically reload the server
- Static files and templates may require manual browser refresh

## Production Deployment

For production deployment:
1. Set `debug=False` in `app.py`
2. Use a production WSGI server like Gunicorn
3. Configure proper email settings
4. Add authentication to the admin panel
5. Use environment variables for sensitive data

## Support

If you encounter any issues:
1. Check the console output for error messages
2. Verify all dependencies are installed
3. Ensure Python version is 3.7 or higher
4. Check file permissions and paths 