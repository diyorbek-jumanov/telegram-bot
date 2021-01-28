import requests

token = '1623544581:AAGcmnpip3itggtxdUpX_GK7CdW-y1jmkic'
url = f'https://api.telegram.org/bot{token}/getMe'

r = requests.get(url)
print(r.json())
