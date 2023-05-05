#1. Escriba una función redondear() que permita redondear un número
#decimal de acuerdo al criterio: Si el número es mayor a 3.50, devolver el
#entero siguiente (en este caso, 4), si no devolver el entero inmediatamente anterior (3).
numero_mayor=3.50
numero=input("poner numero cual quiera:")
def redondear(numero):
    if numero<numero_mayor:
        return round(numero_mayor)
    elif numero>numero_mayor:
        return round(numero_mayor) 
  
#2.Coloque el módulo del ejercicio anterior dentro de un paquete. En un
#módulo que esté fuera de ese paquete, cree una función de suma de
#decimales que redondee el resultado haciendo uso de la función
#redondear() del paquete recién creado

#import archivo 







#3. Usando el módulo datetime, escribe un programa que muestre la fechay hora actuales del sistema

"""import datetime
fecha_actual=datetime.datetime.now()
print(fecha_actual)"""

#4. Escriba un programa que devuelva un número par al azar entre 2 y 10
#(pista: para comprobar si se pueden generar todos los números, pruebe
#ejecutar el programa dentro de un ciclo infinito).


"""numero=100
suma=0

while True :
    print(numero)
    numero=numero+1
    for i in range(2)"""









#5. Bola mágica: La bola mágica (Magic 8 ball) es un popular juguete usado
#para la adivinación o para buscar consejo. Su mecanismo es muy simple:
#ante una pregunta del usuario, la bola responde con una de 8 posibles
#respuestas:
#- Es seguro que sí
#- Las chances son buenas
#- Puedes contar con ello
#- Pregúntame de nuevo más tarde
#- Concéntrate y pregunta de nuevo
#- No veo con claridad, intenta de nuevo
#- Mi respuesta es no
#- Mis fuentes me dicen que no
#Escriba una función en Python para simular la bola mágica

"""import random
input("haz tu pregunta:")
respuesta=random.randint(1,8)
if respuesta==1:
    print("Es seguro que sí")
elif respuesta==2:
    print("Las chances son buenas")
elif respuesta==3:
    print("Puedes contar con ello")
elif respuesta==4:
    print("Pregúntame de nuevo más tarde")
elif respuesta==5:
    print("Concéntrate y pregunta de nuevo")
elif respuesta==6:
    print("No veo con claridad, intenta de nuevo")
elif respuesta==7:
    print("Mi respuesta es no")
else:
    print("Mis fuentes me dicen que no")"""
#6.Encuentre el tiempo de ejecución de los programas de los ejercicios
#anteriores (pista: use el módulo time)






