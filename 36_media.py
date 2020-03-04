# 36 Escribir un programa que calcule la media de x cantidad números introducidos por el
# teclado.


numeros = (input(" Digite los numeros por separados por comas  \n"))
lista = (numeros.split(","))  # split separa los valores ingresados por comas
lista_entero = list(map(int, lista))  # map permite convertir lista de string a entero
suma = 0
i = 0
for i in range(0, len(lista_entero)):  # len recorre la lista
    suma = suma + lista_entero[i]  # suma todos los elementos de la lista
    i = i + 1
media = suma / i
print("Promedio " + str(media))