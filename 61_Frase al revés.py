# 61. Escribir un programa que lea una frase introducida desde el teclado y la escriba al revés.

palabra = input("Ingresar palabra: ")
palabra.split()                # se separan las posiciones
p_reves = ''.join(reversed(palabra))    # invertir posiciones
print(p_reves)
