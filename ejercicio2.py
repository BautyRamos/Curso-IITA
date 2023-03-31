"""Escribí un programa que solicite al usuario ingresar tres números para luego
mostrarle el promedio de los tres"""

"""Usuario=input("ingresar tres numeros")
Numero="ingresar numero"
print(Numero,"100")
print(Numero,"200")
print(Numero,"300")

print(100+200+300)
print(600//3)"""

#lista="hola como estas"
#
#print(lista[:4])

lista=[]
es_primo=input("ingresar numero:")
def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True

