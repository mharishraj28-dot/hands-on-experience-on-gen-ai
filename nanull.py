import pandas as pd
import numpy as np

data={'name':['naveen','karthi','surya','deepak'],'age':[12,17,np.nan,19],'salary':[40000,45000,np.nan,75000],'dep':['cse','ece','it',np.nan]}
df=pd.DataFrame(data)
print(df)

print('total no:\n')
print(df.isnull().sum())

print('specific no:\n')
print(df[df.isnull().any(axis=1)])

print('specific no:\n')
print(df[df.notnull().all(axis=1)])

print('without nan values:/n')
print(df.dropna())

print('add valuse:/n')
df_dup=df.copy()

print('fill values:\n')
df_dup['age'].fillna(df['age'].mean(),inplace=True)
df_dup['salary'].fillna(0,inplace=True)
df_dup['age'].fillna('unknown',inplace=True)

print(df_dup)
print('dup columns:/n')
df_rename=df.copy()
df_rename=df.rename(columns={'name':'name_up','age':'age_up','salary':'salary_up'})
print(df_rename)
print('dup values:/n')
df_up=df_rename[['name_up','age_up','salary_up','dep']].copy()
print(df_up)
print('add columns:\n')
df_up['namo']=['a','b','c','d']
print(df_up)
print('dup values:\n')
print(df.drop('salary',axis=1))
