# Abre el archivo en modo lectura
with open('archivo.txt', 'r') as file:
    # Lee y muestra cada línea del archivo
    for line in file:
        print(line.strip())
