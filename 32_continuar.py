# 32  Escribir un programa que realice la pregunta ¿Desea continuar S/N? y que no deje de
# hacerla hasta que el usuario teclee N.


terminar = False
while not terminar:
    pregunta = input("¿Desea continuar S/N?")
    if pregunta == "S":
        terminar = False
    elif pregunta == "N":
        terminar = True

