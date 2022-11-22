# Liste=('Paris','Tunis')
# pays={}
# pays=pays.fromkeys(Liste,1)
# print(pays.get('Paris'))
# print(pays.items())
#ex video 5/30 :
classeur= {
    "positif": [] ,
    "negatif": [],

}
def trier(classeur,nombre):
    if(nombre>0) :

        classeur["positif"].append(nombre)
    else :
        classeur["negatif"].append(nombre)

    return (classeur)
trier(classeur,5)
trier(classeur,-3)
trier(classeur,4)
trier(classeur,4)
print(classeur)