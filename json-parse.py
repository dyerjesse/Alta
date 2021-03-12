import json

with open('snowboard-db.json', 'r') as file:
	data = json.load(file)

print(data)