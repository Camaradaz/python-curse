print("*************************************")
print("*Reconoce o numero mais grande porra*")
print("*************************************\n")

numero_uno = int(input("Introduce el primer número entero: "))
numero_dos = int(input("Introduce el segundo número entero: "))
numero_tres = int(input("Introduce el tercer número entero: "))

if numero_uno > numero_dos and numero_uno > numero_tres:
    print("El numero:" ,numero_uno, "es el más grande")
elif numero_dos > numero_tres and numero_dos > numero_uno:
    print("El numero:" ,numero_dos, "es el más grande")
else:
    print("El número", numero_tres, "es el número más grande.")