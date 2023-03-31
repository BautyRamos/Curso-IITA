#1) Meter los números del 1 al 20 en una lista y mostrarla en pantalla. Hacer lo mismo
#para un rango de números indicado por un usuario.

"""lista=[]

for i in range (1,21):
    lista.append(i)
    print(i)

print(lista)"""   

#2) Pide un número y guarda en una lista su tabla de multiplicar hasta el 10. Por
#ejemplo, si pide el 5 la lista tendrá: 5,10,15,20,25,30,35,40,45,50

"""numero=input("ingresar numero:")
lista=[]
for i in range (2,21,2):
    lista.append(i)
    print(i)

print(lista)"""
 
# 3) Pide una cadena (string) por teclado, mete los caracteres en una lista sin repetir
#caracteres.

"""caracteres=str(input("ingrese texto:"))

lista=[]

for i in range(len(caracteres)):
    if caracteres[i]!=" ":
        lista.append(caracteres[i])
print(lista)"""

#4) Pide una cadena (string) por teclado, mete los caracteres en una lista sin espacios

"""caracteres=str(input("ingrese texto:"))

lista=[]

for i in range(len(caracteres)):
    if caracteres[i]!=" ":
        lista.append(caracteres[i])
print(lista)"""

#5) Crea una tupla con números, pide un numero por teclado e indica cuantas veces se
#repite.


"""numeros = (3,6,99,0,1,23,4,4,1,4)
 
numero = int(input("Dame un numero: "))
 
contador= 0
for i in numeros:
    if numero == i:
        contador = contador + 1
 
print ("Hay ",contador," repeticion/es")"""



#6) Crea una tupla con los meses del año, pedir números al usuario. Si el numero esta
#entre 1 y la longitud máxima de la tupla, muestra el contenido de esa posición sino
#muestra un mensaje de error. El programa termina cuando el usuario introduce un
#cero

"""meses=("enero","febrero","marzo","abril","mayo","junio","julio","agosto"
             ,"septiembre","octubre","niviembre","diciembre")
usuario=False
while(not usuario):

    numero =int(input("dame un numero:"))

    if(numero==0):
        usuario= True
    else:
        if(numero>=1 and numero<=len(meses)):
            print(meses[numero-1])
        else:
            print("insertar un numero entre 1 y ",len(meses))"""

#7) Crea una tupla con números e indica el número con mayor valor y el que menor tenga

numeros = (5,6,3,-1,1,6,478,3,9,9,5,9)
 
maximo = numeros[0]
minimo = numeros[0]
 
for i in numeros:
    if i > maximo:
        maximo = i
 
    if i < minimo:
        minimo = i
 
print("El maximo es ",maximo)
print("El minimo es ",minimo)
