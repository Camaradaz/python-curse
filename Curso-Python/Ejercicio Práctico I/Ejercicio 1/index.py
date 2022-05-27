print("*******************************")
print("*Sistema de control vacacional*")
print("******************************* \n")

nombre_empleado = input("Por favor introduce el nombre del empleado: ")
clave_departamento = int(input("Por favor introduce la clave del departamento: "))
antiguedad_empleado = float(input("Por favor introduce la antiguedad del empleado: "))

if clave_departamento == 1:
    if antiguedad_empleado >= 1 and antiguedad_empleado <2:
        print("El empleado ", nombre_empleado, "tiene derecho a 6 (seis) días de vacaciones.")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <=6:
        print("El empleado ", nombre_empleado, "tiene derecho a 14 (catorce) días de vacaciones.")
    elif antiguedad_empleado >= 7:
        print("El empleado ", nombre_empleado, "tiene derecho a 20 (veinte) días de vacaciones.")
    else:
        print("Aún no tiene vacaciones.")


elif clave_departamento == 2:
    if antiguedad_empleado >= 1 and antiguedad_empleado <2:
        print("El empleado ", nombre_empleado, "tiene derecho a 7 (siete) días de vacaciones.")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <=6:
        print("El empleado ", nombre_empleado, "tiene derecho a 15 (quince) días de vacaciones.")
    elif antiguedad_empleado >= 7:
        print("El empleado ", nombre_empleado, "tiene derecho a 22 (veintidos) días de vacaciones.")
    else:
        print("Aún no tiene vacaciones.")

elif clave_departamento == 3:
    if antiguedad_empleado >= 1 and antiguedad_empleado <2:
        print("El empleado ", nombre_empleado, "tiene derecho a 10 (diez) días de vacaciones.")
    elif antiguedad_empleado >= 2 and antiguedad_empleado <=6:
        print("El empleado ", nombre_empleado, "tiene derecho a 20 (veinte) días de vacaciones.")
    elif antiguedad_empleado >= 7:
        print("El empleado ", nombre_empleado, "tiene derecho a 30 (treinta) días de vacaciones.")
    else:
        print("Aún no tiene vacaciones.")

else:
    print("La clave del departamento no existe, vuelve a intentarlo.")