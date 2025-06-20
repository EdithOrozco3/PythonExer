frutas = ["manzana", "banana", "naranja"]

print("Lista de frutas con bucle for:")
for fruta in frutas:
    print(fruta)

print("\nLista de frutas con bucle while:")
i = 0
while i < len(frutas):
    print(frutas[i])
    i += 1

print("\nLista de frutas con bucle for y range:")
for i in range(len(frutas)):
    print(frutas[i])    

print("\nLista de frutas con bucle for y enumerate:")
for i, fruta in enumerate(frutas):
    print(f"Índice {i}: {fruta}")   

print("\nLista de frutas con bucle for y zip:")
for i, fruta in zip(range(len(frutas)), frutas):
    print(f"Índice {i}: {fruta}")   

print("\nLista de frutas con bucle for y comprensión de listas:")
frutas_con_comprension = [fruta for fruta in frutas]    
print(frutas_con_comprension)

print("\nLista de frutas con bucle for y comprensión de listas con condición:")
frutas_con_condicion = [fruta for fruta in frutas if "a" in fruta]  
print(frutas_con_condicion)

print("\nLista de frutas con bucle for y comprensión de listas con transformación:")
frutas_transformadas = [fruta.upper() for fruta in frutas]  
print(frutas_transformadas)

print("\nLista de frutas con bucle for y comprensión de listas con condición y transformación:")
frutas_transformadas_condicion = [fruta.upper() for fruta in frutas if "a" in fruta]    
print(frutas_transformadas_condicion)

print("\nLista de frutas con bucle for y comprensión de listas con condición y transformación:")
frutas_transformadas_condicion = [fruta.lower() for fruta in frutas if "a" in fruta]
print(frutas_transformadas_condicion)

print("\nLista de frutas con bucle for y comprensión de listas con condición y transformación:")
frutas_transformadas_condicion = [fruta.capitalize() for fruta in frutas if "a" in fruta]
print(frutas_transformadas_condicion)

print("\nLista de frutas con bucle for y comprensión de listas con condición y transformación:")
frutas_transformadas_condicion = [fruta.title() for fruta in frutas if "a" in fruta]
print(frutas_transformadas_condicion)

print("\nLista de frutas con bucle for y comprensión de listas con condición y transformación:")
frutas_transformadas_condicion = [fruta[::-1] for fruta in frutas if "a" in fruta]
print(frutas_transformadas_condicion)

print("\nLista de frutas con bucle for y comprensión de listas con condición y transformación:")
frutas_transformadas_condicion = [fruta.replace("a", "@") for fruta in frutas if "a" in fruta]
print(frutas_transformadas_condicion)

print("\nLista de frutas con bucle for y comprensión de listas con condición y transformación:")
frutas_transformadas_condicion = [fruta.replace("a", "4") for fruta in frutas if "a" in fruta]
print(frutas_transformadas_condicion)

print("\nLista de frutas con bucle for y comprensión de listas con condición y transformación:")
frutas_transformadas_condicion = [fruta.replace("a", "4").upper() for fruta in frutas if "a" in fruta]
print(frutas_transformadas_condicion)

print("\nLista de frutas con bucle for y comprensión de listas con condición y transformación:")
frutas_transformadas_condicion = [fruta.replace("a", "4").lower() for fruta in frutas if "a" in fruta]
print(frutas_transformadas_condicion)

print("\nLista de frutas con bucle for y comprensión de listas con condición y transformación:")
frutas_transformadas_condicion = [fruta.replace("a", "4").capitalize() for fruta in frutas if "a" in fruta]
print(frutas_transformadas_condicion)

print("\nLista de frutas con bucle for y comprensión de listas con condición y transformación:")
frutas_transformadas_condicion = [fruta.replace("a", "4").title() for fruta in frutas if "a" in fruta]
print(frutas_transformadas_condicion)

print("\nLista de frutas con bucle for y comprensión de listas con condición y transformación:")
frutas_transformadas_condicion = [fruta.replace("a", "4")[::-1] for fruta in frutas if "a" in fruta]
print(frutas_transformadas_condicion)

print("\nLista de frutas con bucle for y comprensión de listas con condición y transformación:")
frutas_transformadas_condicion = [fruta.replace("a", "4").replace("e", "3") for fruta in frutas if "a" in fruta]
print(frutas_transformadas_condicion)

print("\nLista de frutas con bucle for y comprensión de listas con condición y transformación:")
frutas_transformadas_condicion = [fruta.replace("a", "4").replace("e", "3").upper() for fruta in frutas if "a" in fruta]
print(frutas_transformadas_condicion)
