import json, os, requests, random

link = ("https://doa-doa-api-ahmadramadhan.fly.dev/api")
json = requests.get(link).json()
os.system("clear")

for data in json:
	print('nomor   : ', data['id'])
	print('doa     : ', data['doa'])
	print('ayat    : ', data['ayat'])
	print('latin   : ', data['latin'])
	print('artinya : ', data['artinya'])
	print(37*'-')