import requests
import os
from PIL import Image
from IPython.display import IFrame

url_get='http://httpbin.org/get'

payload={"name":"Joseph","ID":"123"}
## get request with parameters
r=requests.get(url_get,params=payload)

r.url
print("request body:", r.request.body)
print(r.status_code)
print(r.text)
print(r.headers['Content-Type'])
print(r.json())
print(r.json()['args'])

'''Output:
application/json
{'args': {'ID': '123', 'name': 'Joseph'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate, br', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.32.5', 'X-Amzn-Trace-Id': 'Root=1-697f71b6-0609628f2e167a076679ce02'}, 'origin': '49.36.213.63', 'url': 'http://httpbin.org/get?name=Joseph&ID=123'}
{'ID': '123', 'name': 'Joseph'}'''