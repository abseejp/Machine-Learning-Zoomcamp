import requests

URL = 'http://localhost:5000/predict'
client_payload = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}


response = requests.post(URL, json = client_payload).json()

print(response)