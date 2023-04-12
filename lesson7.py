""" Словари - это упорядоченные коллекции формата ключ-значение. Значением может быть любой объект,
ключом может быть только неизменяемый объект.
Синтаксис словарей: {'key':'value'}
где key - это ключ, по которому доступен элемент value.
Для того что бы получить наше значение по ключу, достаточно после названия словаря в квадратных скобках указать название ключа.
Также можно использовать метод  get(), который в случае отсутствия элемента по такому ключу вернет None """
my_dict = {
    'key': 'value'
}
print(my_dict['key'])
print(my_dict.get('key'))
print('-----------------------------------------')
my_dict = {
    'key': 'value',
    10: True,
    0.2: 'hello'
}
print(my_dict)
print(my_dict[0.2])
# print(my_dict[value]) # NameError: name 'value' is not defined. Did you mean: 'False'?
print(my_dict.get(55))
print(my_dict.get('key'))
print(my_dict.get('key', -1))
print(my_dict.get('key2', -1))
print('-----------------------------------------')
# clear() - очищает словарь
my_dict = {
    'key': 'value'
}
my_dict.clear()
print(my_dict)
print('-----------------------------------------')
# items() - возвращает пару ключ-значение
my_dict = {
    'key': 'value'
}
my_dict.items()
# my_dict_items([('key', 'value')])
# print(my_dict_items)
print('-----------------------------------------')
d = {
    1: 10,
    2: 20
}
print(d.items())
print('-----------------------------------------')
# pop(key) - удаляет ключ и возвращает соответствующее ему значение
my_dict = {
    'key': 'value'
}
print(my_dict.pop('key'))
# popitem() - удаляет последнее значение и возвращает его в формате ключ-значение
my_dict = {
    'key': 'value',
    'key2': 'value2'
}
print(my_dict.popitem())
print(my_dict)
print('-----------------------------------------')
d = {
    '1': 'world',
    '2': 'a'
}
print(d)
d.pop('1')
print(d)
d = {
    '1': 'world',
    '2': 'a'
}
print(d.pop('1'))
print(d.popitem())
print(d)
print('-----------------------------------------')
# update({'key':'value'}) - добавляет новое ключ-значение
my_dict = {}
my_dict.update({'key': 'value'})
print(my_dict)
# values() - возвращает все значения в словаре
my_dict = {
    'key': 'value',
    'key2': 'value2'
}
my_dict.values()
# dict_values(['value','value2'])
print('-----------------------------------------')
d = {
    1: 3,
    2: 4,
    5: 2
}
d.update({6: 30})
print(d)
print('-----------------------------------------')
d = {
    1: 3,
    2: 4,
    5: 2
}
d1 = {
    55: 6,
    45: 3
}
d.update({6: 30})
d.update(d1)
print(d)
print('-----------------------------------------')
# Задача 1: Посчитать с помощью словаря сколько раз элемент повторяется в списке
my_list = [1, 1, 1, 1, 1, 2, 2, 2, 4, 5, 6, 6, 6, 6, 7, 7, 7, 7]
value_to_count = 5
count_dict = {value_to_count: 0}
for element in my_list:
    if element == value_to_count:
        count_dict[value_to_count] += 1
print(count_dict)
print('-----------------------------------------')
my_list = [1, 1, 1, 2, 2, 2, 4, 5, 6, 6, 6, 6, 7, 7, 7, 7]
count_dict = {}
for element in my_list:
    if element in count_dict:
        count_dict[element] += 1
    else:
        count_dict[element] = 1
print(count_dict)
for key, value in count_dict.items():
    print("Key:", key, "count", value)
# Задача 2: Пройтись по слвоарю и вывести все значения, у которых четный ключ
d = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
for number, number_val in d.items():
    if number % 2 == 0:
        print(number, number_val)
# Задача 3:Удалить все ключи, значения которых начинаются с буквы а
d = {
    'alice': 35,
    'mark': 25,
    'april': 45,
    'john': 19
}
new_d = {}
for name, age in d.items():
    if name[0] != 'a':
        new_d[name] = age
print(d)
print(new_d)
