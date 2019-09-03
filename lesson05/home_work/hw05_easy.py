# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке, из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Создание директории
def create_dir(_dir):
    from os import makedirs
    try:
        makedirs(_dir)
    except OSError as ex:
        print(f'Невозможно создать {_dir} !!!')
    else:
        print(f'Успешно создано {_dir}!')
    finally:
        input('Press Enter to continue...\n')

# Удаление директории
def remove_dir(_dir):
    from os import rmdir
    try:
        rmdir(_dir)
    except OSError:
        print(f'Невозможно удалить "{_dir}" !!!')
    else:
        print(f'Успешно удалено "{_dir}"!')
    finally:
        input('Press Enter to continue...\n')

# Проверка:
# *************************************************
from sys import path
from os.path import join

for i in range(1, 10):
    dir_i = join(path[0], 'dir_' + str(i))
#    create_dir(dir_i)
#    remove_dir(dir_i)
# *************************************************

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Вывод всех директорий в указанной директории
def ls_dir(_path):
    from os import listdir
    from os.path import isdir
    try:
        for _dir in listdir(_path):
            # Подозреваю что выводить нужно всё содержимое директории а не только директории
#            if isdir(_dir):
                print(_dir)
    except OSError as ex:
        print(ex)

# Проверка:
# *************************************************
from os import getcwd

#ls_dir(getcwd())
# *************************************************

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

# Копирование файла
def cp_file(_file, _file_new):
    from shutil import copyfile
    try:
        copyfile(_file, _file_new)
    except OSError as ex:
        print(ex)

# Проверка:
# *************************************************
from sys import argv
from os.path import dirname
from os.path import basename

#cp_file(argv[0], join(dirname(argv[0]), basename(argv[0]) + '_new'))
# *************************************************