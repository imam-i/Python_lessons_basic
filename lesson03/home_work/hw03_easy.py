__author__ = 'Алишаев Имам Курбанмагомедович'

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом)
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math


def my_round(number, ndigits):
    _result = 0
    _integer, _fractional = str(number).split('.')
    if len(_fractional) >= ndigits and int(_fractional[ndigits]) > 5:
        _result = float(_integer + '.' + _fractional[:ndigits])
        _result += (1 / (10 ** ndigits))
    else:
        _result = float(_integer + '.' + _fractional[:ndigits])
    return _result


print(my_round(2.1234567, 5))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    _ticket_number = str(ticket_number)
    _a = 0
    _b = 0
    if len(_ticket_number) != 6:
        return False
    for char_a in _ticket_number[:3]:
        _a += int(char_a)
    for char_b in _ticket_number[3:]:
        _b += int(char_b)
    if _a == _b:
        return True
    else:
        return False


print(lucky_ticket(976679))