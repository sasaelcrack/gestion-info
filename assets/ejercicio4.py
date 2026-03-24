# Ejercicio 4: 
#Analiza el siguiente “código existente” y realiza un -> refactor <-, tener en cuenta los 
#problemas que se plantean al final.

#Código original (difícil de mantener)

op = input("ingrese operacion ( suma, resta, multiplicacion, division)")
a = int(input("Ingrese primer numero"))
b = int(input("Ingrese segundo numero"))

def calc(a, b, op):
    
    ops = {
        "s": lambda x,y: x + y,
        "r": lambda x,y: x - y,
        "m": lambda x,y: x * y,
        "d": lambda x,y: "Error" if y == 0 else x/y
    }
    func = ops.get(op)
    return func (a, b) if func else None

result = calc(a, b, op)
print("El resultado de", op, "Es:" , result)
   

   
   
    #if op == "s":
     #    return a + b
     #elif op == "r":
     #    return a - b
     #elif op == "m":
      #   return a * b
     #elif op == "d":
      #  if b == 0:
       #      return "error"
        # return a / b
     #else:
      #   return None

#Problemas:
#• Retorna "error" (string) o números → mezcla de tipos (confuso)
#• op con letras “mágicas”
#• No deja claro qué errores existen
#• Difícil testear los errores bien