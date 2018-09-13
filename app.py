import json
import requests
import time
import os

api_url = 'http://data.fixer.io/api/latest?access_key='
api_key = os.environ['API_KEY']

response = requests.request("GET", api_url + api_key)
result = 1 / float(json.loads(response.text)['rates']['CHF'])

while True:
    print(round(result, 4))
    time.sleep(3600)

