import pandas as pd
df= pd.read_csv('C:/Users/digdepstudent/Documents/Вута/14.11.2022/py14.11.2022/data.tsv', sep='\t', index_col = 'ID')
print(df.to_string())