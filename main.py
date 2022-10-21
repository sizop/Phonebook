import csv
import os.path

import import_export_data
import input_data
import menu
import search


def main():
    menu.main_menu('Start')
    while True:
        menu.main_menu('Main')
        value = input('Выберите пункт меню: ')
        if value != '1' and value != '2' and value != '3' and value != '4' and value != '0':
            continue
        value = int(value)
        match value:
            case 1:
                print('=' * 50)
                menu.file_menu()
                value_1 = input('Подтвердите свой выбор ')
                if value_1 == '1':
                    if os.path.exists('phonebook.csv') == True:
                        print('Файл уже существует')
                        continue
                    with open('phonebook.csv', 'w', encoding="utf-8") as file:
                        writer = csv.DictWriter(file, fieldnames=['Фамилия', 'Имя', 'Отчество', 'Телефон'],
                                                lineterminator='\n')
                        writer.writeheader()
                else:
                    continue
            case 2:
                print('=' * 50)
                print('Ввод новой записи')
                print('=' * 50)
                if os.path.exists('phonebook.csv') == False:
                    print('Файл отсутствует. Создайте новый файл. Пункт меню 1')
                    continue
                input_data.input_data()
            case 3:
                print('=' * 50)
                print('Поиск записи')
                print('=' * 50)
                if os.path.exists('phonebook.csv') == False:
                    print('Файл отсутствует. Создайте новый файл. Пункт меню 1')
                    continue
                menu.search_menu()
                value_1 = input('Выберите пункт ')
                if value_1 == '1':
                    search_string = {}
                    name = input('Введите фамилию ')
                    if name.isalpha() == False:
                        print('Введено не верное значение')
                        continue
                    search_string = search.search_data('Фамилия', name)
                elif value_1 == '2':
                    search_string = []
                    name = input('Введите № телефона ')
                    if name.isdigit() == False:
                        print('Введено не верное значение')
                        continue
                    search_string = search.search_data('Телефон', name)
                else:
                    continue
                print(search_string)
            case 4:
                print('=' * 50)
                print('Импорт/экспорт записей')
                print('=' * 50)
                menu.import_export_menu()
                value_1 = input('Выберите пункт ')
                if value_1 == '1':
                    if os.path.exists('phonebook.csv') == False:
                        print('Файл отсутствует. Создайте новый файл. Пункт меню 1')
                        continue
                    import_export_data.export_to_txt()
                elif value_1 == '2':
                    if os.path.exists('phonebook.csv') == False:
                        print('Файл отсутствует. Создайте новый файл. Пункт меню 1')
                        continue
                    import_export_data.import_to_csv()
                else:
                    continue
            case 0:
                break

main()
