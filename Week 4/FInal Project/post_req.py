import requests

def post(msg):
    URL = 'http://127.0.0.1:9999/send'

    data = {'message': msg}

    response = requests.post(URL, data=data)
    
    if response.status_code == 200:
        print('Message Sent!')
    else:
        print('An error occurred.')
