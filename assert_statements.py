#
def divisors(num: int):
    div_list = []
    for i in range(1, num + 1):
        if num % i == 0:
            div_list.append(i)

    return div_list


def run():
    num = input("Ingrese un número al que desee calcular sus divisores -> ")
    assert int(num) > 0, "Solo puedes ingresar números positivos!"
    assert num.isnumeric(), "Solo puedes ingresar números en la función!"
    print(divisors(int(num)))
    print("Fin del programa!")


if __name__ == "__main__":
    run()
