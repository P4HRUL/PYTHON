import json, os, requests, random

link = ("https://kodepos-2d475.firebaseio.com/kota_kab/k69.json?print=pretty")
json = requests.get(link).json()

logo = ('''\033[1;94m
  _  _____  ____  _____   ____   ___  ____  
 | |/ / _ \|  _ \| ____| |  _ \ / _ \/ ___| 
 | ' / | | | | | |  _|   | |_) | | | \___ \ 
 | . \ |_| | |_| | |___  |  __/| |_| |___) |
 |_|\_\___/|____/|_____| |_|    \___/|____/ 

\033[1;96m- \033[1;97mCoding By : \033[1;96mPahrul Aguspriana XD.
''')
os.system("clear")
print(logo)

for data in json:
	print('\033[1;97m[\033[1;92m-\033[1;97m] kecamatan   : ', data['kecamatan'])
	print('\033[1;97m[\033[1;92m-\033[1;97m] kelurahan   : ', data['kelurahan'])
	print('\033[1;97m[\033[1;92m-\033[1;97m] kode pos    : ', data['kodepos'])
	print("\033[1;90m"+37*'-')