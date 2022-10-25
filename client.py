import requests

url = 'http://127.0.0.1:3000/compute'
#url = 'https://www.w3schools.com/python/demopage.php'
req = {'key': 'value'}

x = requests.post(url, json=req)
print(x.text)