# 45 Escribir un programa que tras asignar números enteros a una lista, determine la posición de
# la lista en la que se encuentra el máximo valor.

lista=[6,4,23,6,3,4]
maximo =max(lista)
posicion =lista.index(max(lista))
print("Numero maximo",maximo)
print("Posicion: ",posicion+1)
