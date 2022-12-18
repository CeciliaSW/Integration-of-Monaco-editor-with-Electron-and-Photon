#Ejercicio9. Escribir un programa que pida al usuario un valor en centímetros, deberá mostrar su correspondiente valor en kilómetros, metros y centímetros.

print("Convertidor de cantidades mayores o iguales a un kilómetro en cm a km y m.")
valor=int(input("Pon un valor en cm mayor o igual a un km y será convertido a kilómetros y metros: "))

cantidad1 = valor/100
cantidad2 = valor/1000
cantidad3 = valor

if valor <1000:
    print ("No se pueden convertir cantidades menores a un kilómetro.")
else:
    print ("Equivale a: " ,cantidad1, "metros.")
    print ("Equivale a: " ,cantidad2, "kilómetros.")
    print ("Tu valor inicial era: " ,cantidad3, "centímetros.")
       
