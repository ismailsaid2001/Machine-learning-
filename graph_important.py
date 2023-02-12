import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris=load_iris()
x=iris.data
y=iris.target
# names=list(iris.target_names)
plt.scatter(x[:,0],x[:,1],c=y,alpha=0.5,s=x[:,2]*100)
plt.xlabel("longeur sépal")
plt.ylabel("largeur sépal")
plt.show()