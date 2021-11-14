import requests
import json
from getpass import getpass
from requests.auth import HTTPBasicAuth

username = input("Enter username: ")
password = getpass("Enter password: ")

authurl = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"
url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device"

payload={}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/atom+xml',
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

token = requests.request("POST", authurl, headers=headers, data=payload)

payload2={}
headers2 = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'X-Auth-Token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI2MTIzZGEzMTdiM2FhOTA2ZWQwYjJiMzIiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVlNWE0MzI2NzUxNjEyMDBjYzRhYzk2MyJdLCJ0ZW5hbnRJZCI6IjVlNWE0MzI1NzUxNjEyMDBjYzRhYzk1YyIsImV4cCI6MTYzNjkxNjE1MSwiaWF0IjoxNjM2OTEyNTUxLCJqdGkiOiJjZmZlNjMxNy0wOTNiLTRjZDAtYTU1OS1hM2E3YjcxYWM3NjkiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.WOcdhQczkDpf9JuFdd9DO8Gy-TzqVs-wDZrfbqRU2H7HeYbXuMDqSfz4Eg3dkL0URTL---xZkiyXUWIcK2pd9bVg8ryjkwlH_4dnxbFgNKnhpOAD5mVC_KKw-mTyb-Q1JhiNb-8QkOZ_fSWNnGa6u4Bua3BGYiIA6I2N7MT4ZPXvWJpzv2g4cTLWVJPSvBOLgoIptJaXpw-cGIz6e8NY9K85ju26B40QOd70MLns9_XXyiO2HkldjZhkFCXwnHezUtaKG1oTTu5WzzgN15OSHeC_bOF0zMRr3_szxbotA3jUYA4seMJ0DOoYkYvs4Dx9Cy-4dwiyJGfdAJwtltVtkQ'
}

list = requests.request("GET", url, headers=headers2, data=payload2)

print(list.text)
