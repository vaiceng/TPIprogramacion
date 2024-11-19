import random

# Diccionario con preguntas organizadas por categoría
preguntas = {
    "Historia": [
        {
            "pregunta": "¿En qué año comenzó la Segunda Guerra Mundial?",
            "opciones": ["1939", "1945", "1914", "1929"],
            "respuesta": "1939"
        },
        {
            "pregunta": "¿Quién fue el primer presidente de los Estados Unidos?",
            "opciones": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"],
            "respuesta": "George Washington"
        }
    ],
    "Ciencia": [
        {
            "pregunta": "¿Cuál es el planeta más grande del sistema solar?",
            "opciones": ["Tierra", "Júpiter", "Saturno", "Marte"],
            "respuesta": "Júpiter"
        },
        {
            "pregunta": "¿Qué partícula subatómica tiene carga negativa?",
            "opciones": ["Protón", "Neutrón", "Electrón", "Quark"],
            "respuesta": "Electrón"
        }
    ],
    "Geografía": [
        {
            "pregunta": "¿Cuál es el río más largo del mundo?",
            "opciones": ["Amazonas", "Nilo", "Yangtsé", "Mississippi"],
            "respuesta": "Amazonas"
        },
        {
            "pregunta": "¿En qué continente se encuentra el desierto del Sahara?",
            "opciones": ["Asia", "África", "Oceanía", "América del Sur"],
            "respuesta": "África"
        }
    ]
}

def mostrar_categorias():
    """Muestra las categorías disponibles."""
    print("Categorías disponibles:")
    for categoria in preguntas:
        print("- ",categoria)

def hacer_pregunta(categoria):
    """Realiza una pregunta aleatoria de la categoría seleccionada."""
    pregunta = random.choice(preguntas[categoria])
    print("\nCategoría: ",categoria)
    print(pregunta["pregunta"])
    for i, opcion in enumerate(pregunta["opciones"], start=1):
        print(f"{i}. {opcion}")
    respuesta_usuario = input("Selecciona el número de la respuesta: ")
    respuesta_correcta = pregunta["opciones"].index(pregunta["respuesta"]) + 1
    return int(respuesta_usuario) == respuesta_correcta

def jugar_preguntados():
    """Función principal del juego."""
    puntuacion = 0
    rondas = 5
    print("¡Bienvenido a Preguntados!")
    for ronda in range(1, rondas + 1):
        print("\nRonda ", ronda, "de", rondas)
        mostrar_categorias()
        categoria = input("Elige una categoría: ")
        if categoria in preguntas:
            if hacer_pregunta(categoria):
                print("¡Correcto!")
                puntuacion += 1
            else:
                print("Incorrecto.")
        else:
            print("Categoría no válida. Pierdes esta ronda.")
    print("\nJuego terminado. Tu puntuación final es: ", puntuacion, "de", rondas)
    if puntuacion == rondas:
        print("¡Excelente! Eres un maestro del conocimiento.")
    elif puntuacion >= rondas / 2:
        print("¡Buen trabajo! Puedes mejorar aún más.")
    else:
        print("No te preocupes, sigue practicando y lo lograrás.")

if __name__ == "__main__":
    jugar_preguntados()