import csv
import os
import datetime

def count_notes(file_name: str):
    """
    Функция принимает имя файла  (file_name) в виде строки
    определяет количество строк в файле
    """
    count = 0
    if(os.path.isfile(file_name)):
         with open(file_name, 'r', encoding='utf-8') as fd:
            file_reader = csv.reader(fd, delimiter=";")
            for row in file_reader:
                count += 1
    return count

def print_data(data):
    """
    Функция принимает данные и выводит в консоль
    """
    notes_book = []
    split_line = "=" * 70
    count = 0

    for notes in data:
        if count == 0:
            print(split_line)
            print("ID        Дата          Время               Заметка")
            print(split_line)
        else:
            notes_book.append(
                {
                    "ID": notes[0] ,
                    "notes_id": notes[1],
                    "notes_time": notes[2],
                    "text_notes": notes[3],
                }
            )
        count +=1

    for notes in notes_book:
        notes_id, notes_date, notes_time, text_notes = notes.values()
        print(f"{notes_id :<6} {notes_date:<12} {notes_time:<20} {text_notes:<5}")

    print(split_line)

def format_verification(atribute: str):
    """
    Функция проверки формата даты
    """
    try:
        datetime.datetime.strptime(atribute, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def find(date, atribute: str):
    """
    Функция поиска по дате
    """
    find_notes = []
    find_notes.append({"ID","Дата", "Время", "Заметка"})
    for notes in date:
        if notes[1] == atribute:
            find_notes.append(notes)

    return find_notes

def num_format_ver(count, num: str):
    """
    Функция проверки числа в диапазоне
    """
    try:
        res = int(num)
        if res >= 0 and res < count:
            return True
        else:
            return False
    except ValueError:
        return False