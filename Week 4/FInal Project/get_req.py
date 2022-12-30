import requests
import json

def get() -> dict:
    URL = 'http://127.0.0.1:9999'

    response = json.loads(requests.get(URL + "/receive").text)['messages']
    try:
        return response[-2]
    except:
        return response[-1]