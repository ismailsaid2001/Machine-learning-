import numpy as np
# A=np.array([[1,2,3],[5,1,6]])
# print(A[np.isnan(A)])
# print(A<5)
# print(np.mean(A)) #moyenne
# print(np.std(A)) #ecart type
# print(np.var(A,ddof=1)) #variance sans biais
# #correlation
# x=np.corrcoef(A)
# print(np.unique(A,return_counts=True))
# print(x)
# # A.sort()
# values,counts=np.unique(A,return_counts=True)
# print(np.argsort(counts)) #pour avoir une idée sur la redondance
# # print(values[np.argsort(counts)])
# c=np.array([1,2,3]) #avec un arrau numpy on peut slectionner plusieurs elements à la fois
# print(values[c])
# for i,j in zip(values[np.argsort(counts)],counts[np.argsort(counts)] ) :
#     print(f'le nb d ocurence de {i} est {j}')
A=np.array([[1,2,2],[4,5,7],[2,4,7]])
print(A.mean(axis=0))