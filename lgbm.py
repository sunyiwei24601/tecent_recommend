import pandas as pd
import numpy as np
import lightgbm as lgb
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import OneHotEncoder,LabelEncoder
from scipy import sparse



print("Loading Data")

def read_csv_file(f,logging=False):
	data=pd.read_csv(f)
	if logging:
		print(data.head(5))
		print(f,"包含以下列")
		print(data.columns.values)
	return data

train=read_csv_file("merge_result_train.csv")
train=train.fillna('-1')
#剥离向量属性

one_hot_feature=['LBS','age','carrier','consumptionAbility','education','gender','house','os','ct','marriageStatus','advertiserId','campaignId', 'creativeId',
       'adCategoryId', 'productId', 'productType']
vector_feature=['appIdAction','appIdInstall','interest1','interest2','interest3','interest4','interest5','kw1','kw2','kw3','topic1','topic2','topic3']

data=train
#将特征转化为序列数
for feature in one_hot_feature:
    try:
        data[feature] = LabelEncoder().fit_transform(data[feature].apply(int))
    except:
        data[feature] = LabelEncoder().fit_transform(data[feature])

#选取不是-1的列
# train=data[data.label!=-1]
# # 取出label
# train_y=train.pop('label')
# test=data[data.label==-1]
# res=test[['aid','uid']]
# test=test.drop('label',axis=1)
# enc = OneHotEncoder()
# train_x=train[['creativeSize']]
# test_x=test[['creativeSize']]
#
# for feature in one_hot_feature:
#     enc.fit(data[feature].values.reshape(-1, 1))
#     train_a=enc.transform(train[feature].values.reshape(-1, 1))
#     test_a = enc.transform(test[feature].values.reshape(-1, 1))
#     train_x= sparse.hstack((train_x, train_a))
#     test_x = sparse.hstack((test_x, test_a))
#     print(feature+' finish')
# print('one-hot prepared !')
#
# cv=CountVectorizer()
# for feature in vector_feature:
#     cv.fit(data[feature])
#     train_a = cv.transform(train[feature])
#     test_a = cv.transform(test[feature])
#     train_x = sparse.hstack((train_x, train_a))
#     test_x = sparse.hstack((test_x, test_a))
#     print(feature + ' finish')
#


# train_y=train.loc[:,'label']
#
# train_x=train.drop('label',1)
# X, val_X, y, val_y = train_test_split(
#     train_x,
#     train_y,
#     test_size=0.05,
#     random_state=1,
#     stratify=train_y ## 这里保证分割后y的比例分布与原数据一致
# )
# X_train = X
# y_train = y
# X_test = val_X
# y_test = val_y
# lgb_train = lgb.Dataset(X_train, y_train)
# lgb_eval = lgb.Dataset(X_test, y_test, reference=lgb_train)
# params = {
#     'boosting_type': 'gbdt',
#     'objective': 'binary',
#     'metric': {'binary_logloss', 'auc'},
#     'num_leaves': 5,
#     'max_depth': 6,
#     'min_data_in_leaf': 450,
#     'learning_rate': 0.1,
#     'feature_fraction': 0.9,
#     'bagging_fraction': 0.95,
#     'bagging_freq': 5,
#     'lambda_l1': 1,
#     'lambda_l2': 0.001,  # 越小l2正则程度越高
#     'min_gain_to_split': 0.2,
#     'verbose': 5,
#     'is_unbalance': True
# }
#
# # train
# print('Start training...')
# gbm = lgb.train(params,
#                 lgb_train,
#                 num_boost_round=10000,
#                 valid_sets=lgb_eval,
#                 early_stopping_rounds=500)
#
# print('Start predicting...')
#
# preds = gbm.predict(X_test, num_iteration=gbm.best_iteration)  # 输出的是概率结果