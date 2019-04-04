lista=['andres','manolo','pepe','pedro','andres','luis']
selected=[]
for x in range(len(lista)-1):
    if 'a' in lista[x]:
        selected.append(lista[x])
print(selected)
