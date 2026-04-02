import smtplib
from email.message import EmailMessage
from logger import log_error

# IMPORTANT: To use this, you need a valid SMTP configuration.
# For example, for Gmail: smtp.gmail.com, port 587, and an App Password.
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_app_password_here"

def send_email(to_email, name):
    if SENDER_EMAIL == "your_email@gmail.com":
        log_error("Skipping email: SENDER_EMAIL is not configured. Please configure email_sender.py.")
        return False
        
    msg = EmailMessage()
    msg['Subject'] = 'Happy Birthday!'
    msg['From'] = SENDER_EMAIL
    msg['To'] = to_email
    
    body = f"Hello {name},\n\nWishing you a very Happy Birthday! Have a wonderful day.\n\nBest regards,\nBirthday Bot"
    msg.set_content(body)
    
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
        return True
    except Exception as e:
        log_error(f"Failed to send email to {to_email}: {str(e)}")
        return False
