#Ejercicio4. Realizar un programa que pregunte al usuario que área de figura desea.
#Círculo, cuadrado, o triángulo.

print("¿Qué área de figura desea? Puede preguntar por círculo (1), cuadrado (2), o triángulo (3).")


figura=int(input("Ponga el número correspondiente a la figura de la cual quiera obtener la fórmula del área:"))


if (figura == 1) : print("La fórmula del área es: 3.1416*(r**2).")

if (figura == 2) : print("La fórmula del área es: L*L.")

if (figura == 3) : print("La fórmula del área es: b*h/2.")

   
print("Una vez sabida la fórmula de su figura ponga el código de esta para calcular alguna área.")
print("La fórmula del círculo se clasifica como (4), del cuadrado (5), y del triángulo (6).")


fórmula=int(input("Ponga el código de fórmula:"))


if fórmula == 4:
    print("Pon el radio del círculo para saber su área.")
    r=float(input("Ingrese el valor del radio:"))
    ACIRC= 3.1416*(r**2)
    print("El área es: ",ACIRC)


if fórmula == 5:
    print("Pon la medida de un lado del cuadrado para saber su área.")
    L=float(input("Ingrese el valor de un lado:"))
    ACUA= L*L
    print("El área es: ",ACUA)


if fórmula == 6:
    print("Pon las siguientes medidas del triángulo para saber su área.")
    b=float(input("Ingrese el valor de la base:"))
    h=float(input("Ingrese el valor de la altura:"))
    ATRI= b*h/2
    print("El área es: ",ATRI)
