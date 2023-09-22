'''Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать
функционал для изменения и удаления данных и поиска по фамилии.
'''

from os.path import exists
from csv import DictReader, DictWriter


def get_info():
    info = []
    first_name = input('Name: ')
    last_name = input('Last name: ')
    info.append(first_name)
    info.append(last_name)
    flag = False
    while not flag:
        try:
            phone_number = int(input('Phone number: '))
            if len(str(phone_number)) != 11:
                print('wrong number')
            else:
                flag = True
        except ValueError:
            print('not valid number')
    info.append(phone_number)
    return info


def create_file():
    if not exists('phone.csv'):
        with open('phone.csv', 'w', encoding='utf-8') as data:
            f_n_writer = DictWriter(data, fieldnames=['Name', 'Last name', 'Phone number'])
            f_n_writer.writeheader()


def write_file(lst):
    # with open('phone.txt', 'a', encoding='utf-8') as data:
    #     data.write(f'{lst[0]};{lst[1]};{lst[2]}\n')
    with open('phone.csv', 'r+') as f_n:
        f_n_reader = DictReader(f_n)
        res = list(f_n_reader)
        obj = {'Name': lst[0], 'Last name': lst[1], 'Phone number': lst[2]}
        res.append(obj)
        f_n_writer = DictWriter(f_n, fieldnames=['Name', 'Last name', 'Phone number'])
        for el in res:
            f_n_writer.writerow(el)


def read_file(file_name):
    # with open(file_name, encoding='utf-8') as data:
    #     phone_book = data.readlines()
    with open(file_name) as f_n:
        f_n_reader = DictReader(f_n)
        phone_book = list(f_n_reader)
    return phone_book


def record_info():
    lst = get_info()
    write_file(lst)

def search_last_name(last_name, phone_book):
    lst = []
    for info in phone_book:
        if info['Last name'] == last_name:
            lst.append(info)
    return lst

def update_last_name(last_name, new_info, phone_book):
    updated_phone_book = []
    for info in phone_book:
        if info['Last name'] == last_name:
            info.update(new_info)
        updated_phone_book.append(info)
    return updated_phone_book

def delete_last_name(last_name, phone_book):
    new_phone_book = [info for info in phone_book if info['Last name'] != last_name]
    return new_phone_book



def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'r':
            if not exists('phone.csv'):
                print('Файл не создан')
                break
            print(*read_file('phone.csv'))
        elif command == 'w':
            if not exists('phone.csv'):
                create_file()
                record_info()
            else:
                record_info()
        elif command == 's':
            last_name = input("Введите фамилию: ")
            lst = search_last_name(last_name, read_file('phone.csv'))
            if lst:
                print(*lst)
            else:
                print("Нет такой фамилии")
        elif command == 'u':
            last_name = input('Введите фамилию для обновления: ')
            new_info = get_info()
            updated_phone_book = update_last_name(last_name, {'Name': new_info[0], 'Last name': new_info[1], 'Phone number': new_info[2]}, read_file('phone.csv'))
            with open('phone.csv', 'w', encoding='utf-8') as f_n:
                f_n_writer = DictWriter(f_n, fieldnames=['Name', 'Last name', 'Phone number'])
                f_n_writer.writeheader()
                f_n_writer.writerows(updated_phone_book)
        elif command == 'd':
            last_name = input("Введите фамилию для удаления: ")
            updated_phone_book = delete_last_name(last_name, read_file('phone.csv'))
            with open('phone.csv', 'w', encoding='utf-8') as f_n:
                f_n_writer = DictWriter(f_n, fieldnames=['Name', 'Last name', 'Phone number'])
                f_n_writer.writeheader()
                f_n_writer.writerows(updated_phone_book)


main()