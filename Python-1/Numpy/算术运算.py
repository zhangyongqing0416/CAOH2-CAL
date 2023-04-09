import numpy as np

A=np.array([[1,2],[-1,4]])
B=np.array([[2,0],[3,4]])
print(A*B)

X=np.random.rand(2,3)
def softmoid(x):
    return 1/(1+np.exp(-x))
def relu(x):
    return np.maximum(0,x)
def softmax(x):
    return np.exp(x)/np.sum(np.exp(x))

print("输入参数X的形状:",X.shape)
print("激活函数softmoid的形状:",softmoid(X).shape)
print("激活函数relu的形状:",relu(X).shape)
print("激活函数softmax的形状:",softmax(X).shape)
print(X)
print(softmoid(X))
print(relu(X))
print(softmax(X))

#点积运算
X1=np.array([[1,2],[3,4]])
X2=np.array([[5,6,7],[8,9,10]])
X3=np.dot(X1,X2)
print(X3)