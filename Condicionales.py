# 21. Escribir un programa que dado un número del 1 a 7 escriba el correspondiente nombre del
# día de la semana.

dia = int(input("Digite el numero del 1 al 7:\n"))
if dia == 1:
    print("Lunes")
elif dia == 2:
    print("Martes")
elif dia == 3:
    print("Miercoles")
elif dia == 4:
    print("Jueves")
elif dia == 5:
    print("Viernes")
elif dia == 6:
    print("Sabado")
elif dia == 7:
    print("Domingo")

# 26. Escribir un programa que calcula el equivalente en grados Fahrenheit o Celsius de una
# temperatura t, el usuario debe indicar si la temperatura que ingreso esta en celcius o
# fahrenheit acompañando el valor por el carácter c o t respectivamente.
# Celsius / 5 = (Fahrenheit – 32) 9.

temp = int(input("Temperatura \n"))
medida = str(input("Celsius: C , Farenheit: F \n"))

if medida == "C":
    conversion = (temp * 1.8) + 32
    print(str(temp) + str(medida) + " es igual a " + str(conversion) + "F")
elif medida == "F":
    conversion = (temp - 32) / 1.8
    print(str(temp) + str(medida) + " es igual a " + str(conversion) + "C")


