#Ejercicio8. Realiza un programa que pida un año al usuario entre 1900 y 2019, y comprueba si el año es bisiesto.

print("Identificador de años bisiestos")

fecha=int(input("Escriba un año entre 1900 y 2019: "))

while (fecha <1900 or fecha >2019):
      fecha= int(input("Este año no está dentro del rango impuesto. Intente con otro:"))

if fecha%400==0 or fecha%100!=0 and fecha%4==0:
   print("El año ", fecha, " es un año bisiesto")
else:
    print("El año ", fecha, " no es un año bisiesto")
