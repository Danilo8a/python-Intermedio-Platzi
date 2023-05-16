import random
import os


# Función para leer el archivo en la carpeta "files"
def read() -> list:
    with open("./files/words.txt", "r", encoding="utf-8") as f:
        return [line.replace("\n", "") for line in f]


# Función para escribir cosas en el archivo "names"
def append(in_word: str):
    with open("./files/words.txt", "a", encoding="utf-8") as f:
        f.write(in_word + "\n")


if __name__ == "__main__":
    # Se leen las palabras guardadas en el documento
    words = read()
    # Selecciona de forma aleatoria una de las palabras leídas desde el documento
    word_selected = random.choice(words)
    # Crea una cadena con tantas underlines como letras en la palabra seleccionada
    word_to_print = len(word_selected) * "_"
    # Inicializa los puntos del juego
    points = 100
    # Variable que guarda la opción a seleccionar
    option = 0
    # Ciclo while para que forzosamente el usuario seleccione una opción entre la 1 y la 3
    while option < 1 or option > 3:
        try:
            option = int(input("Ingrese el número de la opción que desea ejecutar:\n"
                               "1- Jugar\n"
                               "2- Ingresar una nueva palabra\n"
                               "3- Salir\n"
                               "-> "))
        # Captura de excepciones en caso de entradas numéricas o alfanuméricas
        except ValueError as ve:
            print("Solo puede ingresar números!")
    # Comprueba que se haya seleccionado la primera opción
    if option == 1:
        # Limpia la consola
        os.system("cls")
        # Ciclo while que comprueba que la palabra adivinada sea diferente a la seleccionada
        while word_to_print != word_selected:
            # Solicita al usuario el ingreso de una palabra e imprime los puntos y la palabra que se está adivinando
            letter_in = input(f"Ingrese una letra a continuación:\n\nPuntos: {points}\n\n{word_to_print}\n\n-> ")
            # Comprueba que la entrada sea un único carácter para continuar con la lógica del programa
            if len(letter_in) == 1:
                # Pone en mayúscula la entrada para comparar con las letras de la palabra seleccionada
                letter_in = letter_in.upper()
                # Bandera para comprobar que se haya encontrado la letra indicada en la palabra
                find = False
                # Ciclo para obtener tuplas con posición y caracter de la cadena seleccionada al asar
                for i, w in enumerate(word_selected):
                    # Comprueba que la letra ingresada sea igual a la i-ésima letra de la palabra al asar
                    if w == letter_in:
                        # Se lleva a verdadero la bandera
                        find = True
                        # Desvela la letra ingresada en la palabra adivinada
                        word_to_print = word_to_print[:i] + w + word_to_print[i + 1:]
                # Si no se encuentra la letra en la palabra, descuenta 10 puntos
                if not find:
                    points -= 10
                # Si se llega a 0 puntos, termina el juego
                if points == 0:
                    break
            # Limpia la consola
            os.system("cls")
        # Al salir, comprueba si se acabaron los puntos
        if points == 0:
            print("Has perdido!")
        else:
            print(f"¡Has ganado! Tu puntuación final es: {points}")
    # Comprueba que se ha seleccionado la segunda opción
    elif option == 2:
        # Limpia la consola
        os.system("cls")
        # Crea una nueva variable llamada new_world
        new_word = ""
        # Utiliza el método read() para leer las palabras guardadas en la base de datos
        words = read()
        # Ciclo while que se mantiene mientras: la palabra ingresada es vacía, la entrada no es solo letras o la palabra
        # ya se encuentra en el documento
        while new_word == "" or not new_word.isalpha() or new_word in words:
            # Palabra de entrada
            new_word = input("Ingrese la nueva palabra:\n-> ").upper()
            # Si la palabra se encuentra en el documento, imprime este mensaje
            if new_word in words:
                print("La palabra ya se encuentra en la base de datos!\n")
            # Si la entrada es vacía o no es solo letras, implrime este mensaje
            elif new_word == "" or not new_word.isalpha():
                print("Debes ingresar una palabra válida!\n")
        # De comprobarse todo, incluye la palabra
        append(new_word)
        # Imprime las palabras incluida la nueva
        print(f"Palabras guardadas en el documento de texto:")

        words = read()
        for w in words:
            print(f"{words.index(w) + 1}- {w}")
