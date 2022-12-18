#Ejercicio5. Realizar un programa que pida 3 números y muestre si todos son iguales, 2 de ellos lo son, o los 3 son diferentes.

print("Averigue si 3 números son iguales o no.")


num1=float(input("Ponga un número:"))
num2=float(input("Ponga otro número:"))
num3=float(input("Ponga un último número más:"))


if (num1 == num2 == num3) : print("Todos los números son iguales.")

if (num1 < num2 < num3) : print("Todos los números son diferentes.")
if (num1 > num2 > num3) : print("Todos los números son diferentes.")
if (num3 < num1 < num2) : print("Todos los números son diferentes.")
if (num1 < num2 > num3) : print("Todos los números son diferentes.")
if (num1 > num2 < num3) : print("Todos los números son diferentes.")

if (num1 < num2 == num3) : print("Únicamente 2 números son iguales.")
if (num1 > num2 == num3) : print("Únicamente 2 números son iguales.")
if (num1 == num2 < num3) : print("Únicamente 2 números son iguales.")
if (num1 == num2 > num3) : print("Únicamente 2 números son iguales.")
if (num1 == num3 < num2) : print("Únicamente 2 números son iguales.")
if (num1 == num3 > num2) : print("Únicamente 2 números son iguales.")

   
