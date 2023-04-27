import requests
import csv
url = "http://api.coincap.io/v2/assets"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
myjson = response.json()
our_data = []
csvheader = ['Symbol','Name','Price in USD']
for x in myjson['data']:
    listing = [x['symbol'],x['name'],x['priceUsd']]
    our_data.append(listing) 
    
with open('crypto.csv','w',encoding='UTF8',newline = '') as f:
    writer = csv.writer(f)
    
    writer.writerow(csvheader)
    writer.writerows(our_data)
print('Successful')
