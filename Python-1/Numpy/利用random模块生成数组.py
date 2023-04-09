import numpy as np

nd3=np.random.random([4,4])
print(nd3)
print("nd3的形状是：",nd3.shape)

import numpy as np
np.random.seed(1)
nd4=np.random.randn(2,3)
print(nd4)
np.random.shuffle(nd4)
print("随即后打乱数据:")
print(nd4)
print(type(nd4))