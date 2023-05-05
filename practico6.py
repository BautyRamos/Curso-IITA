#1) Escribir una clase llamada Rectángulo que contenga una base y una altura, y que contenga un método que devuelva el área
#del rectángulo. 


"""class Rectangulo:
    Base=0
    Altura=0
    def __init__(self,base,altura):
        self. Base=base
        self.Altura=altura

    def Area(self):
        return self.Base*self.Altura

Rectangulo1=Rectangulo(10,10)
print(Rectangulo1.Area())"""

#2) Modelar una clase Mate que describa el funcionamiento de la conocida bebida tradicional argentina. La clase debe contener
#como miembros:
#o Un atributo para la cantidad de cebadas restantes hasta que se lava el mate (representada por un número).
#o Un atributo para el estado (lleno o vacío).
#o Un atributo n, que indica la cantidad máxima de cebadas.
#o Un método cebar, que llena el mate con agua. Si se intenta cebar con el mate lleno, se debe lanzar una
#excepción que imprima el mensaje ¡Cuidado! ¡Te quemaste!
#o Un método beber, que vacía el mate y le resta una cebada disponible. Si se intenta beber un mate vacío, se
#debe lanzar una excepción que imprima el mensaje: ¡El mate está vacío!
#o Es posible seguir cebando y bebiendo el mate aunque no haya cebadas disponibles. En ese caso la cantidad
#de cebadas restantes se mantendrá en 0, y cada vez que se intente beber se debe imprimir un mensaje de aviso:
#“Advertencia: el mate está lavado.” pero no se debe lanzar una excepción.

"""class Mate:
    def __init__(self,cebadas=3,estado=False,limiteC=3):
        self.Cebadas=cebadas
        self.Estado=estado
        self.LimiteC=limiteC
    def cebar(self):
        if self.Estado==True:
            print("te quemaste")
        else:
            self.Estado=True

    def beber(self):
        self.Estado
        
Mate1=Mate(3,"lleno",9)
print(Mate1.cebar())
print(Mate1.beber())"""



#3) Botella y Sacacorchos
# Escribir una clase Corcho, que contenga un atributo bodega (cadena con el nombre de la bodega).
# Escribir una clase Botella que contenga un atributo corcho con una referencia al corcho que la tapa, o None si está
#destapada.
# Escribir una clase Sacacorchos que tenga un método destapar que le reciba una botella, le saque el corcho y se guarde
#una referencia al corcho sacado. Debe lanzar una excepción en el caso en que la botella ya esté destapada, o si el
#sacacorchos ya contiene un corcho.
# Agregar un método limpiar, que saque el corcho del sacacorchos, o lance una excepción en el caso en el que no haya
#un corcho.

"""class Corcho:
     def __init__(self, Bodega):
         self.Bodega=Bodega
    
     def __str__(self):
         return self.Bodega

class Botella:
     def __init__(self, Corcho:Corcho):
        self.CorchoDeBotella=Corcho

class Sacacorcho:
     def __init__(self):
        self.CorchoSacacorcho=None
    
     def Destapar(self,Botella:Botella):
         if self.CorchoSacacorcho==None:
             if Botella.CorchoDeBotella!=None:
                 self.CorchoSacacorcho=Botella.CorchoDeBotella
                 Botella.CorchoDeBotella=None
                 print("Botella destapada")
             else:
                 print("La botella ya esta destapada")
         else:
             print("El sacacorchos ya tiene un corcho, primero hay que limpiarlo")
            
     def Limpiar(self):
         if self.CorchoSacacorcho==None:
             print("El sacacorchos ya esta limpio")
         else:
             self.CorchoSacacorcho=None
             print("Sacacorcho limpiado")"""

#4) Una heladería es un tipo especial de restaurante. Cree una clase Restaurante, cuyo método __init__() guarde dos atributos:
#restaurante_nombre y tipo_comida. Cree un método describir_restaurante() que muestre estas piezas de información, y un
#método abrir_restaurante() que muestre un mensaje indicando que el restaurante ahora está abierto. Luego cree una clase
#Heladeria que herede de Restaurante, y agregue a los existentes un atributo llamado sabores que almacene una lista de los
#sabores de helado disponibles. Escriba también un método que muestre estos valores, cree una instancia de la clase y llame
#al método

class Restaurante:
    restaurante_nombre="mostaza"
    tipo_comida="hamburguesa"
    def __init__(self,restaurante_nombre,tipo_comida):
        self.describir_restaurante=restaurante_nombre and tipo_comida
        self.abrir_resaurante=("abierto")
    
class Heladeria(Restaurante):
    sabores="chocolate,vainilla y frutilla"
    def __init__(self,sabores):
        self.sabores_helado=sabores
    




