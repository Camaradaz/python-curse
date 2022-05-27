def hola_marta():
    return "Hola Marta! Estoy programando en Python."
def hola(alguien):
    return "Hola" , alguien, "Estoy programando en Python."

def suma(a,b):
    resultado = a + b
    return resultado
def resta(c,d):
    resultado = c - d
    return resultado
def producto(e,f):
    resultado = e * f
    return resultado
def división(g,h):
    resultado = g / h
    return resultado
def cuadrado(n):
    return n * n

def suma_5_cuadrados():
    suma = 0
    suma = suma + cuadrado(1)
    suma = suma + cuadrado(2)
    suma = suma + cuadrado(3)
    suma = suma + cuadrado(4)
    suma = suma + cuadrado(5)
    return suma

def numeros():
    for x in [1,2,3,4,5,6,7,8,9,10]:
        print("Numero " + str(x))


        


