def mayor_menor_edad(lista):
    for i in lista:
        if i >= 18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")

mayor_menor_edad([18,21,8,19,5,4,3,8,2,3])