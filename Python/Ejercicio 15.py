#Ejercicio15. Realizar un programa que muestre en pantalla el valor absoluto de un número si este es múltiplo de 3 o 7.

print("Descubre el valor absoluto de un múltiplo de 3 o 7.")

num=int(input("Pon un número: "))
absoluto= abs(num)

if num%3 == 0:
    print("El número es múltiplo de 3.")
    print("Su valor absoluto es: ",absoluto)
elif num%7 == 0:
    print("El número es múltiplo de 7.")
    print("Su valor absoluto es: ",absoluto)
else:
    print("El número no es múltiplo de 3 ni de 7. No se puede sacar su valor absoluto.")
