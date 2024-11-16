from generar_llaves import generar_llaves
from RSA import encriptar, desencriptar

def main():
    # Solicitar rango inferior y superior
    rango_inferior = int(input("Ingrese el rango inferior: "))
    rango_superior = int(input("Ingrese el rango superior: ")) 
    # Generar llaves pública y privada
    pubkey, privkey = generar_llaves(rango_inferior, rango_superior)

    # Mensaje a encriptar
    mensaje = input("Ingrese el mensaje a encriptar: ")
    print(f"Mensaje original: {mensaje}")

    # Encriptar mensaje
    mensaje_encriptado = [encriptar(caracter, pubkey) for caracter in mensaje]
    print(f"Mensaje encriptado: {mensaje_encriptado}")

    # Desencriptar mensaje
    mensaje_desencriptado = ''.join([desencriptar(caracter, privkey) for caracter in mensaje_encriptado])
    print(f"Mensaje desencriptado: {mensaje_desencriptado}")

if __name__ == "__main__":
    main()