#Ejercicio7. Realizar un programa que pida 3 números y los muestre en orden ascendente.

print("Pon 3 números y el programa los ordenará de manera ascendente.")

num1= float(input("Pon un número."))
num2= float(input("Pon otro número."))
num3=float(input("Pon un último número."))



if (num1 < num2 < num3) : print("Sus números ya están ordenados.")
if (num1 > num2 > num3) : print(num3,num2,num1)
if (num3 < num1 < num2) : print(num3,num1,num2)
if (num1 < num2 > num3) : print(num1,num3,num2)
if (num1 > num2 < num3) : print(num2,num3,num1)

