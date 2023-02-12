import matplotlib.pyplot as plt
import  numpy as np
import matplotlib
matplotlib.use('TkAgg')
import  matplotlib.pyplot
dataset={f"experience {i}":np.random.randn(100,3) for i in range(4)}
# fig,ax=plt.subplots(2,2)
#print(dataset.values())
x=np.random.randn(100,3)
plt.plot(x)
# print(x)
# print(dataset)
# for i in range(4) :
#     plt.subplot(2,2,i+1)
#     plt.plot(dataset[f"experience {i}"])
plt.show()
