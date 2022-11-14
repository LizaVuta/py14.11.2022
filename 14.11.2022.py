import pandas as pd
df= pd.read_csv('C:/Users/digdepstudent/Documents/Вута/14.11.2022/py14.11.2022/data.tsv', sep='\t', index_col = 'ID'
)
#print(df.head())
#print(df.tail())
#rint(df.to_string())
print(df.info())
df=df.dropna(axis=0)

x= df['age'].mean()
df['age'].fillna(x, inplace= True)
print(df.to_string())
print(df.info())
df.drop_duplicates(inplace= True)
print(df.to_string())
print(df.info())
df['sex_num']=0.0
print(df.to_string())