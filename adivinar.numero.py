from random import randint

print('*** Juego de advivinar el numero ***')

# 2. Juego de Adivinar el Número
# Crea funciones para:
#
# Generar un número numero_a_buscar
# Verificar si el intento del usuario es correcto, mayor o menor
# Contar los intentos realizados
# Dar pistas al usuario

def numero_aleatorio():
    numero = randint(1, 100)
    print(f'El numero aleatorio es {numero}')
    return numero

def verifica_numero(numero_a_buscar, numero_jugador):
    if numero_jugador == numero_a_buscar:
        print('El numero es correcto has ganado')
        return True
    elif numero_jugador > numero_a_buscar:
        print(f'Tu numero {numero_jugador} es mas grande')
        return False
    elif numero_jugador < numero_a_buscar:
        print(f'Tu numero {numero_jugador} es mas pequeño')
        return False
    else:
        print('Numero incorrecto')
        return False

def contar_intentos(intentos):
    return intentos + 1


numero_a_buscar = numero_aleatorio()
salir = False
intentos = 0

while not salir:
    numero_jugador = int(input('Ingrese tu numero para adivinar (1-100): '))
    intentos = contar_intentos(intentos)

    gano = verifica_numero(numero_a_buscar, numero_jugador)
    if gano:
        print(f'🎉 Lo lograste en {intentos} intentos !!!!')
        salir = True
