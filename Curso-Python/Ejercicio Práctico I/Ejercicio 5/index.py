print("******************************************")
print("*Ejercicio Práctico 5: Sucesión Fibonacci*")
print("******************************************\n")

numero_uno, numero_dos = 0, 1 
while numero_dos <= 1597:
    print(numero_uno, numero_dos, end= " ")
    numero_uno = numero_uno + numero_dos
    numero_dos = numero_uno + numero_dos 


