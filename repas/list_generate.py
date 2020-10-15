#L'usuari introdueix dos nombre enters, inici i final i es genera una llista
#Pista: list.append()

mylist = list()

inici = int(input("Introdueix l'inici"))
final = int(input("Introdueix el final"))

x = range(inici,final)
for n in x:
    mylist.append(n)
    ++n
    print(n)



print(mylist)




