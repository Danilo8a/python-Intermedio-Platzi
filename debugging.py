# Función mal hecha a propósito
def divisors(num: int):
    div_list = []

    for i in range(1, num + 1):
        # Acá está (estaba) el error
        if num % i == 0:
            div_list.append(i)

    return div_list


def run():
    num = int(input("Ingrese un número al que desee calcular sus divisores -> "))
    print(divisors(num))
    print("Fin del programa!")


if __name__ == "__main__":
    run()
