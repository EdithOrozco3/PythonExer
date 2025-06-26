def saludo():
    print("¡Hola, mundo!")


saludo()  # Imprime "¡Hola, mundo!"

## Función con un parámetro
def saludo(nombre):
    print(f"¡Hola, {nombre}!")

saludo("Juan")  # Imprime "¡Hola, Juan!"
saludo("Edith")  # Imprime "¡Hola, Edith!"

## Función con varios parámetros
def saludo(nombre, edad):
    print(f"¡Hola, {nombre}! Tienes {edad} años.")

saludo("Juan", 30)  # Imprime "¡Hola, Juan! Tienes 30 años."

## Función con un parámetro por defecto
def saludo(nombre="mundo"):
    print(f"¡Hola, {nombre}!")

saludo()  # Imprime "¡Hola, mundo!"

## Función con un parámetro por defecto y otro obligatorio
def saludo(nombre, edad=18):   
    print(f"¡Hola, {nombre}! Tienes {edad} años.")

saludo("Ana")  # Imprime "¡Hola, Ana! Tienes 18 años."

## Función con un número variable de argumentos
def saludo(*nombres):
    for nombre in nombres:
        print(f"¡Hola, {nombre}!")  

saludo("Juan", "Ana", "Pedro")

## Función con un número variable de argumentos y un parámetro por defecto
def saludo(edad=18, *nombres):
    for nombre in nombres:
        print(f"¡Hola, {nombre}! Tienes {edad} años.")

saludo(25, "Juan", "Ana")  # Imprime "¡Hola, Juan! Tienes 25 años." y "¡Hola, Ana! Tienes 25 años."

