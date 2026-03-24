#1

##   x = int(input("Enter number:"))
  #  print(10/4)
#except:
#    print("An error ocurred.")
#finally:
#    print("The 'try except' is finished.")
    
#2. tipos de errores en phyton
# Erroresn de sintaxis (Syntax Error)
# Errores logicos (LogicalError)
# Errores en tiempo de ejecucion (RuntimeError)

#Leer enteros separados por comas, calcular el promedio y manejar errores de conversion corrige ademas 
# corrige ademas el calculo logico del promedio    

# Leer enteros separados por comas, calcular el promedio 
# y manejar errores de conversión + corregir el cálculo lógico del promedio

try:
    numeros = input('Ingresa numeros separados por comas:')
    lista = [int(x.strip()) for x in numeros.split(',') if x.strip()!= '']
    
    if len(lista) == 0:
        raise ValueError('No ingresaste numeros validos.')
    else:
        promedio = sum(list) / len(lista)
        print('promedio es:', promedio)
        
except ValueError as e:
    print('Error', e)



 



