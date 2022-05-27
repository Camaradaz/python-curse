def cuadrado(n):
    return n * n
def suma_cuadrados(n): 
    suma = 0
    for x in range(1, n + 1):
         suma = suma + cuadrado(x)
    return suma

print("La suma de los primeros 100 cuadrados es", suma_cuadrados(100))

def hola(nombre):
    return "Hola " + nombre + "!"

def saludar():
    nombre = input("Por favor ingrese su nombre: ")
    saludo = hola(nombre)
    print(saludo)
    
saludar()

def imprimir_cuadrados():
    print("Bienvenido, se va a calcular los cuadrados de numeros enteros")

    n1= int(input("Ingrese un numero entero: "))
    n2= int(input("Ingrese otro numero entero: "))

    for x in range(n1, n2):
        print(x * x)
        print("¡Eso es todo por ahora!")

imprimir_cuadrados()


      
