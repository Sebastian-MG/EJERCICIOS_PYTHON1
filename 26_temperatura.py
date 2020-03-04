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


