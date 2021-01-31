import requests
from pprint import pprint

token = '1623544581:AAGcmnpip3itggtxdUpX_GK7CdW-y1jmkic'

url = f'https://api.telegram.org/bot{token}/getUpdates'

r = requests.get(url)
pprint(r.json()['result'][0]['message'])
