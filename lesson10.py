# исключения и их обработка. Исключения - это механизм для обработки заведомо известных ошибок и других возможных
# проблем, во время выполнения программы.
""" a=10
b=0
c=a/b
print (c) # ZeroDivisionError: division by zero
Print('---------------------------------------------------') """
#  Для обработки исключения используется блок try-except
try:
    1 / 0
except:
    print("You can't devide on 0")
print('---------------------------------------------------')
a = 10
b = 20
try:
    c = a / b
except:
    c = 0
    print('Devision on zero')
print(c)
""" Виды исключений
Для того чтобы обработка ошибок была более точечной, можно указывать определенный тип ошибки, который вы ожидаете.
Изначально отлавливаются ошибки типа BaseException, под которые попадают любые ошибки.
Часто встречающиеся виды исключений:
NameError - не найдено переменную с таким именем.
TypeError - неверный тип объекта, к которому применяется операция.
ValueError - ошибка, связанная со значением аргумента.
AssertionError - выражение в функции assert ложно.
ImportError - не удалось импортирование модуля или его атрибута."""


def x():
    a = 10


try:
    print(abc)
except NameError as error:
    print(error)
print('-----------------------------------------------------------')


def x():
    a = 10


try:
    print(abc)
except ValueError as error:
    print(error)
except NameError as error:
    print(error)
print('-----------------------------------------------------------')
try:
    print(int("abc"))
except ValueError as error:
    print(error)
print('-----------------------------------------------------------')
try:
    assert 2 == 3
except AssertionError as error:
    print(error)
print('-----------------------------------------------------------')
x = None
try:
    for elem in x:
        print(elem)
except TypeError as error:
    print(error)
print('-----------------------------------------------------------')
# Задача 1: Реализовать функцию, которая будет принимать на вход номер месяца, вернуть его название иреализовать в нем несколько обработок исключений.


def get_month(number):
    months = {
        1: "Jan",
        2: "Fab",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec"
    }
    try:
        return months[number]
    except KeyError as key_error:
        print(key_error, ", use only nimbers from 1 to 12")
    except TypeError as type_error:
        print(type_error, ", use only nimbers from 1 to 12")


month_name = get_month([1, 2, 3])
print(month_name)
# Задача 2: Нужно проверить, все ли числа в последовательности уникальны и реализовать несколько обработок исключений.


def check(sequence):
    if len(set(sequence)) == len(sequence):
        return True
    return False


def check_sequence_unique(array):
    try:
        return check(array)
    except TypeError as type_error:
        print(type_error, "use only strings, lists orsets")


s = [1, 2, 3, 4]
u = check_sequence_unique(s)
print(u)
print('----------------------------------------------')
def check(sequence):
    if len(set(sequence)) == len(sequence):
        return True
    return False


def check_sequence_unique(array):
    try:
        return check(array)
    except TypeError as type_error:
        print(type_error, "use only strings, lists orsets")


s = False
u = check_sequence_unique(s)
print(u)
