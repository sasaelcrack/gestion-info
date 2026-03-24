# Ejercicio 2: 
#Abrir un archivo, capturar errores de apertura, contar líneas en else, cerrar en finally y mostrar un mensaje final.

filepath = input("datos.txt: ")
file = None
try:
    file = open(filepath, "r")
    line_count = 0
    for line in file:
        line_count += 1
except FileNotFoundError:
    print(f"Error: el archivo '{filepath}' no existe.")
else:
    print(f"Total de líneas: {line_count}")
    print("Archivo leído correctamente.")
finally:
    if file:
        file.close()
    print("Operación finalizada.")