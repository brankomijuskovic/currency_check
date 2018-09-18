import json
import requests
import time
import os

api_url = 'http://data.fixer.io/api/latest?access_key='
api_key = os.environ['API_KEY']
sleep_time = os.environ['SLEEP']

response = requests.request("GET", api_url + api_key)
result = 1 / float(json.loads(response.text)['rates']['CHF'])

while True:
    print(round(result, 5))
    time.sleep(sleep_time)

