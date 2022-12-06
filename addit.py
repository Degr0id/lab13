import tools


def check_if_bd(file):
    good = True
    for line in file:
        if line.count("|") != 3:
            good = False
            break
    file.seek(0)
    return good


def max_len_field(file):
    res = [0] * 4
    for line in file:
        tmp = line.strip().split("|")
        for i in range(4):
            res[i] = max(res[i], len(tmp[i]))
    file.seek(0)
    return res


def menu():
    file_name = ""
    while True:
        print("\nМеню")
        print("1) Выбрать файл для работы\n"
              "2) Инициализировать базу данных\n"
              "3) Вывести содержимое базы данных\n"
              "4) Добавить запись в конец базы данных\n"
              "5) Поиск по одному полю\n"
              "6) Поиск по двум полям\n"
              "9) Очистить ввод\n"
              "0) Выход.")
        user_input = input("Ввод-->")
        if user_input == "1":
            file_name = tools.getfilename()
        elif user_input == "2":
            tools.create_db(file_name)
        elif user_input == "3":
            tools.output(file_name)
        elif user_input == "4":
            tools.add(file_name)
        elif user_input == "5":
            tools.search_by_one(file_name)
        elif user_input == "6":
            tools.search_by_two(file_name)
        elif user_input == "9":
            clear = "\n" * 100
            print(clear)
        elif user_input == "0":
            break
        else:
            print("Некорректный ввод, пожалуйста введите номер операции\n")
