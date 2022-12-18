#Ejercicio10. Realizar un programa que pida dos números enteros y muestre en pantalla si el número mayor es múltiplo del número menor.

print("Averigue si en dos números, uno es múltiplo del otro. Recuerde poner el número mayor primero.")

num1=int(input("Inserte un número: "))
num2=int(input("Inserte otro número: "))

if num1%num2 == 0:
    print("El segundo número insertado es múltiplo del primero.")
else:
    print("El segundo número insertado no es múltiplo del primero.")
