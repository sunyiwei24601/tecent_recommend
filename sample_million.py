import pandas as pd
df=pd.read_csv('train.csv')
df=df.sample(n=1000000)
df.to_csv('train_sample_million.csv')