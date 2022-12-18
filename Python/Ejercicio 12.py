#Ejercicio12. Realizar un programa que pida dos números, si son iguales multiplicarlos.
#Si el primero es mayor que el segundo se deben restar.
#Si el primero es menor que el segundo que se sumen.

print("Multiplque, reste o sume dos números según sea el caso.")

num1=int(input("Ingresa un número: "))
num2=int(input("Ingresa otro número: "))

if(num1==num2):
 multiplicación = num1*num2
 print("Los números se multiplicarón y dieron como resultado: ",multiplicación)
else:
 if(num1>num2):
  resta = num1-num2
  print("Los números se restaron y dieron como resultado: ", resta)
 else:
  suma = num1+num2
  print("Los números se sumaron y dieron como resultado: ", suma)
