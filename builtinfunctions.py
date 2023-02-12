dic1={
"w1":1,
"w2":2,
"w3":3
}
for i in range(1,4):
    print(dic1[f"w{i}"])
#fichiers :
f=open('fichier.txt','w')
f.write('bonjour')
f.close()
f=open('fichier.txt','r')
print(f.read())
f.close()
with open('fichier.txt','r') as f :
    print(f.read())
#ex1
f=open("fichier.txt",'w')
for i in range(10):
    f.write(f"{i}^2 ={i*2}\n")
f.close()
with open("fichier.txt",'r') as f :
    L=[]
    L=(f.read()).split("\n") #you can use
    print(L)
#just split() with no parameters means any white space aith any length
#you can use readlines and split() also
liste=[line.strip() for line in open('fichier.txt','r')]
print(liste)
#rq split("\n") et splitlines sont equivalentes
#there is a function called readlines() that transform a string into a list but keeps \n