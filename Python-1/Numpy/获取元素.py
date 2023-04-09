import numpy as np
np.random.seed(2019)
nd11=np.random.random([10])
nd11[3]
nd11[1:6:2]
nd11[::-2]
nd12=np.arange(25).reshape([5,5])
nd12[1:3,1:3]

nd12[(nd12>3)&(nd12<10)]

nd12[[1,2]] #或nd12[1:3,:]

nd12[:,1:3]