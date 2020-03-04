# Decir si una frase es o no un palíndromo, es decir, si se lee igual de derecha a a izquierda
# que de izquierda a derecha.

palabra = input("Digite  una frase: ")
p_reves = palabra[::-1]      # sting invertido
if palabra == p_reves:
    print("La palabra  es un palindromo")
else:
    print("La palabra no es un palindromo")
