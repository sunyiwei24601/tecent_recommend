import pandas as pd

data=pd.read_csv("merge_result_train.csv")

for i in data :
	print(i)

data['interest1']
#把向量份额里先剔除
vector_feature=['appIdAction','appIdInstall','interest1','interest2','interest3','interest4','interest5','kw1','kw2',
                'kw3','topic1','topic2','topic3','uid']

ad_feature=['advertiserId','campaignId','creativeId','productId','productType',
            'creativeSize','no','adCategoryId']


for i in vector_feature:
	data=data.drop(i,axis=1)

for i in ad_feature:
	data=data.drop(i,axis=1)



for i in data:
	print(i)
	print(data[i].unique())
	print(len(data[i].unique()))

print(data.loc[(data['education'] == 1) & (data['os'] == '1 2'),'label'])

# print(data.loc(1))
# classifier创建一个根据兴趣向量的分类器

def classify_interest():
	pass


