texto = ["Hola","Adios","Frio","Calor"]
numeros = [2, 3, 5, 7, 11, 13]
varios =["Jueves",7,"Febrero",36.2]
print(texto)
print(numeros)
print(varios)
texto1=texto[-1]
numeros1=numeros[-1]
varios1=varios[-1]
print("La primera variable contiene:",texto1,"La segunda variable contiene:",numeros1,"La tercera variable contiene:",varios1)
pelis={"LOTR":"Peter Jackson",1:"El señor de los anillos 1","LOTR":"Peter Jackson",2:"El señor de los anillos 2","LOTR":"Peter Jackson",3:"El señor de los anillos 3"}
print(pelis)
for x in pelis.keys():
    print(x)
for x in pelis.values():
    print(x)
