import numpy as np

nd9=np.random.random([5,5])
np.savetxt(X=nd9,fname='./test1.txt')
nd10=np.loadtxt('./test1.txt')
print(nd10)