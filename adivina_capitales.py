import random

def cargar_paises_y_capitales(archivo): # función para cargar el archivo y devolver los países y capitales
    paises_y_capitales = {}
    with open(archivo, 'r', encoding='utf-8') as file: 
        # abre el archivo en modo lectura - especifica el conjunto de caracteres que se usará para interpretar el contenido del archivo 
        for linea in file:
            pais, capital = linea.strip().split(',')
            # elimina espacios innecesarios y separa elementos de una lista
            paises_y_capitales[pais] = capital
    return paises_y_capitales
    
def juego_adivinar_capital(paises_y_capitales): # función principal del juego
    puntaje = 0  
    jugando = True
    while jugando:
        pais, capital_correcta = random.choice(list(paises_y_capitales.items()))  # seleccionar un país-capital aleatorio
        # selecciona un elemento al azar - devuelve una vista de todos sus pares clave-valor como tuplas
        print("¿Cuál es la capital de", pais, "?")
        respuesta = input("Tu respuesta: ")
        
        if respuesta.strip().lower() == capital_correcta.lower(): 
            # verificar si la respuesta es correcta comparando: sacando espacios inecesarios y convirtiendo a minusculas
            print("¡Correcto! 🎉 Ganaste un punto.")
            puntaje += 1
        else:
            print("Incorrecto. La capital de ", pais, "es", capital_correcta)
        
        print("Puntaje actual: ", puntaje)
        
        if puntaje == 10: # verificar si el puntaje ha llegado a 10 puntos
            print("¡Felicidades! Has alcanzado 10 puntos y ganado el juego. 🎉")
            break
        
        jugar_nuevamente = input("¿Quieres jugar de nuevo? (s/n): ")
        if jugar_nuevamente == 'n':  # Si el jugador elige "n", termina el juego
            print("Gracias por jugar. ¡Hasta la próxima!")
            jugando = False
    print("Puntaje final:", puntaje)

# cargar los países y capitales desde el archivo y empezar el juego
if __name__ == "__main__": 
    paises_y_capitales = cargar_paises_y_capitales("paises_y_capitales.txt")
    juego_adivinar_capital(paises_y_capitales)

