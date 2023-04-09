import numpy as np

arr=np.arange(10)
print(arr)
#不修改向量本身
print(arr.reshape(-1,5))
#修改向量本身
arr.resize(5,2)
print(arr)
#转置
print(arr.T)
print(arr.ravel())