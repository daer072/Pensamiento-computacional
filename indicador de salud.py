dias = ["lunes","martes","miercoles","jueves","viernes"]
niveles_azucar = [190, 160, 95, 175, 160]  # mg/dL
niveles_sal = [2000, 2400, 1800, 2400, 2700]  # mg
presion = [115, 130, 110, 125, 175]  # mmHg


azucar_min =70
azucar_max = 140
limite_sal=2300


total_azucar = 0
total_sal = 0
total_presion = 0

#conexion de listas de niveles con lista de dias 
i = 0
while i < len(dias):
    dia = dias[i]
    azucar = niveles_azucar[i]
    sal = niveles_sal[i]
    presion_sistolica = presion[i]

    # azúcar
    if azucar >= azucar_min and azucar <= azucar_max:
        alerta_azucar = "Normal"
    else:
        alerta_azucar = "¡Alerta! Azúcar fuera de rango"

    # sal
    if sal <= limite_sal:
        alerta_sal = "Normal"
    else:
        alerta_sal = "¡Alerta! Exceso de sal"

    # presión
    if presion_sistolica < 120:
        alerta_presion = "Normal"
    elif presion_sistolica >= 120 and presion_sistolica <= 129:
        alerta_presion = "¡Alerta! Elevada"
    elif presion_sistolica >= 130 and presion_sistolica <= 139:
        alerta_presion = "¡Alerta! Hipertensión Etapa 1"
    elif presion_sistolica >= 140:
        alerta_presion = "¡Alerta! Hipertensión Etapa 2"

    print(dia + ": Azúcar:", azucar, "mg/dL (" + alerta_azucar + "), Sal:", sal, "mg (" + alerta_sal + "), Presión:", presion_sistolica, "mmHg (" + alerta_presion + ")")

    total_azucar = total_azucar + azucar
    total_sal = total_sal + sal
    total_presion = total_presion + presion_sistolica

    i = i + 1  # Pasar al siguiente día

promedio_azucar = total_azucar / 5
promedio_sal = total_sal / 5
promedio_presion = total_presion / 5

print ("\n promedios de la semana")
print ("azucar promedio:", promedio_azucar, "mg/dL")
print ("sal promedio:", promedio_sal, "mg/dL")
print ("presion promedio:",  promedio_presion, "mg/dL")
