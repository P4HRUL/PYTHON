import os, requests, json
os.system("clear")

def masuk():
    ip = input("masukan alamat ip address target : ")
    link = requests.get(f"http://ip-api.com/json/{ip}")
    if link.status_code == 200:
    	data = json.loads(link.text)
    print(37*'-')
    print ("- country :",data["country"])
    print ("- countryCode :",data["countryCode"])
    print ("- region :",data["region"])
    print ("- regionName :",data["regionName"])
    print ("- city :",data["city"])
    print ("- lat :",data["lat"])
    print ("- lon :",data["lon"])
    print ("- timezone :",data["timezone"])
    print ("- isp :",data["isp"])
    print ("- as :",data["as"])
    print(37*'-')
            
masuk()
