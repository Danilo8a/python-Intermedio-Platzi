# Agregando control de excepciones
def divisors(num: int):
    div_list = []
    # Manejando el ingreso de números negativos
    try:
        if num < 0:
            raise ValueError("Solo puedes ingresar números positivos!")

        for i in range(1, num + 1):

            if num % i == 0:
                div_list.append(i)

        return div_list
    except ValueError as ve:
        print(ve)
        

def run():
    try:  # Bloque try - except para manejar errores al ingresar letras/palabras en lugar de números
        num = int(input("Ingrese un número al que desee calcular sus divisores -> "))
        print(divisors(num))
        print("Fin del programa!")
    except ValueError as ve:
        print("Debes ingresar un número!")


if __name__ == "__main__":
    run()
