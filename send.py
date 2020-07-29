import requests

headers= {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTk1NDQ2NDYxLCJqdGkiOiI5YjZiZTk0ODBmNTI0YTdlYjcwY2E0MjMwMmNiNzlhZSIsInVzZXJfaWQiOjJ9.9N33EA9jEvOoUBZhVaWRG-l5RWWWAy-TnmxxP1QsW_E'
r = requests.get('http://127.0.0.1:8000/api/token/', headers=headers)

print(r.text)