# config.py

# Network scanning settings
NETWORK_SUBNET = "192.168.1.0/24"  # Change this to your local subnet

# Trusted devices (MAC addresses in lowercase)
TRUSTED_MACS = {
    "00:11:22:33:44:55": "My Laptop",
    "66:77:88:99:aa:bb": "My Phone",
}

# Alert settings
EMAIL_ALERTS_ENABLED = False  # Set to True to enable email alerts
EMAIL_SMTP_SERVER = "smtp.gmail.com"
EMAIL_SMTP_PORT = 587
EMAIL_USERNAME = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"  # Use app password, not your real password
ALERT_RECIPIENT_EMAIL = "recipient_email@gmail.com"

# SMS Alerts (optional, if using Twilio or similar)
SMS_ALERTS_ENABLED = False
TWILIO_ACCOUNT_SID = "your_account_sid"
TWILIO_AUTH_TOKEN = "your_auth_token"
TWILIO_FROM_NUMBER = "+1234567890"
ALERT_RECIPIENT_PHONE = "+0987654321"

# Scan interval in seconds
SCAN_INTERVAL = 60  # Run scan every 60 seconds

# Logging
LOG_FILE_PATH = "logs/intrusion_log.json"

