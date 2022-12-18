#Ejercicio11. Realice un programa que pida un número al usuario e indique si es un  número positivo, negativo o cero.

print("Averigua si un número es positivo, negativo; o igual a cero.")

num=int(input("Ingresa un número: "))

if(num==0):
 print("El número es cero.")
else:
 if(num>0):
  print("El número es positivo.")
 else:
  print("El número es negativo.")
