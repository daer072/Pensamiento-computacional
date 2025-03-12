modelo = int(input("Ingrese el año del vehiculo: "))
placa = int(input("Ingrese el número con el que termina su la placa: "))

antiguedad = 2025 - modelo 

if placa % 2 == 0:
    print("No circula los lunes y solo puede circular hasta el medio dia los sabados")
elif placa % 2 == 1:
    print("No circula los viernes")

if antiguedad > 25:
    print("ADVERTENCIA: Su vehiculo necesita un mantenimiento obligatorio.")

