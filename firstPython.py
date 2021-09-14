import os
import json
import requests


BASE_URL = 'http://api.exchangeratesapi.io/v1/latest'

ACCESS_KEY = os.getenv('ACCESS_KEY')
SYMBOLS = os.getenv('SYMBOLS', 'USD,AUD,CAD,PLN,MXN')

URL = f'{BASE_URL}?access_key={ACCESS_KEY}&symbols={SYMBOLS}'

def update_rates(url: str):
    response = requests.get(url)
    response_json = json.loads(response.text)

    del response_json["success"]
    del response_json["timestamp"]

    write_to_file(response_json, 'htyui')

    print(response_json)

def write_to_file(data: dict, file_name: str = 'no_name'):
    with open(f'{file_name}.json', 'w') as file:
        json.dump(data, file)

if __name__ == '__main__':
    update_rates(URL)
