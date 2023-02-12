import math
import random
import statistics
import os
import glob
#math :
# print(math.cos(math.pi))
#statistics
liste=[2,10,6,2,10,6]
# print(statistics.mean((liste)))
# print(statistics.variance(liste))
#random
# print(random.choice(liste))
#to have always the same random number
random.seed(3)
print(random.choice(liste))
print(random.randint(5,10))
print(random.randrange(100)) #only one number means the stop integer
#echantillon :
# print(random.sample(range(100),10))
# #ici la population  est de 0 a 99 et l'echatillon N=10
# random.shuffle(liste) #ne retourne rien c'est une procedure change l'ordre
# print(liste)
#os :
# print(os.getcwd()) #retourne the currrent workin directory
#glob
print(glob.glob("*")) #tous les elements sur le rep de travail
print(glob.glob("*.txt"))
#exercice :

