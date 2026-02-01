import requests
import os
from PIL import Image
from IPython.display import IFrame

url='https://www.ibm.com/'
r=requests.get(url)

print(r.status_code)
print(r.headers['Content-Type'])
print(r.headers['Content-Length'])


'''Output:200
text/html;charset=utf-8
39383
(.venv)'''