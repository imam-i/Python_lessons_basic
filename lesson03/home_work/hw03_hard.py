# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате: n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (все выражение вводится целиком в виде строки)
# Вывод: 1 17/42 (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3

# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

def fileToDict(file):
    # ***********************************************************
    _dict = []
    _file = open('./data/' + file, 'r', encoding='UTF-8')
    _file_key = []
    for _line in _file:

        # Заголовки массива file
        if len(_file_key) == 0:
            _file_key = _line.split()
            continue

        # Значения массива file
        i = 0
        _vars = _line.split()
        _vars_str = {}
        while i < len(_vars) and len(_vars) == len(_file_key):
            _vars_str[_file_key[i]] = _vars[i]
            i += 1
        _dict.append(_vars_str)

    _file.close()
    return _dict
    # ***********************************************************

workers = fileToDict('workers')
hours_of = fileToDict('hours_of')

for _hours_of in hours_of:
    _name_h = _hours_of['Имя']
    _surname_h = _hours_of['Фамилия']
    _hours_worked = int(_hours_of['Отработано_часов'])

    for _workers in workers:
        _name_w = _workers['Имя']
        _surname_w = _workers['Фамилия']
        _watch_rate = int(_workers['Норма_часов'])
        _salary = int(_workers['Зарплата'])
        if _workers.get('час_работы') == None:
            _hour_of_work = _workers['час_работы'] = round(_salary / _watch_rate, 2)

        if _name_w == _name_h and _surname_w == _surname_h:
            if _hours_worked < _watch_rate:
                _hours_of['К_выплате'] = _hours_worked * _hour_of_work
            elif _hours_worked == _watch_rate:
                _hours_of['К_выплате'] = _salary
            else:
                _pererabotka = _hours_worked - _watch_rate
                _hours_of['К_выплате'] = _salary + ((2 * _pererabotka) * _hour_of_work)

for itm in hours_of:
    print(itm)


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
