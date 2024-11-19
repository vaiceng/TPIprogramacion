def mostrar_menu():
        print("\n--- Menú Principal ---")
        print("1. Jugar al Juego de la Oca")
        print("2. Jugar a Adivina las Capitales")
        print("3. Jugar a Adivina y Descifra")
        print("4. Jugar al Buscaminas")
        print("5. Jugar a Preguntados")
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
        paises_y_capitales = adivina_capitales.cargar_paises_y_capitales('paises_y_capitales.txt')
        adivina_capitales.juego_adivinar_capital(paises_y_capitales)
    elif opcion == "3":
        print("\n¡Iniciando Adivina y Descifra!")
        import adivinaydescifra 
        adivinaydescifra.jugar_adivinaydescifra()
    elif opcion == "4":
        print("\n¡Iniciando el Buscaminas!")
        import buscaminas 
        buscaminas.jugar_buscamina(5, 5, 5)
    elif opcion == "5":
        print("\n¡Iniciando Preguntados!")
        import preguntados  
        preguntados.jugar_preguntados()
    elif opcion == "6":
        print("\n¡Gracias por jugar! Hasta la próxima.")
        break
    else:
        print("\nOpción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()
