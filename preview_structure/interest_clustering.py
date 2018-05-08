import numpy as np
from kmodes.kmodes import KModes
import pandas as pd
import os
from sklearn.preprocessing import OneHotEncoder
# random categorical data
#data = np.random.choice(20, (100, 10))
#将一个向量分组为n维
def split_ser(d):
	for  k in d:
		line=k
	if isinstance(line,float):
		#print(line)
		features=[]
		return features
	lines=line.split(' ')
	ints=[]
	for j in lines:
		ints.append(int(j))
	#print(ints)
	return ints

def change_onehot(ints,lenth):
	a=[0]
	a=a*lenth
	for i in ints:
		a[i-1]=1
	return a

if os.path.exists("interest_clustering_100thousand.npy"):
	datas=np.load("interest_clustering_100thousand.npy")
	print("读取数据成功")
else:
	data=pd.read_csv("../merge_result_train.csv")
	vector=['interest1','interest2','interest3','interest4','interest5']
	terms=[]
	for i in range(int(len(data)/10)):
		# for i in range(100):

		if (i%1000 == 0): print(i)
		interest1=split_ser(data.interest1[i:i+1])
		interest2=split_ser(data.interest2[i:i+1])
		interest3=split_ser(data.interest3[i:i+1])
		interest4=split_ser(data.interest4[i:i+1])
		interest5=split_ser(data.interest5[i:i+1])
		lenth=[122,82,10,10,136]
		a=[]
		a+=change_onehot(interest1,lenth[0])
		a+=change_onehot(interest2,lenth[1])
		a+=change_onehot(interest3,lenth[2])
		a+=change_onehot(interest4,lenth[3])
		a+=change_onehot(interest5,lenth[4])
		terms.append(a)
	datas=np.array(terms)
	np.save("interest_clustering_100thousand.npy",datas)



km = KModes(n_clusters=30, init='Huang', n_init=5, verbose=1)
clusters = km.fit_predict(datas)

# Print the cluster centroids
print(clusters)
np.save("result_clusters.npy",clusters)