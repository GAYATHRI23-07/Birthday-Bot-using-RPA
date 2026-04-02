# Birthday Reminder Bot

This automation bot reads an Excel sheet containing names, dates of birth, and emails, and will pop up a desktop notification and send an automated email to anyone whose birthday matches today's date.

## File Structure

- `main.py`: The entry point script to run the bot.
- `excel_handler.py`: Contains logic to read and filter rows from `birthdays.xlsx`.
- `email_sender.py`: Configures SMTP credentials and sends out the email. 
- `notifier.py`: Produces custom Windows/desktop notifications for reminders.
- `logger.py`: Writes the outcomes of the bot run to `log.txt`.
- `create_sample.py`: A utility script to generate a dummy `birthdays.xlsx`.
- `requirements.txt`: Project dependencies.

## Instructions

1. **Install Python**: You will need to install Python for Windows. Ensure `python` or `pip` is available in your command prompt.
2. **Install Dependencies**: Open the folder in the terminal and run:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure Email (Crucial)**: Open `email_sender.py` and modify the constants:
   - `SMTP_SERVER`
   - `SMTP_PORT`
   - `SENDER_EMAIL` (your email address)
   - `SENDER_PASSWORD` (use an App Password if using Gmail, not your actual account password)

4. **Prepare Data**: Provide a `birthdays.xlsx` file in the same directory. Alternatively, you can run `python create_sample.py` to generate an example file with dummy data.

5. **Run the Bot**:
   ```bash
   python main.py
   ```
   Check the terminal output and the `log.txt` generated!
