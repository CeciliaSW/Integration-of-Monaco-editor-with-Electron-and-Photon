#Ejercicio14. Realizar un programa que pida un número al usuario que corresponda al día de la semana.
#Deberá mostrar su equivalente en letra.

print("Ponga un día de la semana y sepa su equivalente en letra.")
print("El número que puede poner es de un rango de (1) a (7).")

num=int(input("Ponga el número correspondiente a un día de la semana: "))

if num==1:
    print("(1) equivale a Lunes.")

if num==2:
    print("(2) equivale a Martes.")

if num==3:
    print("(3) equivale a Miércoles.")

if num==4:
    print("(4) equivale a Jueves.")

if num==5:
    print("(5) equivale a Viernes.")

if num==6:
    print("(6) equivale a Sábado.")

if num==7:
    print("(7) equivale a Domingo.") 
