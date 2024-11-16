def inverso_modular(a, m):
    t, nuevo_t = 0, 1
    r, nuevo_r = m, a

    while nuevo_r != 0:
        cociente = r // nuevo_r
        t, nuevo_t = nuevo_t, t - cociente * nuevo_t
        r, nuevo_r = nuevo_r, r - cociente * nuevo_r

    if r > 1:
        return None
    if t < 0:
        t += m
    return t
