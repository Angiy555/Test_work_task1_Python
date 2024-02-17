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
    print('2 - Добавить заметку')
    print('3 - Поиск заметки по дате')
    print('4 - Редактировать заметку')
    print('5 - Удалить заметку')
    print('0 - Выход из программы')
    print(split_line)


def add_new_note():
    """
    Функция запрашивает у пользователя заметку и сохраняет ее в файл
    """
    text_notes = input('Введите текст заметки:\n')
    current_date_time = datetime.datetime.now()
    notes_date = current_date_time.date()
    notes_time = current_date_time.time()
    notes_list= []

    if(os.path.isfile(file_name)):
        notes_list = reader_notes_from_file()
        max_ID = search_maximum_ID(notes_list)
        notes_list.append([max_ID + 1, notes_date, notes_time, text_notes])
        writer_note_to_file(notes_list)
    else:
        notes_list.append([1, notes_date, notes_time, text_notes])
        writer_note_to_file(notes_list)


def show_all():
    """
    Функция выводит заметки на экран
    """
    try:
        notes_list = reader_notes_from_file()
        print_notes_to_console(notes_list)
    except TypeError:
        print('')


def search_note_by_date():
    """
    Функция запрашивает дату поиска и выводит результат поиска
    """
    search_date = input("Введите дату искомой заметки (гггг-мм-дд): ")
    print()
    if not is_correct_format_date(search_date):
        print("Введен не верный формат даты")
        return
    notes_list = reader_notes_from_file()
    found_notes = find_notes_by_date(notes_list, search_date)
    print_notes_to_console(found_notes)


def modify_note():
    """
    Функция выдает список заметок для изменения
    и по выбранному ID записывает новую заметку
    """
    search_date = input("Введите дату искомой заметки (гггг-мм-дд): ")
    print()
    if not is_correct_format_date(search_date):
        print("Введен не верный формат даты")
        return
    notes_list = reader_notes_from_file()
    found_notes = find_notes_by_date(notes_list, search_date)
    print_notes_to_console(found_notes)
    num_note = input('Введите ID записи или 0 для выхода: ')
    if not is_correct_format_range_number(notes_list, num_note):
        print("Введен не верный ID!")
        return
    num = int(num_note)
    if num == 0:
        return
    new_note = input("Введите новую заметку: ")
    number_line = search_line_number_by_ID(notes_list, num)
    notes_list[number_line][3] = new_note
    writer_note_to_file(notes_list)
    print("\n Запись изменена!")


def remove_note():
    """
    Функция выдает список заметок в котором выбирается заметка для удаления
    """
    search_date = input("Введите дату искомой заметки (гггг-мм-дд): ")
    print()
    if not is_correct_format_date(search_date):
        print("Введен не верный формат даты")
        return
    notes_list = reader_notes_from_file()
    found_notes = find_notes_by_date(notes_list, search_date)
    print_notes_to_console(found_notes)
    num_note = input('Введите ID записи для удаления или 0 для выхода: ')
    if not is_correct_format_range_number(notes_list,num_note):
        print("Введен не верный ID!")
        return
    num = int(num_note)
    if num == 0:
        return
    number_line = search_line_number_by_ID(notes_list, num)
    notes_list.pop(number_line)
    writer_note_to_file(notes_list)
    print("\n Запись удалена!")
