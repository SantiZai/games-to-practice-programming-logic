import random

palabras = ("PROGRAMACION", "AHORCADO", "PYTHON")

def generar_diccionario(palabra):
    diccionario = {}
    for letra in palabra:
        if letra not in diccionario.keys():
            diccionario[letra] = 1
        else:
            diccionario[letra] += 1
    return diccionario

def cantidad_veces(palabra, letra):
    contador = 0
    for let in palabra:
        if let == letra:
            contador += 1
    return contador

def generar_tablero(palabra, acertadas):
    tablero = []
    for i in range(len(palabra)):
        if palabra[i] not in acertadas:
            tablero.append("_")
        else:
            tablero.append(palabra[i])
    return tablero

def generar_palabra_aleatoria():
    return palabras[random.randint(0, len(palabras) - 1)]

def jugar():
    palabra = generar_palabra_aleatoria()
    intentos_fallidos = 0
    letras_acertadas = []
    letras = generar_diccionario(palabra)

    while intentos_fallidos < 7 and len(letras_acertadas) < len(palabra):
        print(generar_tablero(palabra, letras_acertadas))
        letra = input("Escribe la letra: ").upper()
        if letra in letras.keys() and letras[letra] > 0:
            letras[letra] = 0
            contador = 0
            while contador < cantidad_veces(palabra, letra):
                letras_acertadas.append(letra)
                contador += 1
            print(f"Letra acertada. {letras_acertadas}")
        elif letra not in letras.keys():
            intentos_fallidos += 1
            print(f"Letra incorrecta. Te quedan {7 - intentos_fallidos} intentos.")

    if len(palabra) == len(letras_acertadas):
        print(f"Felicidades, ganaste! La palabra era {palabra}")
    else:
        print(f"Perdiste, la palabra era {palabra}")
