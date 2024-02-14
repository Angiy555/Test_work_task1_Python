import csv
import os
import datetime
from functions import *

def draw_interface ():
    """
    Функция рисования меню
    """
    split_line = "=" * 45
    print('#########          ЗАМЕТКИ          #########')
    print(split_line)
    print('########            МЕНЮ            #########')
    print(split_line)
    print('1 - Показать список заметок')
    print('2 - Добавить добавить заметку')
    print('3 - Поиск заметки по дате')
    print('4 - Редактировать заметку')
    print('5 - Удалить заметку')
    print('0 - Выход из программы')
    print(split_line)

def add_new(file_name: str):
    """
    Функция принимает имя файла  (file_name) в виде строки
    запрашивает у пользователя данные
    """
    text_notes = input('Введите текст заметки:\n')
    current_date_time = datetime.datetime.now()
    notes_date = current_date_time.date()
    notes_time = current_date_time.time()
    count = count_notes(file_name)

    #Открытие файла и запись в него данных в конце файла
    name_header = ["ID","Дата", "Время", "Заметка"]
    if(os.path.isfile(file_name)):
        with open(file_name, 'a', encoding='utf-8') as fd:
            file_writer = csv.DictWriter(fd, delimiter=";", lineterminator="\r", fieldnames=name_header)
            file_writer.writerow({"ID": count,"Дата": notes_date, "Время": notes_time, "Заметка": text_notes})
    else:
        with open(file_name, 'a', encoding='utf-8') as fd:
            file_writer = csv.DictWriter(fd, delimiter=";", lineterminator="\r", fieldnames=name_header)
            file_writer.writeheader()
            file_writer.writerow({"ID": count + 1,"Дата": notes_date, "Время": notes_time, "Заметка": text_notes})

def show_all(file_name: str):
    """
    Функция принимает имя файла  (file_name) в иде строки
    и выводит заметки на экран
    """
    try:
        with open(file_name, 'r',encoding='utf-8') as fd:
            file_reader = csv.reader(fd, delimiter=";")
            print_data(file_reader)
    except FileNotFoundError:
        print('Файла с записями не найдено.')

def find_by_atribute(file_name:str):
    """
    Функция принимает имя файла  (file_name) в виде строки
    запрашивает атрибут поиска и выводит результат поиска
    """
    atribute = input("Введите дату искомой заметки (гггг-мм-дд): ")
    print()
    if format_verification(atribute):
        try:
            with open(file_name, 'r',encoding='utf-8') as fd:
                file_reader = csv.reader(fd, delimiter=";")
                find_reader = find(file_reader, atribute)
                if len(find_reader) > 1:
                    print_data(find_reader)
                else:
                    print('Такой записи нет в заметках')
        except FileNotFoundError:
            print('Файла с записями не найдено.')
    else:
        print("Введен не верный формат даты")

def modify_data(file_name):
    """
    Функция принимает имя файла  (file_name) в виде строки
    выдает список заметок для изменения
    и запрашивает новые данные
    """
    atribute = input("Введите дату искомой заметки (гггг-мм-дд): ")
    print()
    if not format_verification(atribute):
        print("Введен не верный формат даты")
        return
    try:
        with open(file_name, 'r',encoding='utf-8') as fd:
            file_reader = list(csv.reader(fd, delimiter=";"))
            find_reader = find(file_reader, atribute)
            if len(find_reader) < 2:
                print('Такой записи нет в заметках')
                return
            print_data(find_reader)
            num_notes = input('Введите ID записи или 0 для выхода: ')
            if not num_format_ver(len(file_reader),num_notes):
                print("Введен не верный ID!")
                return
            num = int(num_notes)
            if num == 0:
                return
            new_notes = input("Введите новую заметку: ")
            file_reader[num][3] = new_notes
            with open(file_name, 'w', encoding='utf-8') as fd:
                name_header = ["ID","Дата", "Время", "Заметка"]
                file_writer = csv.DictWriter(fd, delimiter=";", lineterminator="\r", fieldnames=name_header)
                count = 0
                for note in file_reader:
                    if count == 0:
                        file_writer.writeheader()
                    else:
                        file_writer.writerow({"ID": note[0],"Дата": note[1], "Время": note[2], "Заметка": note[3]})
                    count += 1
                print("\n Запись изменена!")
    except FileNotFoundError:
        print('Файла с записями не найдено.')

def remove_data(file_name):
    """
    Функция принимает имя файла  (file_name) в виде строки
    выдает список заметок в котором выбирается заметка для удаления
    """
    atribute = input("Введите дату искомой заметки (гггг-мм-дд): ")
    print()
    if not format_verification(atribute):
        print("Введен не верный формат даты")
        return
    try:
        with open(file_name, 'r',encoding='utf-8') as fd:
            file_reader = list(csv.reader(fd, delimiter=";"))
            find_reader = find(file_reader, atribute)
            if len(find_reader) < 2:
                print('Такой записи нет в заметках')
                return
            print_data(find_reader)
            num_notes = input('Введите ID записи для удаления или 0 для выхода: ')
            if not num_format_ver(len(file_reader),num_notes):
                print("Введен не верный ID!")
                return
            num = int(num_notes)
            if num == 0:
                return
            file_reader.pop(num)
            with open(file_name, 'w', encoding='utf-8') as fd:
                name_header = ["ID","Дата", "Время", "Заметка"]
                file_writer = csv.DictWriter(fd, delimiter=";", lineterminator="\r", fieldnames=name_header)
                count = 0
                for note in file_reader:
                    if count == 0:
                        file_writer.writeheader()
                    else:
                        file_writer.writerow({"ID": count,"Дата": note[1], "Время": note[2], "Заметка": note[3]})
                    count += 1
                print("\n Запись удалена!")
    except FileNotFoundError:
        print('Файла с записями не найдено.')
