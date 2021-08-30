def main():
    # Escribe tu código abajo de esta línea
    pass
    grados = int(input("Introduce los grados: "))
    if 0 < grados < 90:
        print('cuadrante 1')
    elif  grados == 180:
        print('eje')
    elif  grados == 270:
        print('eje')
    elif  grados == 360:
        print('eje')
    elif 90 < grados < 180:
        print('cuadrante 2')
    elif 180 < grados < 270:
        print('cuadrante 3')
    elif 270 < grados < 360:
        print('cuadrante 4')
    elif grados > 360:
        print('excede')
    elif grados < 0:
        print('excede')

if __name__ == '__main__':
    main()
