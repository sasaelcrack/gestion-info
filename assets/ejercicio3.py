# Ejercicio 3: 
#Crear un menú con: (1) dividir números, (2) abrir archivo y mostrar primera línea, (3) salir. 
#Captura ValueError, ZeroDivisionError, FileNotFoundError y usa un except
#Exception final para no previstos.

while True:
        print("\n=== Menú ===")
        print("1. Dividir números")
        print("2. Abrir archivo y ver primera línea")
        print("3. Salir")
 
        option = input("Elige una opción: ")
 
        try:
            if option == "1":
                a = float(input("Dividendo: "))
                b = float(input("Divisor: "))
                print(f"Resultado: {a / b}")
 
            elif option == "2":
                filepath = input("Ruta del archivo: ")
                file = open(filepath, "r")
                print(f"Primera línea: {file.readline()}")
                file.close()
 
            elif option == "3":
                print("Saliendo...")
                break
 
            else:
                raise ValueError(f"Opción inválida: '{option}'")
 
        except ValueError as e:
            print(f"Valor incorrecto: {e}")
        except ZeroDivisionError:
            print("Error: no se puede dividir entre cero.")
        except FileNotFoundError:
            print("Error: archivo no encontrado.")
        except Exception as e:
            print(f"Error inesperado: {e}")