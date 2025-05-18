import sys
import random

def jugar_piedra_papel_tijeras(jugador):       # Define funcion juego piedra papel y tijeras
    
    opciones = ['piedra', 'papel', 'tijeras']   # Opciones del juego
    
    jugador = jugador.lower()        # Se valida entrada del jugador
    if jugador not in opciones:      # si eleccion no esta opciones imprime  mensaje
        print("\nArgumento inválido: Debe ser piedra, papel o tijera.\n")
        return
    
    computadora = random.choice(opciones) #La computadora elige en forma aleatoria entre las opciones 
    
    if jugador == computadora:           # Bloque de determinacion del resultado
        resultado = "¡Empate!"
    elif (
        (jugador == 'piedra' and computadora == 'tijeras') or
        (jugador == 'papel' and computadora == 'piedra') or
        (jugador == 'tijeras' and computadora == 'papel')
    ):
        resultado = "¡Ganaste!"
    else:
        resultado = "¡Perdiste!"
    
    
    print(f"\nTu jugaste: {jugador}")            # Imprime los resultados
    print(f"Computador jugó: {computadora}")
    print(f"{resultado}\n")


if __name__ == "__main__":     # Para que este código solo se ejecute cuando el script es el programa principal
    if len(sys.argv) != 2:     # Es una lista que contiene los argumentos de línea de comandos 
        print("\nUso: python juego.py 'piedra', 'papel' o 'tijeras'")    # si datos no son correctos entra en el bloque imprimiendo instrucciones
        print("Ejemplo: python juego.py piedra\n")
    else:
        jugar_piedra_papel_tijeras(sys.argv[1])              