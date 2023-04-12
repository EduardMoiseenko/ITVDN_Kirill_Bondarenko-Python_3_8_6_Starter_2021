# Функции - объект, который принимает и возвращает значение. def my_function(): - синтаксис объявления функции
def print_sum():
    print(2 + 2)


# Для вызова функции нужно указать ее имя,а после ()
print_sum()
print("----------------------------------------")


def print_value():
    print('Hello')


print(print_value)
print_value()
""" Поведение функции можно менять. Для этого нужно передавать в нее параметры, которые будут дальше использоваться в коде.
Для этого пропишите в скобках название параметра и используйте это название в своей логике в теле функции """


def print_message(msg):
    print(msg)


print_message('Hello!!!')
print_message('Hi')


def func(a):
    print(a * 3)


func(3)


def func(a, b, c):
    print(a + b + c)


func(3, 2, 5)


# Для того чтобы вернуть результат функции, нужно воспользоваться специальным словом return
def sum_two_numbers(a, b):
    return a + b


sum_two_numbers(12, 2)
result = sum_two_numbers(10, 1)
print(result)
print("----------------------------------------")


def function(a, b):
    return a+b


result = function(2, 5)
result2 = function(10, 45)
print(result)
print(result2)
print("----------------------------------------")

# Задача 1: Найдите максимальное значение в передаваемом в функцию списке и верните его, если оно больше 0, в ином сучае верните сообщение о том, что число меньше 0.


def get_max_from_list(list_values):
    max_value = list_values[0]
    for element in list_values:
        if element > max_value:
            max_value = element
    return max_value if max_value > 0 else 'Max value is less then zero'


a = [1, 3, 56, 45, 0]
max_a = get_max_from_list(a)
print(max_a)
a2 = [-1, -3, -56, -45]
max_a2 = get_max_from_list(a2)
print(max_a2)
print("----------------------------------------")
# Задача 2: Верните количество букв в слове, которое передается в параметрах


def get_string_length(string):
    return len(string)


string_a = 'hello'
string_b = 'bye'
len_a = get_string_length(string_a)
len_b = get_string_length(string_b)
print('Str a has', len_a, 'characters')
print('Str a has', len_b, 'characters')

# Задача 3: Напишите функцию, которая возводит в степень число, которое передается в параметрах, если степень не отрицательная. Первый параметр - число, второй - степень, в которую его нужно возвести.


def power(value, value_power):
    if value_power >= 0:
        return value ** value_power


two_in_power_of_ten = power(2, 0)
print(two_in_power_of_ten)
