from plyer import notification
from logger import log_error

def show_popup(title, message):
    try:
        notification.notify(
            title=title,
            message=message,
            app_name='Birthday Bot',
            timeout=10 # Notification stays for 10 seconds
        )
    except Exception as e:
        log_error(f"Failed to send popup notification: {e}")
