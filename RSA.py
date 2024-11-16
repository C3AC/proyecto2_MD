def encriptar(caracter, pubkey):
    e, n = pubkey
    mensaje = ord(caracter)
    encriptado = pow(mensaje, e, n)
    return encriptado

def desencriptar(encriptado, privkey):
    d, n = privkey
    desencriptado = pow(encriptado, d, n)
    return chr(desencriptado)

