# import urllib.request as request 
# src = "https://www.google.com"
# with request.urlopen(src) as response:
#     data = response.read().decode("utf-8")

# print(data)

from urllib import request as req
import json

url = "https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=296acfa2-5d93-4706-ad58-e83cc951863c"
web_open = req.urlopen(url)
raw_data = web_open.read().decode("utf-8")
print(raw_data)
