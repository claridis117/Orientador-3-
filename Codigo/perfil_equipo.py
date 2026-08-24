
def contiene_digitos(texto):
    val= False
    for caracter in texto:
        if caracter.isdigit():
            val = True
            
    return val

def normalizar_nombre(nombre):
    return nombre.title()

def generar_sigla(texto):
    palabras= texto.split()
    sigla= ""
    for palabra in palabras:
        sigla += palabra[0].upper()
    
    return sigla


def main():
    print("== Registro del equipo ==")
    
    nombre_equipo= input("Ingrese el nombre del equipo: ")
    
main()