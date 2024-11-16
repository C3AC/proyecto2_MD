from generar_llaves import generar_llaves
from RSA import encriptar, desencriptar
from positivoyentero import numscan

def main():
   
    rango_inferior = numscan()
    rango_superior = numscan()
    try: 
        pubkey, privkey = generar_llaves(rango_inferior, rango_superior)
    except RecursionError:
        print("Error: El intervalo de generación de primos no permite asegurar unicidad para los valores encriptados, se usara el intervalo por defecto [2, 1000]")
        pubkey, privkey = generar_llaves(2, 1000) 


    mensaje = input("Ingrese el mensaje a encriptar: ")
    print(f"Mensaje original: {mensaje}")


    mensaje_encriptado = [encriptar(caracter, pubkey) for caracter in mensaje]
    print(f"Mensaje encriptado: {mensaje_encriptado}")


    mensaje_desencriptado = ''.join([desencriptar(caracter, privkey) for caracter in mensaje_encriptado])
    print(f"Mensaje desencriptado: {mensaje_desencriptado}")

if __name__ == "__main__":
    main()