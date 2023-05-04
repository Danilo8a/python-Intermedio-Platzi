import math


def run():
    my_dict = {i: i ** 3 for i in range(1, 101) if i % 3 != 0}
    print(my_dict)
    
    # Reto: crear un diccionario con los primeros 1000 números naturas cuyos valores sean sus raíces cuadradas.
    another_dict = {i: math.sqrt(i) for i in range(1, 1001) if i % 3 != 0}
    print(another_dict)


if __name__ == "__main__":
    run()
