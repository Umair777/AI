import requests
import os
from PIL import Image
from IPython.display import IFrame

url='https://www.ibm.com/'
r=requests.get(url)

print(r.status_code)
print(r.headers['Content-Type'])
print(r.headers['Content-Length'])

##saving image
rl='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'

r = requests.get(rl)
print(r.headers)

print(r.headers['Content-Type'])

path = os.path.join(os.getcwd(), 'image.png')
with open(path, 'wb') as f:
    f.write(r.content)
    
Image.open(path)


'''Output:200
text/html;charset=utf-8
39383
(.venv)'''