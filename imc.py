import sys

def calcula_imc(peso, altura_cm):
    
    altura = altura_cm / 100 
    imc = peso / (altura ** 2)
    return round(imc, 2)

def clasifica_imc(imc):

    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidad grado I"
    elif 35 <= imc < 40:
        return "Obesidad grado II"
    else:
        return "Obesidad grado III"

if __name__ == "__main__":
    # 
    if len(sys.argv) != 3:
        print("Uso: python imc.py 'peso en kg' y 'altura en cm'")
        print("Ejemplo: python imc.py 70 165")
        sys.exit(1)
    
    try:
        peso = float(sys.argv[1])
        altura = float(sys.argv[2])
        
        if peso <= 0 or altura <= 0:
            print("Argumento inválido: El peso y la altura deben ser valores positivos")
            sys.exit(1)
            
        imc = calcula_imc(peso, altura)
        clasificacion = clasifica_imc(imc)
        
        print(f"Su IMC es {imc}")
        print(f"La clasificación OMS es {clasificacion}")
        
    except ValueError:
        print("Argumento inválido: El peso y la altura deben ser valores numéricos")
        sys.exit(1)