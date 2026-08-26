def normalizar_nombre(nombre):
    return nombre.title()


def generar_sigla(nombre_equipo):
    palabras = nombre_equipo.split()
    sigla = ""

    for palabra in palabras:
        sigla += palabra[0].upper()

    return sigla


def contiene_digitos(texto):
    for caracter in texto:
        if caracter.isdigit():
            return True

    return False