##EJERCICIO 1
#for i in range(1, 11):
    #if i % 2 ==1:
     #   print(i)
    
    
##EJERCICIO 2
#x = 1
#while x < 11:
 #   if x % 2 ==1:
  #      print(x)
   # x +=1
   
   
##ESCENARIO 1
# while True:
#     palabra = str(input("Ingrese una palabra:"))
#     if palabra == "chupacabra":
#         print( "¡Has dejado el bucle con éxito!")
#         break

##ESCENARIO 2
user_word = input("Ingrese una palabra: ")
user_word = user_word.upper()  

for letra in user_word:
    if letra in "AEIOU":  
        continue  
    print(letra)  
