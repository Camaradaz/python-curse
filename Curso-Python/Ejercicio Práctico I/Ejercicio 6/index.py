#Ejemplo de break

print("while con sentencia break \n")
contador = 0
while contador < 10:
    contador += 1 

    if contador == 5:
        break
    print("el valor de la variable es: ",contador)

print("El programa ha finalizado.")

#Ejemplo continue
print("\nwhile con sentencia break \n")
contador = 0
while contador < 10:
    contador += 1 

    if contador == 5:
        continue
    print("el valor de la variable es: ",contador)
