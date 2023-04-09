import numpy as np
nd5=np.zeros([3,3])
#生成与nd5形状一样的全0矩阵
#np.zeros_like(nd5)
#生成全是1的3✖3矩阵
nd6=np.ones([3,3])
#生成3阶单位矩阵
nd7=np.eye(3)
#生成三阶的对角矩阵
nd8=np.diag([1,2,3])
print(nd5)
print(nd6)
print(nd7)
print(nd8)