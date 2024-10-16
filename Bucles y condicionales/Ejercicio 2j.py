"""Pida por teclado números, hasta que introduzca el 0. Posteriormente debe mostrar su suma y su producto."""

# Importación de librerías:
from os import system # Importo el comando "system" de la libreía "os"

# Declaración de variables:

numero = 2 # Para pedir por teclado el valor con el que voy a operar.
suma = 0 # Para acumular los valores sumados del numero pedido por teclado
producto = 1 # Para acumular la multiplicacion de los numeros

# Programa principal:

system("cls") # Borra la pantalla, en Windows.

while numero != 0: # ! = distinto de cero
    numero = float(input("introduce el numero a multiplicar y sumar:(0 para terminar)"))
    suma = suma + numero
    if numero != 0:
        producto = producto * numero


print(f"suma total es {suma}")
print(f"la multiplicacion total es  {producto}")
