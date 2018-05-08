import pandas as pd

data=pd.read_csv("merge_result_train.csv")


interest=data['interest1']

interests=[]
for i in interest:
	nums=i.split(" ")
	print(nums)