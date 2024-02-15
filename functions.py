import csv
import os
import datetime

file_name = 'notes.csv'

def reader_notes_from_file():
    """
    Функция чтения фала формата csv передающая на выход list без заголовка
    """
    try:
        with open(file_name, 'r',encoding='utf-8') as csv_file:
            reader_notes = csv.reader(csv_file, delimiter=";")
            notes_list = list(reader_notes)
            notes_list.pop(0)
            return notes_list
    except FileNotFoundError:
        print('Файла с записями не найдено.')


def writer_note_to_file(notes_list):
    """
    Функция записи list в фала формата csv
    """
    with open(file_name, 'w', encoding='utf-8') as csv_file:
        name_header = ["ID","Дата", "Время", "Заметка"]
        file_writer = csv.DictWriter(csv_file, delimiter=";", lineterminator="\r", fieldnames=name_header)
        file_writer.writeheader()
        for row in notes_list:
            file_writer.writerow({"ID": row[0],"Дата": row[1], "Время": row[2], "Заметка": row[3]})


def print_notes_to_console(notes_list):
    """
    Функция принимает list и выводит в консоль
    """
    split_line = "=" * 70

    print(split_line)
    print("ID        Дата          Время               Заметка")
    print(split_line)

    for notes in notes_list:
        print(f"{notes[0] :<6} {notes[1]:<12} {notes[2]:<20} {notes[3]:<5}")

    print(split_line)


def is_correct_format_date(atribute: str):
    """
    Функция проверки формата даты
    """
    try:
        datetime.datetime.strptime(atribute, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def is_correct_format_range_number(notes_list, number_note_string: str):
    """
    Функция проверки числа в диапазоне
    """
    try:
        number_note = int(number_note_string)
        for row in notes_list:
            if int(row[0]) == number_note:
                return True
        return False
    except ValueError:
        return False


def find_notes_by_date(notes_list, atribute: str):
    """
    Функция поиска по дате
    """
    found_notes = []
    for note in notes_list:
        if note[1] == atribute:
            found_notes.append(note)
    if len(found_notes) < 1:
        print('Записи с такой датой нет в заметках')
        return
    return found_notes


def search_line_number_by_ID(notes_list, number_ID):
    count = 0
    number_line = 0
    for row in notes_list:
        if int(row[0]) == number_ID:
            number_line = count
        count += 1
    return number_line


def search_maximum_ID(notes_list):
    max_ID = 0
    for row in notes_list:
        if int(row[0]) > max_ID:
            max_ID = int(row[0])
    return max_ID