try:
    with open("archivo_inexistente.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("El archivo no se encuentra.")
