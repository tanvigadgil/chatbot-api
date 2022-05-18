
import json

f = open('mental_disorders.json')


data = json.load(f)

for i in data['name']:
	if i['disorder'] == "Anoreksia Nervosa":
		print(i['short_description'])


f.close()
