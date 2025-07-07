import random
import datetime

from math import sqrt


resultado = sqrt(25)
print(resultado)  # Imprime 5.0

numero_aleatorio = random.randint(1, 20)
print("Numero aleatorio: " + str(numero_aleatorio))  # Imprime un número entero aleatorio entre 1 y 20

fecha_actual = datetime.datetime.now()
print("Fecha actual: " + str(fecha_actual.date()))  # Imprime la fecha y hora actual