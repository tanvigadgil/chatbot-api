
import json

f = open('mental_disorders.json')


data = json.load(f)

for i in data['disorder']:
	if i['name'] == "OCD":
		print(i['response'])
		break


f.close()
