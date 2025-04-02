# #EJERCICIO 1
#
# array = int(input("Ingrese el tamaño de su vector: "))
# multiplos = int(input("Ingrese su numero: "))
# salida =[]
# for i in range (0,array): # para i en el rango de 0 a lo que el usuario haya ingresado en la longitud de su arreglo
#     salida.append(i*multiplos) # "append" es para agregar a "salida" (que es un arreglo vacio) la multiplicacion de i con el numero de multiplos que el usuario haya ingresado
#     print(salida)
#     

#EJERCICIO 2
# tamaño = int(input("Ingrese el tamaño de sus vectores: "))
# nombres = []
# longitudes = []

# for i in range(tamaño):
#     nombre = input("Ingresa el nombre de la persona: " + str(i + 1))  # Concatenación para mostrar el número
#     nombres.append(nombre) 
#     longitudes.append(len(nombre)) 

# print("Nombres y longitudes:")
# for i in range(tamaño):
#     print("Nombre: " + nombres[i] + ", Longitud: " + str(longitudes[i]))  # Concatenación para mostrar valores

#ESCENARIO 1
# Mostrar el menú de opciones
print("5. Excelente")
print("4. Muy Buena")
print("3. Buena")
print("2. Regular")
print("1. Malo")

# Inicializar variables
clients = []  # Lista para almacenar las evaluaciones
clientes = int(input("Ingrese la cantidad de clientes evaluados: "))

# Registrar las evaluaciones de los clientes
for i in range(clientes):
    while True:
        evaluacion = int(input("Ingrese la evaluación del cliente " + str(i + 1) + " (5-Excelente, 4-Muy Buena, 3-Buena, 2-Regular, 1-Malo): "))
        if evaluacion >= 1 and evaluacion <= 5:
            clients.append(evaluacion)  # Guardar la evaluación si es válida
            break
        else:
            print("Por favor, ingrese un número entre 1 y 5.")

# Tabulación de respuestas
excelente = 0
muy_buena = 0
buena = 0
regular = 0
malo = 0

# Contamos las respuestas
for evaluacion in clients:
    if evaluacion == 5:
        excelente += 1
    elif evaluacion == 4:
        muy_buena += 1
    elif evaluacion == 3:
        buena += 1
    elif evaluacion == 2:
        regular += 1
    elif evaluacion == 1:
        malo += 1

# Mostrar la cantidad de respuestas por categoría
print("Respuestas:")
print("Excelente:", excelente)
print("Muy Buena:", muy_buena)
print("Buena:", buena)
print("Regular:", regular)
print("Malo:", malo)

# b) Evaluación más frecuente
# Encontramos la evaluación más frecuente con un bucle simple
max_respuesta = excelente
evaluacion_mas_frecuente = 5  # Inicialmente asumimos que la más frecuente es Excelente

if muy_buena > max_respuesta:
    max_respuesta = muy_buena
    evaluacion_mas_frecuente = 4
if buena > max_respuesta:
    max_respuesta = buena
    evaluacion_mas_frecuente = 3
if regular > max_respuesta:
    max_respuesta = regular
    evaluacion_mas_frecuente = 2
if malo > max_respuesta:
    max_respuesta = malo
    evaluacion_mas_frecuente = 1

# Mostrar la evaluación más frecuente
if evaluacion_mas_frecuente == 5:
    print("La evaluación más frecuente es: Excelente")
elif evaluacion_mas_frecuente == 4:
    print("La evaluación más frecuente es: Muy Buena")
elif evaluacion_mas_frecuente == 3:
    print("La evaluación más frecuente es: Buena")
elif evaluacion_mas_frecuente == 2:
    print("La evaluación más frecuente es: Regular")
else:
    print("La evaluación más frecuente es: Malo")

# c) Promedio de las evaluaciones
# Calculamos el promedio sin usar sum()
total = 0
for evaluacion in clients:
    total += evaluacion
promedio = total / len(clients)

# Mostrar el promedio
print("Promedio:", round(promedio, 2))

# d) Porcentaje de respuestas por debajo del promedio
# Calculamos el porcentaje de respuestas menores que el promedio
menor_promedio = 0
for evaluacion in clients:
    if evaluacion < promedio:
        menor_promedio += 1

porcentaje_bajo_promedio = (menor_promedio / len(clients)) * 100

# Mostrar el porcentaje
print("Porcentaje menor al promedio:", round(porcentaje_bajo_promedio, 2), "%")




