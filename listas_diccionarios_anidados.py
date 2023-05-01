def run():

    # Listas y diccionarios cualesquiera
    my_list = [1, 'Danilo Ochoa', True, 9.9]
    my_dict = {'firstname': 'Danilo', 'lastname': 'Ochoa'}

    # Lista y diccionario anidados
    my_super_list = [
        {'firstname': 'Danilo', 'lastname': 'Ochoa'},
        {'firstname': 'Lidsahi', 'lastname': 'San Blas'},
        {'firstname': 'Jimmy', 'lastname': 'Rincones'},
        {'firstname': 'Ivan', 'lastname': 'Noname'}
    ]

    my_super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-2, -1, 0, 1, 2],
        "float_nums": [0.1, 0.2, 0.3, 0.4, 0.5]
    }

    for key, value in my_super_dict.items():
        print(key, "-", value)


if __name__ == '__main__':
    run()
