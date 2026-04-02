import pandas as pd
from datetime import datetime

data = {
    'Name': ['Alice', 'Bob'],
    'DOB': [datetime(1995, 4, 2), datetime(1990, 12, 25)],
    'Email': ['alice@example.com', 'bob@example.com']
}

df = pd.DataFrame(data)
df.to_excel('birthdays.xlsx', index=False)
print("Created birthdays.xlsx successfully.")
