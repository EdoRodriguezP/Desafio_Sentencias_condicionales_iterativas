# Desafios_Python
Repo con desafios de Desafios Latam.

# Desafío - Sentencias condicionales e iterativas (I)

En este desafío validaremos nuestros conocimientos para identificar qué instrucciones de bloque utilizar para manejar el flujo en base a condiciones lógicas.

## Actividad 1 - IMC

El IMC, conocido también como el Índice de masa corporal, es una medida que asocia el peso de una persona con su talla (su altura). Este valor es utilizado normalmente como un indicador nutricional y constituye un índice fácil y sencillo de calcular para determinar el estado de obesidad y sobrepeso de una persona.

**Fórmula del IMC:**  
IMC = peso (kg) / (altura (m))²

### Clasificación OMS

| Rango de IMC    | Clasificación OMS    |
|-----------------|----------------------|
| < 18.5         | Bajo Peso            |
| [18.5, 25[     | Adecuado             |
| [25, 30[       | Sobrepeso            |
| [30, 35[       | Obesidad Grado I     |
| [35, 40[       | Obesidad Grado II    |
| > 40           | Obesidad Grado III   |

### Requerimientos

Se solicita crear el programa `imc.py` que permita calcular el IMC de una persona:

1. Ingresar el peso en Kg y la talla (altura) en centímetros
2. Calcular el IMC ajustando los valores de entrada a las unidades requeridas por la fórmula
   - El resultado debe mostrarse con 2 decimales
3. Mostrar al usuario:
   - El valor de su IMC
   - La clasificación según la OMS

### Ejemplo de validación

python imc.py 81 178

Su IMC es 25.56
La clasificación OMS es Sobrepeso

## Actividad 2 - Cachipún

El Cachipún (también conocido como chin chan pu, pikachú, jankenpón, yan ken po, pin pon papas, hakembó o how-are-you-speak) es un juego de manos con tres elementos:

- **Piedra** vence a **tijera** (la rompe)
- **Tijera** vence a **papel** (lo corta)
- **Papel** vence a **piedra** (la envuelve)

Formando así un ciclo cerrado de reglas. Se utiliza frecuentemente para tomar decisiones entre dos personas.

### Requerimientos

Se implementará un programa `cachipun.py` donde:

1. El usuario ingresa como argumento: `piedra`, `papel` o `tijera`
2. El computador elige aleatoriamente usando `random.choice()`
3. Se determinan las posibles salidas:
   - Ganar
   - Perder
   - Empatar
4. Validación de entrada:
   - Si el argumento no es válido, mostrar mensaje de error

### Ejemplo de ejecución

python juego.py piedra

Tu jugaste Piedra
Computador jugó tijera
Ganaste!!

python juego.py papelon
Argumento inválido: Debe ser piedra, papel o tijera.






