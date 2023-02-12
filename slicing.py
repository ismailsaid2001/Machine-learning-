# import numpy as np
# B=np.zeros((4,4))
# B[1:-1,1:-1]=1
# print(B[:,:])
# # rq:we shall use :: when we want to select all the items and using a step
# c=np.random.randint(1,10,[5,5])
# print(c<5)
# c[c<5]=3
# print(c)
# d=c[c<5]
# print(d)
# print(d.shape) #c'est un tableau à une seule dimension
#exercice
import numpy as np
from scipy import misc
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
face=misc.face(gray=True)
print(face)
print(face.ravel())
A=face[int(0.25*face.shape[0]):face.shape[0]-int(0.25*face.shape[0]),int(0.25*face.shape[1]):face.shape[1]-int(0.25*face.shape[1])]
#plus claire :
h=face.shape[0]
w=face.shape[1]
B=A[h//4:-h//4,w//4-w//4]
plt.imshow(A,cmap=plt.cm.gray)
print(A.shape)
A[A<100]+=50
# plt.imshow(A,cmap=plt.cm.gray)
# plt.imshow(face,cmap=plt.cm.gray)
plt.show()
#pour "compresser une image on procéder comme ça : A[::2;::2]