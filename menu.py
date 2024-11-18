from Juego_oca import jugar as jugar_oca
from adivina_capitales import jugar as jugar_capitales
from adivinaydescifra import jugar as jugar_descifra
from buscaminas import jugar as jugar_buscaminas
from carrera_mente import jugar as jugar_mente

def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Jugar al Juego de la Oca")
        print("2. Jugar a Adivina las Capitales")
        print("3. Jugar a Adivina y Descifra")
        print("4. Jugar al Buscaminas")
        print("5. Jugar a Carrera de Mente")
        print("6. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            print("\n¡Iniciando el Juego de la Oca!")
            jugar_oca()
        elif opcion == "2":
            print("\n¡Iniciando Adivina las Capitales!")
            jugar_capitales()
        elif opcion == "3":
            print("\n¡Iniciando Adivina y Descifra!")
            jugar_descifra()
        elif opcion == "4":
            print("\n¡Iniciando el Buscaminas!")
            jugar_buscaminas()
        elif opcion == "5":
            print("\n¡Iniciando Carrera de Mente!")
            jugar_mente()
        elif opcion == "6":
            print("\n¡Gracias por jugar! Hasta la próxima.")
            break
        else:
            print("\nOpción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
