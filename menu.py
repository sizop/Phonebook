def main_menu(value):
    match value:
        case 'Start':
            print('Здравствуйте')
            print('=' * 50)
        case 'Main':
            print('Варианты работы программы')
            print('1. Создать новый файл')
            print('2. Внести запись')
            print('3. Найти запись')
            print('4. Импорт/экспорт записей')
            print('0. Выход из программы')
            print('Любой другой знак. Возврат в основное меню')
            print('=' * 50)


def search_menu():
    print('=' * 50)
    print('Варианты поиска')
    print('1. Найти по фамилии')
    print('2. Найти найти по № телефона')
    print('Любой знак. Возврат в основное меню')
    print('=' * 50)


def import_export_menu():
    print('=' * 50)
    print('Варианты')
    print('1. Экспорт из csv в txt файл')
    print('2. Импорт из txt в csv файл')
    print('Любой знак. Возврат в основное меню')
    print('=' * 50)


def file_menu():
    print('=' * 50)
    print('Варианты')
    print('1. Подтвердите свой выбор')
    print('Любой знак. Возврат в основное меню')
    print('=' * 50)
