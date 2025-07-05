archivo = open("datos.txt", "w")
archivo.write("Hola, mundo!")
archivo.close()

archivo = open("datos.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()