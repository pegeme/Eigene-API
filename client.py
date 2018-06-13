import requests
import json

while True:
	city = raw_input("City? : ")
	url = 'http://127.0.0.1:5000/?q={}'.format(city)
	res = requests.get(url)
	data = res.json()

	if res.status_code == 200:
		print(data)
		break
