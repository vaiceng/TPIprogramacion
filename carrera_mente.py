def juego_carrera_de_mente():
    print("Bienvenido al carrera de mente")
    print("Responde correctamente para ganar")
    print("Elige el nivel de dificultad:")
    print("1. Fácil")
    print("2. Medio")
    print("3. Difícil")

    nivel = input("Selecciona el nivel 1 - 2 - 3 : ")

    if nivel == "1":
        preguntas = [
            ("¿Por que las plantas son verdes?", "clorofila"),
            ("¿Cuantos dias tiene un año?", "366"),
            ("¿Cuantos mundiales tiene Argentina?", "3"),
        ]
    elif nivel == "2":
        preguntas = [
            ("¿Cuál es el río más largo de del mundo?", "Amazonas"),
            ("¿Cuantos huesos humanos tiene un adulto?", "206"),
            ("¿En qué año comenzó la revolución de mayo?", "1810"),
        ]
    elif nivel == "3":
        preguntas = [
            ("¿En que año se firmo la independecia en USA?", "1776"),
            ("¿Cuanto segundos hay en un dia?", "86400"),
            ("¿En qué año fue sancionada la constitución Argentina?", "1853"),
        ]
    else:
        print("Nivel no válido")
        return

    puntaje = 0

    for pregunta, respuesta_correcta in preguntas:
        print("\nPregunta:", pregunta)
        respuesta = input("Escriba su respuesta: ").lower()
        if respuesta == respuesta_correcta:
            print("Correcto")
            puntaje += 1
        else:
            print("Incorrecto, la respuesta era:", respuesta_correcta)

    print("\nJuego terminado, tu puntaje final es:", puntaje, "de", len(preguntas))
    if puntaje == len(preguntas):
        print("Muy bien!!")
    elif puntaje > 0:
        print("Buen intento, falto practica")
 

juego_carrera_de_mente()
