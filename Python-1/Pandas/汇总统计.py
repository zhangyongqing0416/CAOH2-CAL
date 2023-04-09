from pandas import DataFrame
import numpy as np
import pandas as pd
inputfile=r'D:\stud.csv'
data=pd.read_csv(inputfile,encoding='gbk')
df=DataFrame(data)
print(df.head(3))
print(df['sub_score'].std())
df1=df.loc[:,['stud_code','sub_code','sub_nmae','sub_tech','sub_score']]
df2=df1.fillna({'sub_tech':'2018-11-05'})
print(df2.head(3))
df21=df2.loc[:,['sub_nmae','sub_score']].head(5)
df22=pd.pivot_table(df21,index='sub_nmae',values='sub_score')
print(df22)
