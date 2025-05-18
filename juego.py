import sys
import random

def jugar_piedra_papel_tijeras(jugador):
    
    opciones = ['piedra', 'papel', 'tijeras']
    
    # Se valida entrada del jugador
    jugador = jugador.lower()
    if jugador not in opciones:      # si eleccion no esta opciones imprime  mensaje
        print("Argumento inválido: Debe ser piedra, papel o tijera.")
        return
    
    #La computadora elige en forma aleatoria entre las opciones 
    computadora = random.choice(opciones) 
    
    # Bloque de determinacion del resultado
    if jugador == computadora:
        resultado = "¡Empate!"
    elif (
        (jugador == 'piedra' and computadora == 'tijeras') or
        (jugador == 'papel' and computadora == 'piedra') or
        (jugador == 'tijeras' and computadora == 'papel')
    ):
        resultado = "¡Ganaste!"
    else:
        resultado = "¡Perdiste!"
    
    # Imprime los resultados
    print(f"\nTu jugaste: {jugador}")
    print(f"Computador jugó: {computadora}")
    print(resultado)

#Para que este código solo se ejecute cuando el script es el programa principal
if __name__ == "__main__":
    if len(sys.argv) != 2:  #Es una lista que contiene los argumentos de línea de comandos 
        print("Uso: python juego.py 'piedra', 'papel' o 'tijeras'")
        print("Ejemplo: python juego.py piedra")
    else:
        jugar_piedra_papel_tijeras(sys.argv[1])