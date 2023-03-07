import json, os, requests, random

link = ("https://ibnux.github.io/BMKG-importer/cuaca/501233.json")
json = requests.get(link).json()
os.system("clear")

for data in json:
	print('tanggal dan waktu : ', data['jamCuaca'])
	print('kode cuaca        : ', data['kodeCuaca'])
	print('cuaca             : ', data['cuaca'])
	print('humidity          : ', data['humidity'])
	print('tempC             : ', data['tempC'])
	print('tempF             : ', data['tempF'])
	print(37*'-')
	
	
	