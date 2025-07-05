nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))


print("Hola, " + nombre + "!")
print("Tienes " + str(edad) + " años.")

print(f"Hola, mi nombre es {nombre} y tengo {str(edad)} años.")

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")