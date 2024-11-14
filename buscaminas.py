import random

def crear_tablero(filas, columnas, minas):
    tablero = [[" " for _ in range(columnas)] for _ in range(filas)]
    minas_colocadas = 0
    while minas_colocadas < minas:
        f, c = random.randint(0, filas - 1), random.randint(0, columnas - 1)
        if tablero[f][c] != "*":
            tablero[f][c] = "*"
            minas_colocadas += 1
    return tablero

def contar_minas_adyacentes(tablero, filas, columnas):
    conteo = [[0 for _ in range(columnas)] for _ in range(filas)]
    for i in range(filas):
        for j in range(columnas):
            if tablero[i][j] == "*":
                conteo[i][j] = "*"
            else:
                minas_adyacentes = 0
                for x in range(max(0, i-1), min(i+2, filas)):
                    for y in range(max(0, j-1), min(j+2, columnas)):
                        if tablero[x][y] == "*":
                            minas_adyacentes += 1
                conteo[i][j] = minas_adyacentes
    return conteo

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(str(celda) for celda in fila))
    print()

def jugar_buscamina(filas, columnas, minas):
    while True:
        tablero = crear_tablero(filas, columnas, minas)
        tablero_minas = contar_minas_adyacentes(tablero, filas, columnas)
        tablero_visible = [["-" for _ in range(columnas)] for _ in range(filas)]
        
        while True:
            mostrar_tablero(tablero_visible)
            try:
                f = int(input("Selecciona una fila (1 a {}): ".format(filas))) - 1
                c = int(input("Selecciona una columna (1 a {}): ".format(columnas))) - 1
            except ValueError:
                print("Por favor, ingresa un número válido.")
                continue

            if f < 0 or f >= filas or c < 0 or c >= columnas:
                print("Coordenadas fuera de rango. Intenta de nuevo.")
                continue

            if tablero[f][c] == "*":
                print("¡Has descubierto una mina! Fin del juego.")
                mostrar_tablero(tablero_minas)
                break

            tablero_visible[f][c] = tablero_minas[f][c]

            casillas_no_minas = filas * columnas - minas
            descubiertas = sum(fila.count("-") == 0 for fila in tablero_visible)
            if descubiertas == casillas_no_minas:
                print("¡Felicidades, has ganado!")
                mostrar_tablero(tablero_minas)
                break
        # Preguntar si el jugador desea jugar de nuevo
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if jugar_de_nuevo != 's':
            print("Gracias por jugar.")
            break

# Configuración del juego
filas = 5
columnas = 5
minas = 5
jugar_buscamina(filas, columnas, minas)
