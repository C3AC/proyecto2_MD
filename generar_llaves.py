from maxcomden import mcd
from inverso_modular import inverso_modular
from generar_primo import generar_primo

def generar_llaves(rango_inferior, rango_superior):
    p = generar_primo(rango_inferior, rango_superior)
    q = generar_primo(rango_inferior, rango_superior)
    n = p * q
    tot_n = (p - 1) * (q - 1)
    e = generar_primo(rango_inferior, rango_superior)
    while True:
        if mcd(e, tot_n) == 1:
            break
        e = generar_primo(rango_inferior, rango_superior)
    d = inverso_modular(e, tot_n)
    return (e,n), (d, n)