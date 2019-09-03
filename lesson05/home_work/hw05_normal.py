# Задача-1:
# Напишите небольшую консольную утилиту, позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел", "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций, и импортированные в данный файл из easy.py

from os import getcwd
from os import chdir

from lesson05.home_work.hw05_easy import ls_dir
from lesson05.home_work.hw05_easy import create_dir
from lesson05.home_work.hw05_easy import remove_dir

def Menu_1():
    _dir = input('Введите имя директории: ')
    try:
        chdir(_dir)
    except OSError:
        print(f'Невозможно перейти в директорию "{_dir}" !!!\n')
    else:
        print(f'Успешно перешел в директорию "{_dir}"!\n')
    finally:
        input('Press Enter to continue...\n')

def Menu_2():
    _dir = getcwd()
    print(f'\nСодержимое директории "{_dir}":')
    ls_dir(_dir)
    input('Press Enter to continue...\n')

def Menu_3():
    _dir = input('Введите имя директории: ')
    remove_dir(_dir)

def Menu_4():
    _dir = input('Введите имя директории: ')
    create_dir(_dir)

while True:
    Menu = {1: 'Перейти в папку',
            2: 'Просмотреть содержимое текущей папки',
            3: 'Удалить папку',
            4: 'Создать папку'}

    for i, itm in Menu.items():
        print(f'{i}.\t{itm}')

    menu_n = input('\nВыберите действие: ')
    menu_n = int(menu_n) if menu_n.isdigit() else 0

    if menu_n == 1:
        Menu_1()
    elif menu_n == 2:
        Menu_2()
    elif menu_n == 3:
        Menu_3()
    elif menu_n == 4:
        Menu_4()
    else:
        print('Выбрана не сушествуюшая комманда!')