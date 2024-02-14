import os
from interface import *
os.system('CLS')


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
            show_all(file_name)
        elif answer == '2':
            os.system('CLS')
            add_new(file_name)
        elif answer == '3':
            os.system('CLS')
            find_by_atribute(file_name)
        elif answer == '4':
            modify_data(file_name)
        elif answer == '5':
            remove_data(file_name)
        elif answer == '0':
           flag_exit = True
        input("\n--- нажмите enter для продолжения ---")

if __name__ == '__main__':
    main()