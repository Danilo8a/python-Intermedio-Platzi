# Función para leer el archivo en la carpeta "files"
def read():
    numbers = []
    with open("./files/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


# Función para escribir cosas en el archivo "names"
def overwrite():
    names = ["Danilo", "Lidsahi", "Sindy", "Luis", "Silvio", "Milagros"]
    with open("./files/names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name+"\n")


def run():
    read()
    overwrite()


if __name__ == "__main__":
    run()
