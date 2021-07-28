import time
import requests

t = 0
url = 'v1/Employees/GetAllActiveEmployees'

while t < 100:
    req = requests.get(url)
    time.sleep(5)
    t +=1
    print(r.json)