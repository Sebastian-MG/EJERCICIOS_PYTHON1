import math


def distancia(x1, y1, x2, y2):
    x = pow(x2 - x1, 2)
    y = pow(y2 - y1, 2)
    d = x + y
    d = math.sqrt(d)
    return d

def main():
    x1 = int(input("coprdenada X1: "))
    y1 = int(input("Coordenada Y1: "))
    x2 = int(input("Coordenada X2: "))
    y2 = int(input("Coordenada Y2: "))
    s = distancia(x1, y1, x2, y2)
    print("la distancia entre los dos puntos es: {}".format(s))

if __name__ == "__main__":
    main()
