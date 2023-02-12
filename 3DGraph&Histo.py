import numpy as np
from scipy import misc
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris=load_iris()
x=iris.data
y=iris.target
# names=list(iris.target_names)
from mpl_toolkits.mplot3d import Axes3D
# ax=plt.axes(projection='3d')
# ax.scatter(x[:,0],x[:,1],x[:,2],c=y)
# plt.show()
#visualisation de fonction
f=lambda x,y:np.sin(x)+np.cos(x+y)
X=np.linspace(0,5,100)
Y=np.linspace(0,5,100)

X , Y=np.meshgrid(X,Y)
Z=f(X,Y)
print(X[0])
print("********")
print(X)
# ax=plt.axes(projection='3d')
# ax.plot_surface(X,Y,Z,cmap='plasma')
# plt.hist(x[:,0],bins=20)
# plt.hist(x[:,1],bins=20)
# histogramme 2D :
# plt.hist2d(x[:,0],x[:,1],cmap='Purples')
# plt.xlabel('long sepal')
# plt.ylabel('larg sepal')
# plt.colorbar()
# plt.show()
face=misc.face(gray=True)
# plt.hist(face.ravel(),bins=255)
# plt.show()
# plt.contourf(X,Y,Z,cmap='RdGy')
# plt.colorbar()
# plt.imshow(face)
# plt.show()
#observation of matrix with imshow
plt.imshow(np.corrcoef(x.T),cmap='Blues')
plt.colorbar()
plt.show()
