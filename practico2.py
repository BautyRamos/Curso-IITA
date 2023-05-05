#1) Pida un número al usuario y determine si es par o impar.

"""usuario=int(input("ingresar numero: "))

if usuario % 2 == 0:
    print(f"el numero {usuario} es par")
else:
    print(f"el numero {usuario} es impar")"""

#2) Escriba una cadena if-elif-else que determine el estado de vida de una persona.
#• Si tiene al menos 2 años, pero menos de 4, muestre que es un infante.
# Si tiene al menos 4, pero menos de 12, muestre que es un niño.
#• Si tiene al menos 13, pero menos de 20, muestre que es un adolescente.
#• Si tiene al menos 20 pero menos de 65, muestre que es un adulto.
#• Si tiene 65 o más, muestre que es un anciano.

"""persona=int(input("si tiene:"))

if persona < 4:
    print(f"tiene {persona} es un infante")
elif persona < 12:
    print(f"tiene {persona} es un niño")
elif persona < 20:
    print(f"tiene {persona} es un adolecentes")
elif persona < 65:
    print(f"tiene {persona} es un adulto")
else :
    print(f"tiene {persona} es un anciano")"""

#3) Cree un ciclo que nunca termine y ejecútelo. Puede probarlo haciendo que muestre algo enpantalla por cada pasada del ciclo. Para finalizarlo, presione Ctrl-C o el comando para detenerla ejecución correspondiente a su editor 

"""numero=100
suma=0

while True :
    print(numero)
    numero=numero+1"""



#4) Escriba un programa que contenga dos ciclos while anidados que muestre 
# los enteros del 1 al 100, diez números por línea, como se muestra abajo:
#1 2 3 4 5 6 7 8 9 10
#11 12 13 14 15 16 17 18 19 20
#21 22 23 24 25 26 27 28 29 30
#. . 91 92 93 94 95 96 97 98 99 100

"""posicion_de_numero=0
numero = 1
while numero <= 100:
     posicion_de_numero = 0
     linea = ""
     while posicion_de_numero != 10:
         linea += str(numero) + "-"
         numero += 1

         posicion_de_numero += 1
     print(linea)"""

# 5) Resuelva el ejercicio anterior usando solo un ciclo while 

numero = 1
while numero <= 100:
     if numero % 10 == 0:
        print(numero)
     else:
         print(numero,end = "-")
     numero += 1