#Ejercicio13. Realizar un programa que pida al usuario un día y un mes.
#El programa debe mostrar el signo zodiacal.

print("Ponga la fecha de su cumpleaños para saber que signo es.")

dia=int(input("Ponga el número del día en que nació: "))
mes=int(input("Ponga el número del mes en que nació: "))

if (mes==3) and (dia>=21) or (mes==4) and (dia<=20):
 print("Su signo es Aries.")

if (mes==4) and (dia>=21) or (mes==5) and (dia<=21):
  print("Su signo es Tauro.")

if (mes==5) and (dia>=22) or (mes==6) and (dia<=21):
  print("Su signo es Geminis.")

if (mes==6) and (dia>=22) or (mes==7) and (dia<=22):
  print("Su signo es Cáncer.")

if (mes==7) and (dia>=23) or (mes==8) and (dia<=22):
  print("Su signo es Leo.")

if (mes==8) and (dia>=23) or (mes==9) and (dia<=22):
  print("Su signo es Virgo.")

if (mes==9) and (dia>=23) or (mes==10) and (dia<=22):
  print("Su signo es Libra.")

if (mes==10) and (dia>=23) or (mes==11) and (dia<=22):
  print("Su signo es Escorpio.")

if (mes==11) and (dia>=23) or (mes==12) and (dia<=21):
  print("Su signo es Sagitario.")

if (mes==12) and (dia>=22) or (mes==1) and (dia<=20):
  print("Su signo es Capricornio.")

if (mes==1) and (dia>=21) or (mes==2) and (dia<=19):
  print("Su signo es Acuario.")

if (mes==2) and (dia>=20) or (mes==3) and (dia<=20):
  print("Su signo es Piscis.")
