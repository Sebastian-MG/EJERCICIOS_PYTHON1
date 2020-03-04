#75. Escribir un programa que calcule la potencia de un numero usando recursividad.


def potencia(b,n):
    if n <= 0:
        return 1
    if n % 2 == 0:
        pot = potencia(b, n/2)
        return pot * pot
    else:
        pot = potencia(b, (n-1)/2)
        return pot * pot * b

# b^n = b^(n/2) × b^(n/2) si n es par.
# b^n = b^(n−1)/2 × b^(n−1)/2 × b si n es impar
