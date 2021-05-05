import requests
respons = requests.get('http://127.0.0.1:8081/get?rank=S')
print(respons.json())
