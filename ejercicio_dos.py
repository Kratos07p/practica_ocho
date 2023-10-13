# Solicitar al usuario que ingrese una serie de nombres
nombres = []
while True:
    nombre = input("Ingrese un nombre (o escriba 'fin' para terminar): ")
    if nombre == "fin":
        break
    nombres.append(nombre)

# Escribir los nombres en un archivo llamado "nombres.txt", uno por línea
with open("nombres.txt", "w") as archivo:
    for nombre in nombres:
        archivo.write(nombre + "\n")
