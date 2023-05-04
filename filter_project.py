# Diccionario con los datos a filtrar
DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Danilo',
        'age': 25,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'python',
    },
    {
        'name': 'Esteban',
        'age': 22,
        'organization': 'Intelix',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 17,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Manuel',
        'age': 32,
        'organization': 'SA Tech',
        'position': 'Backend Developer',
        'language': 'php',
    },
    {
        'name': 'Lidsahi',
        'age': 27,
        'organization': 'GenSet Designer',
        'position': 'Community Manager',
        'language': '',
    },
    {
        'name': 'Mariangela',
        'age': 29,
        'organization': '',
        'position': 'Student',
        'language': 'r',
    },
]


def run():
    # Función para imprimir fancy con expresiones lambda
    print_fancy = lambda arry: print(f"{arry}\n{12 * len(arry) * '-'}")

    # todos los trabajadores de python, solo nombres
    all_py_name = [worker['name'] for worker in DATA if worker['language'] == 'python']
    print_fancy(all_py_name)

    # todos los trabajadores de python
    all_platzi_name = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']
    print_fancy(all_platzi_name)

    # Ahora los mayores pero con filter
    adults = list(filter(lambda i: i['age'] > 18, DATA))
    adults = list(map(lambda i: i['name'], adults))
    print_fancy(adults)

    # Agrega un nuevo campo a los diccionarios llamado old con valor true si es > 18 o false si no.
    old_workers = list(map(lambda i: i | {'old': True if i['age'] > 18 else False}, DATA))
    print_fancy(old_workers)

    # Reto: hacer all_py_name y all_platzi_name con filter y map
    all_py_name = list(filter(lambda i: i['language'] == 'python', DATA))
    all_py_name = list(map(lambda i: i['name'], all_py_name))
    print_fancy(all_py_name)

    all_platzi_name = list(filter(lambda i: i['organization'] == 'Platzi', DATA))
    all_platzi_name = list(map(lambda i: i['name'], all_platzi_name))
    print_fancy(all_platzi_name)


if __name__ == "__main__":
    run()
