# Ejercicio 7

lista = []

while True:
    nombre = input("Introduzca un nombre: ")
    if nombre == "fin":
        break
    telefono = input("Introduzca un telefono: ")

    linea = {}
    linea["Nombre"] = nombre
    linea["Telefono"] = telefono

    lista.append(linea)

for linea in lista:
    print(linea)