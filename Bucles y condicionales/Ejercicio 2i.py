"""Que sume todos los números pares positivos, partiendo desde 0, 
hasta que la suma supere el valor de 1000. Posteriormente, 
debe mostrar en pantalla cuál es el valor de la suma y cuántos números se han sumado"""

# Importación de librerías:
from os import system

# Declaración de variables:

suma = 0
numero = 2
contador = 0

# Programa principal:

system("cls") # Borra la pantalla, en Windows.

while suma <= 1000:
    suma = suma + numero
    numero += 2 # Equivale a escribir numero = numero +2
    contador += 1

print(f"suma total es {suma}")
print(f"el numero de valores suamdos es {contador}")
print(f"el ultimo numero sumado es {numero}")