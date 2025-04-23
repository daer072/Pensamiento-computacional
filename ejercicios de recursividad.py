#EJERCICIO 1
# n = int(input("Ingrese su numero: "))

# def es_par_o_impar(n):
#     if n % 2 == 0:
#         print("Su numero es par")
#     else: 
#         print("Su numero es impar")

# #llamado a la funcion
# es_par_o_impar(n)

#EJERCICIO 2

# def suma_lista(lista):
#     if not lista:
#         return 0
#     return lista[0] + suma_lista(lista[1:])

# numeros = [2, 4, 6, 8, 10]
# print(suma_lista(numeros))  


#EJERCICIO 3    
# n = int(input("Ingrese su numero: "))

# def  cuenta_regresiva(n):
#     if n < 0:
#         print("Depegar!")
#     else:
#         print (n)
#         cuenta_regresiva (n-1)
            
            
# cuenta_regresiva(n)

#EJERCICIO 4
# n = int(input("Ingrese su número: "))

# def cuenta_ascendente(n):
#     for i in range(0, n + 1):  
#         print(i)

# cuenta_ascendente(n)

#EJERCICIO 5
# n = int(input("Ingrese su número: "))

# def suma_hasta(n):
#     suma = 0
#     for i in range(1, n + 1):
#         suma += i  # Acumular la suma de los números
#     print(suma)

# suma_hasta(n)


#EJERCICIO 6
# n = int(input("Ingrese su número: "))

# def factorial(n):
#     mult = 1  # Inicializamos en 1 para evitar el problema con el 0
#     for i in range(1, n + 1):
#         mult *= i  # Multiplicamos cada número sucesivo
#     print(mult)

# factorial(n)


#EJERCICIO 7
def minimo(lista):
    if len(lista) == 1:
        return lista[0]
    
    return min(lista[0], minimo(lista[1:]))

print(minimo([5, 3, 8, 1, 2]))  

    

    
