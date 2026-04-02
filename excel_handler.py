import pandas as pd
from logger import log_error

def read_birthdays(file_path_or_buffer):
    try:
        # Load the Excel file without parsing dates yet
        df = pd.read_excel(file_path_or_buffer)
        
        # Map common date of birth column variations to 'DOB'
        dob_aliases = ['dob', 'birthday', 'birth date', 'date of birth']
        
        def map_column(c):
            cleaned = str(c).strip()
            if cleaned.lower() in dob_aliases:
                return 'DOB'
            return cleaned.title()
            
        df.columns = [map_column(c) for c in df.columns]
        
        # Verify required columns exist
        required_columns = ['Name', 'DOB', 'Email']
        if not all(col in df.columns for col in required_columns):
            log_error(f"Missing required columns in Excel file. Found: {list(df.columns)}, Expected: {required_columns}")
            raise ValueError(f"Missing required columns. Ensure Name, DOB, and Email exist.")
            
        # Manually convert DOB to datetime, coercing errors
        df['DOB'] = pd.to_datetime(df['DOB'], errors='coerce')
        
        return df
    except Exception as e:
        log_error(f"Error reading Excel data: {e}")
        raise e
