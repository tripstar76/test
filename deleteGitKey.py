#!/usr/bin/env python3
import json
import requests


#################
# retrieve json
#################

with open("/media/HDD/Scripting/GIT/auth.txt", "r") as f:
	AUTH_TOKEN = f.readline().rstrip()

url = "https://api.github.com/user/keys"
headers = {
	'Authorization': f'token {AUTH_TOKEN}',
}

with requests.get(url, headers=headers) as data:
	data_dict = data.json()
	print(f"response from request keys: {data}")

# test = {}
# for key in data_dict:
	# print(key['title'])
	# test[key['title']] = key['id']

if not input("Delete Key? (y/n): ").lower().strip()[:1] == "y": print("no delete"); exit()

for key in data_dict:
	# print(key['title'])
	if key['title'].startswith("voron3"):
		print(key['id'])
		print(key['title'])
		index = data_dict.index(key)
		print(f"The index of {key['title']}, id {key['id']} is", index)
		if not input("Delete Key? (y/n): ").lower().strip()[:1] == "y": print("no delete"); break
		response = requests.delete(f"https://api.github.com/user/keys/{key['id']}", headers=headers)
		print(response)
		print("deleted")
	else:
		print(key['title'])
print("done")

