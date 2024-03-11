def saludo_usuario():
    nombre = input("Ingrese su nombre")
    return f"Hola {nombre}!, es un placer saludarte"

print(saludo_usuario())




#%%
numero = int(input("Ingrese un número: "))

for i in range(1, numero + 1):
  # Mostrar cada número en la consola
  print(i)
