
def saludo_usuario():
    nombre = input("Ingrese su nombre")
    return f"Hola {nombre}!, es un placer saludarte"

print(saludo_usuario())




#%%
numero = int(input("Ingrese un número: "))

for i in range(1, numero + 1):
  # Mostrar cada número en la consola
  print(i)



def calcular(operacion):
    numero1 = int(input("Ingrese el primer numero: "))
    numero2 = int(input("Ingrese el segundo numero: "))

    if operacion == '+':
        resultado = numero1 + numero2
    elif operacion == '-':
        resultado = numero1 - numero2
    elif operacion == '*':
        resultado = numero1 * numero2
    elif operacion == '/':
        resultado = numero1 / numero2
    else:
        resultado = "Operación no válida"

    return resultado

operacion_elegida = input("Ingrese la operación que desea realizar (+, -, *, /): ")

resultado = calcular(operacion_elegida)
print("El resultado de la operación es:", resultado)

