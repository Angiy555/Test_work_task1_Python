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

def is_format_verification(atribute: str):
    """
    Функция проверки формата даты
    """
    try:
        datetime.datetime.strptime(atribute, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def is_num_format_ver(count, num: str):
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

def find_notes(file_name: str, atribute: str):
    """
    Функция поиска по дате
    """
    try:
        with open(file_name, 'r',encoding='utf-8') as fd:
            file_reader = list(csv.reader(fd, delimiter=";"))
            find_notes = []
            find_notes.append({"ID","Дата", "Время", "Заметка"})
            for notes in file_reader:
                if notes[1] == atribute:
                    find_notes.append(notes)
            if len(find_notes) < 2:
                print('Такой записи нет в заметках')
                return
            print_data(find_notes)
            return file_reader
    except FileNotFoundError:
        print('Файла с записями не найдено.')

def recording_changes(file_name: str, data):
    with open(file_name, 'w', encoding='utf-8') as fd:
        name_header = ["ID","Дата", "Время", "Заметка"]
        file_writer = csv.DictWriter(fd, delimiter=";", lineterminator="\r", fieldnames=name_header)
        count = 0
        for note in data:
            if count == 0:
                file_writer.writeheader()
            else:
                file_writer.writerow({"ID": count,"Дата": note[1], "Время": note[2], "Заметка": note[3]})
            count += 1



