import json
import requests
import time
import os
from influxdb import InfluxDBClient

api_url = 'http://data.fixer.io/api/latest?access_key='
api_key = os.environ['API_KEY']
sleep_time = os.environ['SLEEP']
influxdb_host = os.environ['INFLUXDB_HOST']


response = requests.request("GET", api_url + api_key)
print(response.text)
result = 1 / float(json.loads(response.text)['rates']['CHF'])

client = InfluxDBClient(influxdb_host, 8086, 'root', 'root', 'chf_data')
client.create_database('chf_data')


while True:
    client.write_points([{"measurement": "CHF", "fields": {"value": round(result, 5)}}])
    time.sleep(int(sleep_time))
