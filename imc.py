import sys

def calculo_imc(peso, altura_cm): # define funcion calculo_imc para realizar el calculo del IMC
    altura = altura_cm / 100
    imc = peso / (altura ** 2)
    return round(imc, 2)       # El resultado se redondea a 2 decimales.

def  clasifica_imc(imc):        # define funcion para clasificacion OMS
    if imc < 18.5:              #
        return "Bajo peso"
    elif imc >= 18.5 and imc < 25:
        return "Peso normal"
    elif imc >= 25 and imc < 30:
        return "Sobrepeso"
    elif imc >= 30 and imc < 35:
        return "Obesidad grado I"
    elif imc >= 35 and imc < 40:
        return "Obesidad grado II"
    else:
        return "Obesidad grado III"

if __name__ == "__main__":      # Determina si el script se está ejecutando directamente
    if len(sys.argv) != 3:      # Lista de argumentos pasados por consola / verifica si se ingresaron 2 argumentos
        print("Uso: python imc.py 'peso en kg' y 'altura en cm'")  # si datos no son correctos entra en el bloque imprimiendo instrucciones
        print("ejemplo python imc.py 70 165")
        sys.exit(1)             # Termina el programa con un código de error 1

    try:                        # Manejo de errores
        peso = float(sys.argv[1])   # sys.argv son strings (porque los argumentos de línea de comandos siempre vienen como texto).
        altura = float(sys.argv[2])  # se convierten an float
    
        if peso <= 0 or altura <= 0: # Validacion de positivos con mensajr de error
            print("Argumento inválido: El peso y la altura deben ser valores positivos")
            sys.exit(1)         # Termina el programa con un código de error 1
    
    except ValueError:
        print("Argumento inválido: El peso y la altura deben ser valores numéricos")
        sys.exit(1)
        
    imc = calculo_imc(peso, altura)
    clasificacion = clasifica_imc(imc)
        
    print(f"Su IMC es {imc}")
    print(f"La clasificación OMS es {clasificacion}")
        