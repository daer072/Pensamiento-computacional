
saldo = 3000
intentos = 3

while saldo > 0 and intentos > 0:
    retiro = int(input("Ingrese la cantidad que desea retirar (o 0 para salir): "))

    if retiro == 0:
        print("Gracias por usar el cajero automático.")
        break
    elif retiro > saldo:
        print("Fondos insuficientes. Intente con una cantidad menor.")
        intentos -= 1  
        print("Intentos restantes:", intentos)
    elif retiro < 0:
        print("Ingrese una cantidad válida para retirar.")
    else:
        saldo -= retiro  # Actualizar saldo después del retiro
        print("Retiro exitoso. Su saldo actual es:", saldo)

    if saldo == 0:
        print("Su saldo se ha agotado. No puede realizar más retiros.")
        break

    if intentos == 0:
        print("Se han agotado sus intentos. Operación bloqueada.")

print("Cajero cerrado.")
