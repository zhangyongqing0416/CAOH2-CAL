import numpy as np
from pandas import Series,DataFrame
import pandas as pd

data={'name':['zhanghua','liuting','gaofei','hedong'],'age':[40,45,38,78],'addr':['jiangxi','hebei','beijing','shanghai']}
d3=DataFrame(data,columns=['name','age','addr'],index=['a','b','c','d'])
print(d3)
###添加行时要注意ignore_index=True,不然会报错
d4=d3.append({'name':'wangkang','age':38,'addr':'hebei'},ignore_index=True) 

d4.index=['a','b','c','d','e']
d4.loc['e','age']=39
print(d4)