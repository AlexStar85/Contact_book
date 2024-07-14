# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в # текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# 1. Создание файла: +++
#     - открываем файл на дозапись +++
# 2. Добавление контакта: +++
#     - запросить у пользователя новый контакт +++
#     - открываем файл на дозапись +++
#     - добавить новый контакт +++
# 3. Вывод данных на экран:
#     - открыть файл на чтение +++
#     - считать файл +++
#     - вывести на экран +++
# 4. Поиск контакта:
#     - выбор варинта поиска
#     - запросить данные для поиска
#     - открытие файла на чтение
#     - считывание данных, сохраняем их в переменню
#     - осществлем поиск контакта
#     - вывод на экран найденного контакта
# 5. Создание user Intarface (UI)
#     - вывести меню на экран +++
#     - запросить вариант действия +++
#     - запустить выбранную функцию +++
#     - осществить возможность выхода из программы +++

def input_surname():
    return input("Введите фамилию контакта: ").title()

def input_name():
    return input("Введите имя контакта: ").title()

def input_patronymic():
    return input("Введите отчество контакта: ").title()

def input_phone():
    return input("Введите телефон контакта: ")  # Убрал .title() для номера телефона

def input_address():
    return input("Введите адрес(город) контакта: ").title()

def create_contact():
    """Запрашивает данные контакта и возвращает строку с информацией."""
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f'{surname} {name} {patronymic}: {phone}\n{address}\n\n'

def add_contact():
    """Добавляет новый контакт в справочник."""
    contact_str = create_contact()
    with open('phonebook.txt', "a", encoding="utf-8") as file:
        file.write(contact_str)

def print_contacts():
    """Выводит все контакты из справочника с нумерацией."""
    with open('phonebook.txt', "r", encoding="utf-8") as file:
        contacts_str = file.read()
    contacts_list = contacts_str.rstrip().split('\n\n')
    for n, contact in enumerate(contacts_list, 1):
        print(n, contact)

def search_contacts():
    """Ищет контакт по выбранному полю."""
    print(
        'Возможные варианты поиска:\n'
        '1. По фамилии\n'
        '2. По имени\n'
        '3. По отчеству\n'
        '4. По телефону\n'
        '5. По адрес(город)'
    )
    var = input('Выберите вариант поиска: ')
    while var not in ('1', '2', '3', '4', '5'):
        print('Некорректный ввод!')
        var = input('Выберите вариант действия: ')
    i_var = int(var) - 1

    search = input('Введите данные для поиска: ').title()
    with open('phonebook.txt', "r", encoding="utf-8") as file:
        contacts_str = file.read()
    contacts_list = contacts_str.rstrip().split('\n\n')

    for str_contact in contacts_list:
        lst_contact = str_contact.replace(':', '').split()
        if search in lst_contact[i_var]:
             print(str_contact)

def edit_contact():
    """Изменяет данные существующего контакта."""
    print_contacts()
    contact_num = int(input("Введите номер контакта для редактирования: ")) - 1
    with open('phonebook.txt', "r", encoding="utf-8") as file:
        contacts_list = file.read().rstrip().split('\n\n')
    if 0 <= contact_num < len(contacts_list):
        contacts_list[contact_num] = create_contact()  # Перезаписываем контакт
        with open('phonebook.txt', "w", encoding="utf-8") as file:
            file.write('\n\n'.join(contacts_list))
        print("Контакт успешно изменен!")
    else:
        print("Неверный номер контакта.")

def delete_contact():
    """Удаляет контакт из справочника."""
    print_contacts()
    contact_num = int(input("Введите номер контакта для удаления: ")) - 1
    with open('phonebook.txt', "r", encoding="utf-8") as file:
        contacts_list = file.read().rstrip().split('\n\n')
    if 0 <= contact_num < len(contacts_list):
        del contacts_list[contact_num]
        with open('phonebook.txt', "w", encoding="utf-8") as file:
            file.write('\n\n'.join(contacts_list))
        print("Контакт успешно удален!")
    else:
        print("Неверный номер контакта.")

def Interface():
    """Запускает интерфейс телефонного справочника."""
    with open('phonebook.txt', "a", encoding="utf-8"):
        pass

    var = 0
    while var != '6':
        print(
            'Возможные варианты:\n'
            '1. Добавить контакт\n'
            '2. Вывести на экран\n'
            '3. Поиск контакта\n'
            '4. Изменить контакт\n'
            '5. Удалить контакт\n'
            '6. Выход'
            )
        print()
        var = input('Выберите вариант действия: ')
        while var not in ('1', '2', '3', '4', '5', '6'):
            print('Некорректный ввод!')
            var = input('Выберите вариант действия: ')
        print()

        match var: 
            case '1':
                    add_contact()
            case '2':
                    print_contacts()
            case '3':
                    search_contacts()
            case '4':
                print('До свидания')
        print()



if __name__ == '__main__':
    Interface()

