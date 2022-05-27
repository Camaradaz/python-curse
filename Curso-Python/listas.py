demo_list = [1, "hola", 3.4, True, [1, 2, 3]]
colors = ["Verde", "Rojo", "Azul"]

numbers_list = list((1, 2, 3, 4, 5, 6))
print(numbers_list)
#print(type(numbers_list))

#R = list(range(1, 101)) #Llega a un numero antes del parámetro
#print(R)
print(type(colors))
#print(dir(colors))
# print(len(colors))
# print(colors[1])
# print(colors[-3])
print('Verde' in colors) #Booleans
print('Violeta' in colors) #Booleans
#print(colors)
#colors[1] = "Amarillo"
print(colors) #Se puede editar, no como tuplas
#colors.append("Violeta") #Agregar elementos
#colors.extend (("Violeta", "Gris", "Dorado")) #Utilizar una tupla para agregar más de 1
#colors.remove("Rojo") #Remueve el elegido
#colors.pop() #Elimina el indice elegido
#colors.insert(-1, "Violeta")
#colors.clear() #Limpia toda la lista
#colors.sort() #Ordena alfabeticamente
#colors.sort(reverse=True) #Ordena al revés
print(colors.index("Rojo")) #Obtener indice
print(colors.count("Verde")) #Contar cuantos hay

