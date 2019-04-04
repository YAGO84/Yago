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

def operacion(lista):
    print(lista)

def Salir(): 
    print("HASTA LUEGO!")

		
opc={'1':suma,'2':resta,'3':multiplica,'4':divide,'5':exponencial, '6':operacion}	
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
        if opcion>'0' and opcion<'8':
            if opcion=='7':
                Salir()
                break
            elif opcion=='6':
                op=input("Introducza la operacion a realizar: ")
                lista=[]
                if len(op)>2:
                    for i in op:
                        if i!=' ': 
                            lista.append(i)
                    opc[opcion](lista)
            else:    
                pn=float(input("Ingrese un Numero: "))
                sn=float(input("Ingrese otro Numero: "))
                opc[opcion](pn,sn)
        respuesta=str(input("Desea hacer otra operacion? [Si/No]: "))
        respuesta=respuesta.lower()
    except:
            print("Ha ocurrido un error.")

