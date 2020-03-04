# 45. Escribir un programa que sume, independientemente, los elementos positivos y negativos de
# la una matriz de 5x5, la matriz se debe llenar solicitando los datos al usuario.

fila = 5
columna = 5
sum_positivos = 0
sum_negativos = 0
matriz = []
numero = 0

for a in range(fila):
    matriz.append([0]*columna)

for i in range(fila):
    for j in range(columna):
        numero = int(input(f"Numero posicion en la matriz [{i}] [{j}]: "))
        matriz[i][j] = numero
        if numero >= 0:
            sum_positivos = sum_positivos + numero
        else:
            sum_negativos = sum_negativos + numero

print(f"Suma de los positivos  {sum_positivos}")
print(f"Suma de los negativos {sum_negativos}")