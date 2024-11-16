def numscan():
    try:
        num = int(input('Ingrese un número entero positivo: (En caso de escoger un numero no entero, este se aproximara al entero mas bajo)'))
        if num < 0:
            raise ValueError
        return num
    except ValueError:
        print('El número ingresado no es un entero positivo.')
        return numscan()
    