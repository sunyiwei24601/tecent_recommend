import pandas as pd
import numpy as np

print("Loading Data")

def read_csv_file(f,logging=False):
	data=pd.read_csv(f)
	if logging:
		print(data.head(5))
		print(f,"包含以下列")
		print(data.columns.values)
	return data

def get_part(f,n,save_file):
	with open(f) as p:
		with open(save_file,'w') as s:
			for i in range(n):
				line=p.readline()
				s.write(line)

train_part=read_csv_file("train_sample_million.csv")
userFeature=read_csv_file("userFeature.csv")
adFeature=read_csv_file("adFeature.csv")
merge_data1=pd.merge(train_part,userFeature,how="left",on="uid")
merge_data2=pd.merge(merge_data1,adFeature,how="left",on="aid")
print(merge_data2)
import csv
merge_data2.to_csv("merge_result_train.csv",index=False)