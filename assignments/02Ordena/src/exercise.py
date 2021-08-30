def main():
    # Escribe el código adecuado para completar el programa
    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    z = int(input("Ingresa el tercer número: "))
    
    menor = min(x, y, z)
    mayor = max(x, y, z)
    enmedio = (x + y + z) - menor - mayor

    print(menor)
    print(enmedio)
    print(mayor)


if __name__=='__main__':
    main()
