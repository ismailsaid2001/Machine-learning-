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
    L=(f.read()).split("\n")
    print(L)