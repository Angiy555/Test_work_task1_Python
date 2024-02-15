import os
from interface import *

def main():
    """
    Основная функция
    """
    file_name = 'notes.csv'
    flag_exit = False
    while not flag_exit:
        os.system('CLS')
        draw_interface()
        answer = input('Введите операцию от 1 до 5 или 0 для выхода: ')
        if answer == '1':
            os.system('CLS')
            show_all()
        elif answer == '2':
            os.system('CLS')
            add_new_note()
        elif answer == '3':
            os.system('CLS')
            search_note_by_date()
        elif answer == '4':
            modify_note()
        elif answer == '5':
            remove_note()
        elif answer == '0':
           flag_exit = True
        input("\n--- нажмите enter для продолжения ---")

if __name__ == '__main__':
    main()