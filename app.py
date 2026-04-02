import datetime
import pandas as pd
from flask import Flask, request, jsonify, render_template
from excel_handler import read_birthdays
from email_sender import send_email
from logger import log_info

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})
        
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
        
    try:
        log_info("Starting Web Request to process birthdays.")
        # Pass the FileStorage object directly to pandas read_excel
        df = read_birthdays(file)
        
        if df is None:
            return jsonify({'error': 'Failed to read Excel file or missing columns.'})
            
        today = datetime.datetime.now()
        today_month = today.month
        today_day = today.day
        
        results = []
        notifications_sent = 0
        
        for index, row in df.iterrows():
            name = row['Name']
            dob = row['DOB']
            email = row['Email']
            
            if pd.isna(dob):
                continue
                
            if dob.month == today_month and dob.day == today_day:
                log_info(f"Web: Birthday match found for {name} ({email})")
                
                # Send Email locally 
                email_sent = send_email(email, name)
                
                # Add to results to be shown in UI and trigger browser notification
                results.append({
                    'name': name,
                    'email': email,
                    'email_sent': email_sent
                })
                notifications_sent += 1
                
        log_info(f"Web: Finished run. Sent {notifications_sent} notifications.")
        
        return jsonify({
            'success': True,
            'matches': results
        })
        
    except Exception as e:
        log_info(f"Web Error: {str(e)}")
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
