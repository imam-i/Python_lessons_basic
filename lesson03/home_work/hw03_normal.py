# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    golden_ratio = (1 + (5 ** (1 / 2))) / 2
    fn = []
    n = int(n)
    m = int(m)

    # Не совсем понял что имелось в виду "Первыми элементами ряда считать цифры 1 1"
    # **************************************************************************
    # Возможно это:
#    if n > 1 and n < 3:
#        fn.append(1)
#    elif n > 2:
#        fn.append(1)
#        fn.append(1)

    # Или это:
    if n > 1:
        n = 1
    # **************************************************************************

    while n <= m:
        if n > 0:
            fn.append(int(( (golden_ratio ** n) - (- golden_ratio) ** (- n) ) / ( (2 * golden_ratio) - 1 )))
        n += 1

    print(fn)

fibonacci(5, 20)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    b = True
    while b:
        b = False
        i = 0
        while i < len(origin_list) - 1:
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]
                b = True
            i += 1
    return origin_list


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
def my_filter(func,iterable):
    result = []
    i = 0
    while i < len(iterable):
        if func(iterable[i]):
            result.append(iterable[i])
        i += 1
    return result

print(my_filter(lambda x: type(x) == int, [45, 22, -6, 'asfd', 0, 'dfs', '']))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

