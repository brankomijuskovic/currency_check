import json
import requests
import time
import datetime
import os
import sys
from influxdb import InfluxDBClient

api_url = 'http://data.fixer.io/api/latest?access_key='
sleep_time = os.environ['SLEEP']
influxdb_host = os.environ['INFLUXDB_HOST']

try:
    api_key = os.environ['API_KEY']
except Exception:
    print("No API key provided, exiting.")
    sys.exit(1)

while True:
    try:
        client = InfluxDBClient(influxdb_host, 8086, 'root', 'root', 'chf_data')
        client.create_database('chf_data')
        break
    except Exception as err:
        print("{} - Can't connect to InfluxDB, sleeping.".format(datetime.datetime.now()))
        print(err)
        time.sleep(5)


while True:
    try:
        response = requests.request("GET", api_url + api_key)
        result = 1 / float(json.loads(response.text)['rates']['CHF'])
        print(result)
        client.write_points([{"measurement": "CHF", "fields": {"value": round(result, 5)}}])
        time.sleep(int(sleep_time))
    except Exception as err:
        print("{} - Something went wrong. {}".format(datetime.datetime.now(), err))
        time.sleep(5)
