#why is list comprhension bettter than classic method :
import  time
start=time.time()
L=[]
# for i in range(1,1000000) :
#     L.append(i**2)
# end=time.time()
# start2=time.time()
# L=[i**2 for i in range(1,1000000)]
# end2=time.time()
# # print(L)
# print(end-start)
# print(end2-start2)
L=[[i**2 for i in range(j)] for j in range(2,5)]
print(L)
prenoms=["ismail","emna","ahmed"]
ages=[20,18,6]
dic={}
dic={prenom:age for prenom,age in zip(prenoms,ages) if age>10 }
print(dic)
#with tuples we have to add tuple key word
tuple_1=tuple(i**3 for i in range(10))
print(tuple_1)
#exercice :
dic2={k:k**2 for k in range(20)}
print(dic2)