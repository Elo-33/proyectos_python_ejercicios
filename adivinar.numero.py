from random import randint

print('*** Juego de advivinar el numero ***')

# 2. Juego de Adivinar el Número
# Crea funciones para:
#
# Generar un número aleatorio
# Verificar si el intento del usuario es correcto, mayor o menor
# Contar los intentos realizados
# Dar pistas al usuario

def numero_aleatorio():
    aleatorio = randint(1, 100)

def verifica_numero(aleatorio):
    if numero_jugador == aleatorio:
        print('El numero es correcto')
    elif numero_jugador > aleatorio:
        print('Tu  numero es mas grande')
    elif numero_jugador < aleatorio:
        print('Tu numero es mas pequeño')
    else:
        print('Numero incorrecto')

def contar_intentos():
    intentos = 0

def pista():
    pass

numero_jugador = int(input('Ingrese tu numero para adivinar (1-100): '))
numero_aleatorio()
verifica_numero()
