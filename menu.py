def mostrar_menu():
        print("\n--- Menú Principal ---")
        print("1. Jugar al Juego de la Oca")
        print("2. Jugar a Adivina las Capitales")
        print("3. Jugar a Adivina y Descifra")
        print("4. Jugar al Buscaminas")
        print("5. Jugar a Carrera de Mente")
        print("6. Salir")
        

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")
        
    if opcion == "1":
        print("\n¡Iniciando el Juego de la Oca!")
        import Juego_oca 
        Juego_oca.jugar()
    elif opcion == "2":
        print("\n¡Iniciando Adivina las Capitales!")
        import adivina_capitales 
        adivina_capitales.juego_adivinar_capital()
    elif opcion == "3":
        print("\n¡Iniciando Adivina y Descifra!")
        import adivinaydescifra 
        adivinaydescifra.jugar_adivinaydescifra()
    elif opcion == "4":
        print("\n¡Iniciando el Buscaminas!")
        import buscaminas 
        buscaminas.jugar_buscamina()
    elif opcion == "5":
        print("\n¡Iniciando Carrera de Mente!")
        import carrera_mente  
        carrera_mente.juego_carrera_de_mente()
    elif opcion == "6":
        print("\n¡Gracias por jugar! Hasta la próxima.")
        break
    else:
        print("\nOpción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()
