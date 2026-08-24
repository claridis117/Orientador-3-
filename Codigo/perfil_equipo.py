
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
    comision = input("Ingrese la comision: ")
    cant_integrantes= int(input("Cuantos integrantes son?: "))
    
    nombres_integrantes= []
    roles_integrantes= []
    
    for i in range(cant_integrantes):
        print(f"\n=== Integrante {i + 1}===")
        nombre= input("Nombre: ")
        rol= input("Rol en el equipo: ")
        
        nombres_integrantes.append(normalizar_nombre(nombre))
        roles_integrantes.append(rol)
        
main()