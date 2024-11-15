import random

palabras = ['gato', 'perro', 'luz', 'amor', 'juego', 'casa', 'mar']
diccionario = {
    'gato': ['gato', 'toga', 'gota'],
    'perro': ['perro', 'roper', 're'],
    'luz': ['luz', 'zul'],
    'amor': ['amor', 'roma', 'maro', 'roam'],
    'juego': ['juego', 'gouje', 'oje'],
    'casa': ['casa', 'saca', 'asca'],
    'mar': ['mar', 'ram', 'arm']
}

print('-----Bienvenidos a Descifra y Adivina-----\n')
print('Selecciona la dificultad:''\nFacil (5 intentos) = 1.''\nMedio (3 intentos) = 2.''\nDificil (1 intento) = 3.\n')

while True:
    dificultad = int(input('Elige 1, 2, 3: '))
    if dificultad == 1 or dificultad == 2 or dificultad == 3:
        break
    else:
        print('ERROR --> Coloque 1, 2 o 3')

if dificultad == 1:
    d = 5
elif dificultad == 2:
    d =  3
elif dificultad == 3:
    d = 1


numero_intentos= 0
palabra = random.choice(palabras)
palabras_validas = diccionario[palabra]
numero_palabras_validas = len(palabras_validas)

while numero_intentos < d:
    print('\n¡Comienza el juego!')
    print('Palabra:', palabra,)
    print('Tienes',d - numero_intentos,'intentos restantes.')

    intento = int(input('¿Cuántas palabras crees que se pueden formar?\n'))
    numero_intentos += 1
    
    if numero_palabras_validas == intento:
        print('Felicitaciones ganaste el juego.')
        break
    if numero_intentos == d:
        print("\nPerdiste el juego. La respuesta correcta era:", numero_palabras_validas)
    elif intento < numero_palabras_validas:
        print("Más alto")
    elif intento > numero_palabras_validas:
        print("Más bajo")