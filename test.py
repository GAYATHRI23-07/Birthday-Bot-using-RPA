import sys
from app import app
from io import BytesIO

with app.test_client() as c:
    with open('birthdays.xlsx', 'rb') as f:
        response = c.post('/upload', data={
            'file': (f, 'birthdays.xlsx')
        })
        print(response.json)
