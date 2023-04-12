# Множества и кортежи
# Множества - это структура данных, не содержащая повторяющихся элементов. Синтаксис множества {1,2,5,4}
a = {1, 2, 2, 3, 4, 4, 4, 4, 4}
print(a)
# Методы множеств
# clear() - очищает множество
my_set = {1, 2, 3, 4, 5}
my_set.clear()
print(my_set)
print('-------------------------------------------')
a = {1, 2, 3, 4, 5, 6}
a.clear()
print(a)
# pop() - удаляет первый элемент множества
my_set = {1, 4, 2, 4, 3}
my_set.pop()
print(my_set)
print('-------------------------------------------')
a = {1, 2, 3, 4, 5, 6}
a.pop()
a.pop()
print(a)
# discard(elem) - удаляет элемент из множества
my_set = {1, 2, 3, 4}
my_set.clear()
print(my_set)
print('-------------------------------------------')
a = {1, 2, 3}
a.discard(3)
print(a)
# remove(elem) - удаляет элемент из множества. Если такого элемента нет,то выдает ошибку
my_set = {1, 2, 5, 4, 3}
my_set.pop()
print(my_set)
print('-------------------------------------------')
""" a = {1, 2, 3}
a.remove(4) # выдаст ошибку так как такого элемента нет в множестве
print(a) """
# add(elem) - добавляет элемент во множество
my_set = {1, 4, 2, 3}
my_set.add(100)
print(my_set)
print('-------------------------------------------')
a = {1, 3, 5, 2}
print(a)
a.add(6)
print(a)
a.add(3)
print(a)
print('-------------------------------------------')
# union(another_set) - объединяет множества
first_set = {1, 2, 3}
second_set = {4}
print(first_set.union(second_set))
print('-------------------------------------------')
a = {1, 2, 3}
b = {4, 5, 6, 7}
c = a.union(b)
print(c)
# intersection(another_set) - находит пересечение двух множеств
first_set = {1, 2, 3}
second_set = {4, 3}
print(first_set.intersection(second_set))
print('-------------------------------------------')
a = {1, 2, 3}
b = {4, 5, 6, 7}
c = a.intersection(b)
print(c)
print('-------------------------------------------')
a = {1, 2, 3}
b = {3, 4, 5}
c = a.intersection(b)
print(c)
print('-------------------------------------------')
# difference(another_set) - разница множеств
first_set = {1, 2, 3}
second_set = {4, 3}
answer = first_set.difference(second_set)
print(answer)
print('-------------------------------------------')
a = {1, 2, 3, 4}
b = {3, 4}
answer = a.difference(b)
answer1 = b.difference(a)
print(answer)
print(answer1)
# elem in set_name - находится ли элемент в множестве
my_set = {1, 4, 2, 3}
answer = 4 in my_set
print(answer)
print('-------------------------------------------')
a = {1, 2, 3, 4}
answer = 3 in a
print(answer)
answer1 = 10 in a
print(answer1)
# Кортеж (tuple) - это неизменяемый список. Синтаксис кортежей: (1,2,3) или (1,).
new_tuple = (1,)
print((1, 2, 3))
print('-------------------------------------------')
a = (1, 2, 3, 4)
print(a)
""" Кортежам свойственны все методы списков, не изменяющие его. Очень часто встречается случай использования кортежей для того, чтобы поменять элементы местами.
Для этого достаточно прописать: a, b = b, a """
a = 1
b = 2
a, b = b, a
print(a)
print(b)
print('-------------------------------------------')
a = (1, 2)
x, y = a
print(x)
print(y)
x, y = y, x
print(x)
print(y)
print('-------------------------------------------')
""" Также, при прохождении по списку кортежей, цикл for может принимать столько значений, сколько элементов в tuple.
Синтаксис: for elem1, elem2 in [(1,2),(2,4)] """
for elem1, elem2 in [(1, 2), (2, 4)]:
    print(elem1, elem2)
print('-------------------------------------------')
a = [(1, 2, 3), (3, 4, 5)]
for first, second, third in a:
    print(first, second, third)
