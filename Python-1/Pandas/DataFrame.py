import numpy as np
from pandas import Series,DataFrame
import pandas as pd

d1=DataFrame(np.arange(12).reshape((3,4)),columns=['a1','a2','a3','a4'],index=['a','b','c'])
print(d1)

data={'name':['zhanghua','liuting','gaofei','hedong'],'age':[40,45,38,78],'addr':['jiangxi','hebei','beijing','shanghai']}

d2=DataFrame(data)
print(d2)
d3=DataFrame(data,columns=['name','age','addr'],index=['a','b','c','d'])
print(d3)
