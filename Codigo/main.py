import perfil_equipo



#PUNTO 7
producto = input("Producto: ")
precio = float(input("Precio unitario: "))
cantidad = int(input("Cantidad: "))
total = precio * cantidad

# a) Usando f-string con formato de dos decimales
print(f"Producto: {producto} | Precio unitario: ${precio:.2f} | Cantidad: {cantidad} | Total: ${total:.2f}")

# b) Usando concatenación con str()
print("Producto: " + producto + " | Precio unitario: $" + str(precio) + 
      " | Cantidad: " + str(cantidad) + " | Total: $" + str(total))


#PUNTO 8


print("REGISTRO DEL EQUIPO")

nombre_equipo = input("Ingrese el nombre del equipo: ")
comision = input("Ingrese la comisión: ")
cantidad = int(input("Ingrese la cantidad de integrantes: "))

nombres = []
roles = []

for i in range(cantidad):
    print(f"Integrante {i + 1}")

    nombre = input("Nombre: ")
    rol = input("Rol inicial: ")

    nombres.append(perfil_equipo.normalizar_nombre(nombre))
    roles.append(rol.title())

print("PERFIL DEL EQUIPO")

print(f"Equipo: {nombre_equipo.upper()}")
print(f"Comisión: {comision}")
print(f"Cantidad de caracteres: {len(nombre_equipo)}")
print(f"Sigla: {perfil_equipo.generar_sigla(nombre_equipo)}")
print(f"¿Contiene un dígito?: {perfil_equipo.contiene_digitos(nombre_equipo)}")

print("\nIntegrantes:")

for i in range(cantidad):
    print(f"{i + 1}. {nombres[i]} - {roles[i]}")