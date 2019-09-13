#!/usr/bin/python3

"""Лото

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

from random import sample
from random import randint

def ticket():
    t = sample(range(1, 91), 15)
    l1 = t[:5];     l1.sort()
    l2 = t[5:10];   l2.sort()
    l3 = t[10:];    l3.sort()

    def _line(l):
        while len(l) < 9:
            l.insert(randint(0, len(l) - 1), ' ')
    _line(l1); _line(l2); _line(l3)

    return [l1, l2, l3]

def out(ticket, mes):
    print('{:-^26}'.format(f' {mes} '))
    for line in ticket:
        for n in line:
            print('{0:>2}'.format(n), end=' ')
        print()
    print('{:-^26}\n'.format('-'))

def cross_out(ticket, barrel):
    _coincidence = False
    for line in ticket:
        if line.count(barrel):
            _coincidence = True
            line[line.index(barrel)] = '-'
    return _coincidence

def ticket_check(ticket):
    c = 0
    for line in ticket:
        c += line.count('-')
    if c == 15:
        return True
    else:
        return False

kegs = sample(range(1, 91), 90)
player_ticket = ticket()
computer_ticket = ticket()

for barrel in kegs:
    out(player_ticket, ' Ваша карточка ')
    out(computer_ticket, ' Карточка компьютера ')

    print(f'Выпал бочёнок: {barrel}')

    while True:
        cross_out_n = input('Зачеркнуть цифру? (y/n): ')
        if cross_out_n == 'y' or cross_out_n == 'n':
            break


    cross_out_f = cross_out(player_ticket, barrel)
    cross_out(computer_ticket, barrel)

    if ticket_check(player_ticket):
        print('Игра окончена, Вы выйграли!')
        break
    elif (ticket_check(computer_ticket) and not ticket_check(player_ticket))\
            or (cross_out_n == 'y' and not cross_out_f)\
            or (cross_out_n == 'n' and cross_out_f):
        print('Игра окончена, Вы проиграли!')
        break