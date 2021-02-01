import requests

def sendMsg(ids, text):

    payload = {
        'chat_id': ids,
        'text': text
    }
    url2 = f'https://api.telegram.org/bot{token}/sendMessage'
    r2 = requests.get(url2, params=payload)

token = '1623544581:AAGcmnpip3itggtxdUpX_GK7CdW-y1jmkic'
url1 = f'https://api.telegram.org/bot{token}/getUpdates'

r1 = requests.get(url1)

data = r1.json()
updates = data['result']

for update in updates:
    message = update['message']
    text = message['text']
    user = message['from']
    i = user['id']
    sendMsg(i, text)
