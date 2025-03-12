consumo = int(input("Ingrese la cantidad de consumo en m³: "))
habitantes = int(input("Ingrese el número de habitantes: "))

if consumo < 15:
    tarifa = 5
elif 15 <= consumo <= 30:
    if habitantes > 3:
        tarifa = 4
    elif habitantes == 3:
        tarifa = 4.5
    else:
        tarifa = 5
else:
    if habitantes > 5:
        tarifa = 3.5
    elif habitantes % 2 == 0:
        tarifa = 4
    else:
        tarifa = 4.2

costo_total = consumo * tarifa

print("Consumo: ", consumo, "m³")
print("Habitantes: ", habitantes)
print("Tarifa: Q", tarifa, "por m³")
print("Costo total: Q", costo_total)
