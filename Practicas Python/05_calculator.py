def suma(a,b):
    print("La suma es:",a+b)

def resta(a,b):
    print("La resta es:",a-b)

def multiplica(a,b):
    print("La multiplicación es:",a*b)

def divide(a,b):
    print("La división es:",a/b)

def exponencial(a,b):
    print("La exponencial es:",a**b)

def operacion(list):
    for operador in lista:
        operador=['+','-','*','/','//','x','X']
        for i in lista:
            if i== '*' or i == 'x' or i == 'X':
                posm=lista.index(i)
                r=float(lista[posm -1])*float(lista[posm+1])
                del list [posm-1:posm+2]
                lista.insert(posm-1,r)
        for i in lista:
             if i== '**':
                pose=lista.index(i)
                r=int(lista[pose -2])**int(lista[pose+1])
                del lista [pose-2:pose+2]
                lista.insert(pose-2,r)
        for i in lista:
             if i== '%' or i == '/':
                posd=lista.index(i)
                r=float(lista[posd -1])/float(lista[posd+1])
                del lista [posd-1:posd+2]
                lista.insert(posd-1,r)
             if i == '//':
                posd=lista.index(i)
                r=float(lista[posd -2])//float(lista[posd+1])
                del lista [posd-2:posd+2]
                lista.insert(posd-2,r)
        for i in lista:
             if i== '+':
                poss=lista.index(i)
                r=float(lista[poss -1])+float(lista[poss+1])
                del lista [poss-1:poss+2]
                lista.insert(poss-1,r)
        for i in lista:
             if i== '-':
                posr=lista.index(i)
                r=float(lista[posr -1])-float(lista[posr+1])
                del lista [posr-1:posr+2]
                lista.insert(posr-1,r)
    
    print("El resultado de su operacion es :",list[0])   
    
def Salir(): 
    print("HASTA LUEGO!")

		
opc={'1':suma,'2':resta,'3':multiplica,'4':divide,'5':exponencial,'6':operacion}	
respuesta="si"
while respuesta!="no":
    try:
        print("+"  +15 * '-' + '+')
        print(("|" + ' ' * 15 +'|\n') *1,end='')
        print(("|" + '-' * 15 +'|\n') *2,end='')
        print(("|" + ' ' * 15 +'|\n') *1,end='')
        print(("|" + ' ' * 2 + '7' + ' ' * 2 + '8' + ' ' * 2 + '9' + ' ' * 4 + '%'+ ' ' * 1 + '|\n') *1,end='')
        print(("|" + ' ' * 15 +'|\n') *1,end='')
        print(("|" + ' ' * 2 + '4' + ' ' * 2 + '5' + ' ' * 2 + '6' + ' ' * 4 + '-'+ ' ' * 1 + '|\n') *1,end='')
        print(("|" + ' ' * 15 +'|\n') *1,end='')
        print(("|" + ' ' * 2 + '1' + ' ' * 2 + '2' + ' ' * 2 + '3' + ' ' * 4 + '+'+ ' ' * 1 + '|\n') *1,end='')
        print(("|" + ' ' * 15 +'|\n') *1,end='')
        print(("|" + ' ' * 2 + '+-' + ' ' * 1 + '0' + ' ' * 2 + ',' + ' ' * 4 + 'X'+ ' ' * 1 + '|\n') *1,end='')
        print(("|" + ' ' * 15 +'|\n') *1,end='')
        print("+" + 15 * '-' + '+')
        print ('''CALCULADORA\n1) SUMAR \n2) RESTAR \n3) MULTIPLICAR \n4) DIVIDIR \n5) EXPONENCIAL \n6) OPERACION COMPLEJA \n7) SALIR''')
        opcion=input("Ingrese la opcion deseada: ")
        if opcion>'0' and opcion<'8' and len(opcion)==1:
            if opcion=='7':
                Salir()
                break
            elif opcion=='6':
                op=str(input("Introducza la operacion a realizar: "))
                list=[]
                lista=[]
                var=''
                operador=''
                if len(op)>3:
                    for i in op:   
                        if i!=' ':
                            if i.isdigit()or i=='.' or i==',':
                                var=var+i
                                if operador!='':
                                    list.append(operador)
                                    operador=''
                            else:
                                list.append(var)
                                var=''
                                if i == '*' or i=='/':
                                    operador=operador+i
                                else:
                                    list.append(i)
                    if var!='':
                        list.append(var)

                else:
                    print("La operacion es incorrecta")

                for i in list:
                    if i!= '':
                        lista.append(i)      
                opc[opcion](lista)
                respuesta=str(input("Desea hacer otra operacion? [Si/No]: "))
                respuesta=respuesta.lower()
            else:    
                pn=float(input("Ingrese un Numero: "))
                sn=float(input("Ingrese otro Numero: "))
                opc[opcion](pn,sn)
                respuesta=str(input("Desea hacer otra operacion? [Si/No]: "))
                respuesta=respuesta.lower()
    except:
            print("Ha ocurrido un error.")
