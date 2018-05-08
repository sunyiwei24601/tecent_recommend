import json
import csv



def get_data(rows):
	with open('userFeature.data') as f:
		datas=[]
		for i in range(rows):
			line=f.readline()
			features=line.split('|')
			print(features)
			data={}
			for feature in features:

				cols=feature.split(' ')
				data[cols[0]]=cols[1:]
			datas.append(data)
	return datas


rows=100000

datas=get_data(rows)

with open('userFeature{}.json'.format(rows),'w') as f:
	json.dump(datas,f)

