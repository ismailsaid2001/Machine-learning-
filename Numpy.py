#Numpy Functions :
import numpy as np
A= np.array([[1,2,3],[5,4,6]])
#A=A.reshape((1,3)) the two have to have the same size:nb of elements
print(A)
print(A.ndim)
print(A.shape)
print(A.size) #number of elements
B=np.zeros((3,2))
print(B)
D=np.full((2,3),9)  #ca retourne une matrice pleine de 9
D2=np.array((2,3))
print(D)
print(np.random.randn(1,4)) #normal distribution :I need to more understand this function
np.eye(4) # matrice identité 4*4
print(np.linspace(1,10,5,dtype=float))
#exercice :
# def initialisation(n,m):
#     # m :nombre de lignes
#     # n :nombre de colonnes
#     A=np.random.randn(n,m)
#     B=np.ones((n,1))
#     return(np.hstack(A,B))
# initialisation(4,2)
A = np.random.randn(4, 2)
B = np.ones((4, 1))
print(A)
print(A.shape)
print(B.shape)
print(B)
C=np.concatenate((A, B),axis=1 )
print(C)
