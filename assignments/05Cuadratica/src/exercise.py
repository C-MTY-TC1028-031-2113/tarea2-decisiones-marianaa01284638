import cmath

def main():
    # Escribe tu código abajo de esta línea
    a = int(input("Da el valor de a: "))
    b = int(input("Da el valor de b: "))
    c = int(input("Da el valor de c: "))

    valor1 = (-c / b)
    dis = ((b**2) - (4 * a * c))
    x1 = (- b + cmath.sqrt ((b**2) - (4 * a * c))) / (2 * a)
    x2 = (- b - cmath.sqrt ((b**2) - (4 * a * c))) / (2 * a)
    x0 = (- b / (2 * a))
    if a == 0 and b == 0:
        print('no tiene solucion')
    elif a == 0 and b != 0:
        print(valor1)
    elif dis < 0:
        print('Raices Completas')
    elif dis > 0:
        print(x1)
        print(x2)
    elif dis == 0:
        print(x0)
    pass

if __name__ == '__main__':
    main()
