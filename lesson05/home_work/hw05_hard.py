# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) - в Linux начинается с /, в Windows с имени диска
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь. Исходной директорией считать ту,
# в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл (запросить подтверждение операции)")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")
    print("ping - тестовый ключ")


def make_dir(dir_name):
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def ping():
    print("pong")

def cp(_file):
    # не успел!
    pass

def rm(remove):
    try:
        os.remove(remove)
    except OSError:
        print(f'Невозможно удалить "{remove}" !!!')
    else:
        print(f'Успешно удалено "{remove}"!')

def cd(_dir):
    try:
        os.chdir(_dir)
    except OSError:
        print(f'Невозможно перейти в директорию "{_dir}" !!!\n')
    else:
        print(f'Успешно перешел в директорию "{_dir}"!\n')
    finally:
        input('Press Enter to continue...\n')

def ls():
    print(os.getcwd())

do = {
    "help": print_help,
    "ping": ping,
    "ls": ls
}

do_2 = {
    "mkdir": make_dir,
    "cp": cp,
    "rm": rm,
    "cd": cd
}

i = 1
argv = sys.argv
while i < len(argv):
    if do_2.get(argv[i]):
        try:
            do_2[argv[i]](argv[i + 1])
            i += 2
        except IndexError:
            print(f'Необходимо указать аргумент для ключа {argv[i]} !!!\n')
            print_help()
            break
    elif do.get(argv[i]):
        do[argv[i]]()
        i += 1
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
        break