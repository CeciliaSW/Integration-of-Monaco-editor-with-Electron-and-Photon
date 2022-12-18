#Ejercicio16. Crear un programa que pida una calificación de 0 a 100, y que muestre en pantalla un mensaje dependiendo de la calificación.
#De 0 a 59 "Reprobaste."
#De 60 a 89 "Pasaste."
#De 90 a 100 "Obtuviste una calificación sobresaliente."


print("Escribe una calificación y recibe un mensaje sobre ella.")

calificación=int(input("Pon un número de 0 a 100: "))
   
   
if (calificación == 0) or (calificación <= 59):
    print("Reprobaste.")
    
elif (calificación == 60) or (calificación <= 89):
    print("Pasaste.")
elif (calificación == 90) or (calificación <= 100):
    print("Obtuviste una calificación sobresaliente.")
else:
    print("No se puede ponderar un número mayor a 100. Esa calificación no es posible.")
