#1)Escriba una función que muestre todos los números primos entre 1 y un número n que es
#ingresado por parámetro

"""def numero_primo(numero):
    primos=[]
    for num in range(1,numero+1):
        primo=True
        for i in range(2,num):
            if num % i == 0 :
                primo =False
                break
        if primo:
            primos.append(num)
    return primos

numero1=int(input("ingresa numero: "))
print(numero_primo(numero1))"""

    
#2) Escriba una función que le pida al usuario ingresar condimentos para un sándwich, hasta
#que el usuario ingrese ‘salir’. Cada vez que se ingrese un condimento, muestre un mensaje
#avisando que ya se agregó el condimento al sándwich. Escriba versiones diferentes del
#programa de acuerdo a estos criterios:
#• Use un test condicional en el ciclo while para detener la ejecución.
#• Use un test condicional dentro del ciclo para decidir si continuar la ejecución.
    
"""def hacer():
    condimento=""
    condimentos=[]
    while condimento!="lo termine":
        condimento=input("ingresar condimento:")
        if condimento!="salir":
            condimentos.append(condimento)
            print("se agrego condimento:")
    print("samwitch listo")        
            
hacer()"""

"""def hacer():
    continuar=True
    condimentos=[]
    while continuar:
        condimento=input("ingresar condimento:")
        if condimento=="salir":
            continuar=False
        else:
            print("se agrego condimento")   
            condimentos.append(condimento) 
    print("sanwitch listo")   

hacer()"""
#3)

"""def hacer_remera(tamaño,mensaje):
    print(f"el tamaño sera {tamaño} y el mensaje sera {mensaje} " )
tamaño=int(input("ingresar tamaño:"))
mensaje=str(input("ingresar mensaje:"))
hacer_remera(tamaño,mensaje)

def hacer_remera(tamaño="l",mensaje="me gusta python"):
    print(f"el tamaño sera {tamaño} y el mensaje sera {mensaje}  ")"""

"""while True:
    hacer_remera()
    if input("desea alterar la remera?")=="si":
        tamaño=int(input("ingresar tamaño:"))
        mensaje=str(input("ingresar mensaje:"))
        hacer_remera(tamaño,mensaje)

    if input("hacer otra remera?")=="no":
        break    """

#4) Serie de Fibonacci: Escriba una función fibonacci(n) que devuelva los n primeros numeros
#de la serie de Fibonacci. En esta serie, los primeros dos números son 0 y 1, y cada sucesivo
#número es la suma de los dos números inmediatamente anteriores (ejemplo: 0,1,1,2,3,5,8, ...)

def fibonacci(vueltas):
    f=[0,1]
    while len(f)<vueltas:
        f.append(f[-1]+f[-2])
    return f

vueltas=int(input("cuantos vueltas?:"))
print(fibonacci(vueltas))