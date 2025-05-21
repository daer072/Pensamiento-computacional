matriz = [
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
]

print("Matriz original:")
for fila in matriz:
    print(fila)

generacion = 1

while generacion <= 2:
    nueva_matriz = []
    
    for numero_fila in range(len(matriz)):
        nueva_fila = []
        
        for numero_columna in range(len(matriz[0])):
            vecinos = 0

            #  vecinosizquierda
            if numero_columna - 1 >= 0:
                if matriz[numero_fila][numero_columna - 1] == 1:
                    vecinos += 1

            # vecinosderecha
            if numero_columna + 1 < len(matriz[0]):
                if matriz[numero_fila][numero_columna + 1] == 1:
                    vecinos += 1

            # reglas  
            if matriz[numero_fila][numero_columna] == 1:
                # Célula viva
                if vecinos == 1 or vecinos == 2:
                    nueva_fila.append(1)  
                else:
                    nueva_fila.append(0)  
            else:
                
                if vecinos == 1:
                    nueva_fila.append(1)  
                else:
                    nueva_fila.append(0)  
        
        nueva_matriz.append(nueva_fila)


    matriz = nueva_matriz


    print("\nGeneración " + str(generacion) + ":")
    for fila in matriz:
        print(fila)

    generacion += 1
