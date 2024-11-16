def numscan():
    inn = input('Ingrese un número entero positivo (En caso de escoger un numero no entero, este se aproximara al entero mas bajo): ')
    try:
        num = int(inn)
        if num < 0:
            num = abs(num)  
        return num
    except ValueError:
        print('El número ingresado no es un entero positivo.')
        return numscan()
    