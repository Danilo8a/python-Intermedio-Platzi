import colorama
colorama.init()


# Función susceptible a generar una excepción
def palindrome(string):
    try:
        if string == "":
            raise ValueError(colorama.Fore.RED+"No se pueden ingresar cadenas vacías"+colorama.Fore.WHITE)
        else:
            return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False


def run():
    # Función nerfeada para poder hacer la explicación xD
    # string = input("Ingrese una palabra -> ")
    # Bloque tyr-except para capturar la posible excepción TypeError.
    try:
        print(palindrome(""))
    except TypeError:
        print("Solo puedes escribir palabras!")


if __name__ == "__main__":
    run()
