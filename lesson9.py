""" Область видимости функции
Область видимости - это область, в которой интерпретиатору доступны ваши переменные, функции и прочее. Область видимости бывает локальная и глобальная.
Переменные, которые объявлены вне функции, называются глобальными переменными в Python. Эти переменные имеют большую область видимости и доступны всем функция,
которые определены после объявления глобальной переменной.
Когда переменная объявляется внутри функции, то это локальная переменная. Область действия локальной переменной ограничена функцией, в которой она создается."""
# Global - глобальная область видимости
x = 1


def print_x():
    print(x)


print_x()
print('--------------------------------------------')
# Local - локальная область видимости


def print_local_y():
    y = 1
    print(y)


print_local_y()
print('--------------------------------------------')
x = 1
print(x)


def print_x():
    print(x)


print_x()
print('--------------------------------------------')


def print_x():
    x = 10
    print(x)


print_x()
print('--------------------------------------------')


def get_x():
    x = 10
    return x


x_from_local = get_x()
print(x_from_local)
print('--------------------------------------------')
""" Вложенные функции
Функции можно объявлять и вызывать внутри друг друга. Это может быть поле, если вы хотите чтобы функция было доступна только в локальной области видимости другой функции."""


def external():
    def internal():
        return 1
    print(internal())


external()
# internal()
print('--------------------------------------------')


def main():
    x = 10

    def internal():
        return 1
    internal_result = internal()
    return x+internal_result


m = main()
print(m)
""" Стандартные функции в Python:
print -функуия для вывода сообщения в консоль
len - функция, которая возвращает длину объекта"""
print('Hello')
print(len([1, 2, 3]))
print(len('abc'))
print(5+5)
print('--------------------------------------------')
""" Стандартные функции в Python:
Функции преобразования типов - нужны для того, чтобы можно было создавать новые объекты определенного типа.
str - преобразование в строку
int - преобразование в целое число
float - преобразование в не целое число
list - преобразование в список
dict - преобразование в словарь
set - преобразование в множество
tuple - преобразование в кортеж
bool - преобразование в True/False """
x = 1
print(str(x))
x_str = str(x)
print(type(x))
print(type(x_str))
x = '123'
x_int = int(x)
print(type(x_int))
x = '123'
x_float = float(x)
print(type(x_float))
x = {}
print(bool(x))
print('--------------------------------------------')
""" Стандартные функции в Python:
sum - возвращает сумму набора чисел.
min и max - возвращает минимум и максимум из набора чисел соответственно."""
print(sum([1,2,3]))
print(min([1,2,3]))
print(max([1,2,3]))
x=[1,2,3,4,5]
print(sum(x))
print(sum(x)/len(x))
print(min(x),max(x))
""" Анонимные функции - используются в случае. если нам их нужно куда-то передать и больше мы не будем их использовать повторно.
Такая запись будет компактнее. У такой функции не будет имени. Синтаксис: lambda x:x
Где первый х - это параметр, который передается в функцию, а второй - то, что возвращается.
Эквивалент обычной функции:
def some_name(x):
  return x
  """
my_list=[1,2,3,5,4]
my_list.sort(key=lambda x: -x)
print(my_list)
print('--------------------------------------------')
x=[1,2,3,4,5]
def make_smth(function):
    for element in x:
        print(function(element))
make_smth(lambda a: a+10)
