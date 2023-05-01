def run():
    # Creando lista con el cuadrado de los primeros 100 enteros
    """
    squares = []
    for i in range(1, 101):
        # Guardando solo el cuadrado de los que NO SON DIVISIBLES ENTRE 3
        if i % 3 != 0:
            squares.append(i ** 2)
    """
    # Creando la lista con list comprehentions
    squares = [i ** 2 for i in range(1, 101) if i % 3 != 0]
    print(squares)

    # Reto de la clase:
    # Crear una lista con los múltiplos de 4, 6 y 9 que tengan 4 dígitos
    reto = [i for i in range(1, 10001) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0 and len(str(i)) < 5]
    print(reto)

if __name__ == "__main__":
    run()
