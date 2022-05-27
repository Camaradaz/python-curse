def hola(nombre):
    return "Hola" + nombre + "!"

def saludar():
    nombre = input("Por favor ingrese su nombre: ")
    saludo = hola (nombre)
    print(saludo)

saludar()
