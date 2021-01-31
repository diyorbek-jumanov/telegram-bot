import requests
import json
from pprint import pprint

token = '1623544581:AAGcmnpip3itggtxdUpX_GK7CdW-y1jmkic'
url = f'https://api.telegram.org/bot{token}/getUpdates'
r = requests.get(url)
data = r.json()
updates = data['result']

for update in updates:
    message = update['message']
    user = message['from']
    first_name = user.get('first_name', None)
    last_name = user.get('last_name', None)
    full_name = f'{first_name} {last_name}'
    print(full_name)
