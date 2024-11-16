import random

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generar_primo(rango_inferior, rango_superior):
    primos = []
    for i in range(rango_inferior, rango_superior + 1):
        if es_primo(i):
            primos.append(i)
    if not primos:
        return None
    return random.choice(primos)