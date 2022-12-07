import Student
import addit


def getfilename():
    name = input("Введите адресс файла: ")
    return name


def create_db(file_name):
    while True:
        try:
            f = open(file_name, 'w')
            num = int(input("Введите количество записей: "))
        except OSError:
            print("Некорректный путь к файлу")
            return -1
        except ValueError:
            print("Пожалуйста введите целое число")
        else:
            break
    i = 1
    while i <= num:
        print(f"{i}-я запись:")
        pname = input("Введите имя (Имя Ф.): ")
        pyear = input("Введите год рождения: ")
        pres = input("Введите результат экзамена: ")
        ppassed = input("Допущен (Да/Нет): ")
        person = Student.Stud([pname, pyear, pres, ppassed])
        # if person.check_fields():
        #     f.write(str(person))
        #     i += 1
        # else:
        #     print("Ошибка в вводе полей")
        f.write(f"{str(person)}\n")
        i += 1
    f.close()


def output(file_name):
    try:
        f = open(file_name, 'r')
    except OSError:
        print("Файл не найден")
        return -1
    if addit.check_if_bd(f):
        if f.readline() == "":
            print("Файл пуст")
            return 0
        widths = addit.max_len_field(f)
        tt_w = 3
        for i in range(4):
            widths[i] = max(14, widths[i])
            tt_w += widths[i]
        print(f"{'-' * tt_w}\n{'Имя'.center(widths[0])}|{'Год рождения'.center(widths[1])}|"
              f"{'Балл'.center(widths[2])}|{'Допущен'.center(widths[3])}\n{'-' * tt_w}")
        for line in f:
            pers = Student.Stud(line.strip().split("|"), widths)
            print(str(pers))
        print(f"{'-' * tt_w}")
    else:
        print("Неверный формат базы данных")
    f.close()


def add(file_name):
    try:
        f = open(file_name, 'r')
    except OSError:
        print("Файл не найден")
        return -1
    tmp = addit.check_if_bd(f, True)
    if tmp[0]:
        f = open(file_name, 'a')
        if not tmp[1].endswith("\n"):
            f.write("\n")
        pname = input("Введите имя (Имя Ф.): ")
        pyear = input("Введите год рождения: ")
        pres = input("Введите результат экзамена: ")
        ppassed = input("Допущен (Да/Нет): ")
        person = Student.Stud([pname, pyear, pres, ppassed])
        f.write(str(person))
    else:
        print("Неверный формат базы данных")
    f.close()


def search_by_one(file_name):
    try:
        f = open(file_name, 'r')
    except OSError:
        print("Файл не найден")
        return -1
    if not addit.check_if_bd(f):
        print("Неверный формат базы данных")
        f.close()
        return -1
    print("Выберите поле:\n1)Имя\n2)Год рождения\n3)Балл\n4)Допуск")
    while True:
        try:
            u_inp = int(input("-->")) - 1
        except ValueError:
            print("Введите номер поля")
        else:
            if not (0 <= u_inp <= 3):
                print("Введите номер поля")
                continue
            break
    val = input("Искомое значение: ")
    print("Результат:")
    was_changed = False
    for line in f:
        fields = line.strip().split("|")
        if fields[u_inp] == val:
            print(line, end='')
            was_changed = True
    if not was_changed:
        print("Подходящих записей нет")
    f.close()


def search_by_two(file_name):
    try:
        f = open(file_name, 'r')
    except OSError:
        print("Файл не найден")
        return -1
    if not addit.check_if_bd(f):
        print("Неверный формат базы данных")
        f.close()
        return -1
    print("Выберите первое поле:\n1)Имя\n2)Год рождения\n3)Балл\n4)Допуск")
    while True:
        try:
            u_inp1 = int(input("-->")) - 1
        except ValueError:
            print("Введите номер поля")
        else:
            if not (0 <= u_inp1 <= 3):
                print("Введите номер поля")
                continue
            break
    val1 = input("Искомое значение: ")
    print("Выберите второе поле:")
    while True:
        try:
            u_inp2 = int(input("-->")) - 1
        except ValueError:
            print("Введите номер поля")
        else:
            if not (0 <= u_inp2 <= 3):
                print("Введите номер поля")
                continue
            break
    val2 = input("Искомое значение: ")
    print("Результат:")
    was_changed = False
    for line in f:
        fields = line.strip().split("|")
        if fields[u_inp1] == val1 and fields[u_inp2] == val2:
            print(line, end='')
            was_changed = True
    if not was_changed:
        print("Подходящих записей нет")
    f.close()
