import requests
import json


def get_rates(API_KEY):
    FIXER_URL = 'http://data.fixer.io/api/latest?access_key='
    response = requests.get(FIXER_URL + API_KEY)

    if response.status_code == 200:
        return json.loads(response.text)

    return None
