#Ejercicio6. Realiza un programa que pida 2 números enteros y diga si el segundo es divisior del primero.

print("Averigue si un número es un divisor.")

dividendo=int(input("Inserte un dividendo:"))
divisor=int(input("Inserte un segundo número:"))

residuo= dividendo % divisor

if (residuo == 0) : print("El segundo número insertado es un divisor.")
if (residuo > 0) : print("El segundo número insertado no es un divisor.")    
