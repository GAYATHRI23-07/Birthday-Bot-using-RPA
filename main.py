import datetime
from excel_handler import read_birthdays
from email_sender import send_email
from notifier import show_popup
from logger import log_info

def main():
    log_info("Starting Birthday Reminder Bot")
    
    # Read Excel file
    df = read_birthdays()
    if df is None:
        log_info("Exiting early due to error reading Excel file.")
        return
        
    # Get current date (day and month)
    today = datetime.datetime.now()
    today_month = today.month
    today_day = today.day
    
    log_info(f"Checking for birthdays on {today_month:02d}-{today_day:02d}")
    
    notifications_sent = 0
    
    # Loop through each row
    for index, row in df.iterrows():
        name = row['Name']
        dob = row['DOB']
        email = row['Email']
        
        # Check if DOB data is valid datetime
        if pd.isna(dob):
            continue
            
        # Compare day and month
        if dob.month == today_month and dob.day == today_day:
            log_message = f"Birthday match found for {name} ({email})"
            log_info(log_message)
            print(log_message)
            
            # Send Email
            email_sent = send_email(email, name)
            
            # Show Popup Notification
            popup_title = "Happy Birthday!"
            popup_message = f"It's {name}'s birthday today! Email status: {'Sent' if email_sent else 'Failed/Skipped'}"
            show_popup(popup_title, popup_message)
            
            # Log final status
            log_info(f"Successfully processed birthday for {name}")
            notifications_sent += 1
            
    log_info(f"Bot finished run. Sent {notifications_sent} notifications.")

if __name__ == "__main__":
    import pandas as pd # Needed here for pd.isna check
    main()
