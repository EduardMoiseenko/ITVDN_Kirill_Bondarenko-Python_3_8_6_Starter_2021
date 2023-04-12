# Списки и срезы. Списки - это упорядоченные коллекции объектов различных типов.
my_list = list('abcd')
print(my_list)
print(my_list[0])
my_list1 = ['a', 35, False, 'd']
print(my_list1)
print('--------------------------------------------')
""" Для того что бы использовать выборку более чем по одному элементу, можно исползовать срезы, которые вернут подмножество элементов списка. Как выглядит срез:
my_list[start:stop:step]
где start - индекс, с которого начинается подмножество, stop - индекс, перед которым закончится подмножество, step - шаг выбора элементов. """
print(my_list[0:1])
print(my_list[0:5])
print(my_list[0:5:2])
print('--------------------------------------------')
my_list2 = [1, 2, 3, 4, 5]
print(my_list2[0:3:2])
# Методы списков
# append() - добавление нового элемента в конец списка
my_list3 = [1]
my_list3.append('new_element')
print(my_list3)
# clear() - удалить все элементы списка
my_list4 = [1, 2, 3]
my_list4.clear()
print(my_list4)
print('--------------------------------------------')
a = [1, 2, 3]
a.append(5)
print(a)
print('--------------------------------------------')
a = [1, 2, 3]
a.clear()
print(a)
print('--------------------------------------------')
# extend() - расширяет список переданой последовательностью
first_list = [1, 2, 3]
second_list = [4, 5, 6]
first_list.extend(second_list)
print(first_list)
# index() - возвращает index указанного элемента, если таких элементов несколько - вернет первый найденный
my_list5 = [1, 2, 3]
print(my_list5.index(1))
print('--------------------------------------------')
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)
print(a.index(4))
print('--------------------------------------------')
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)
print(a)
print('--------------------------------------------')
a = [1, 2, 3]
b = [4, 5, 6]
a = a + b
print(a)
print('--------------------------------------------')
# pop() - удаляет элемент указанного индекса и вовзращает его
my_list = [1, 2, 3]
removed_element = my_list.pop(0)
print(removed_element)
print(my_list)
# reverse() - зеркально отображает список
print('--------------------------------------------')
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)
print('--------------------------------------------')
a = [1, 2, 3, 4]
removed_element = a.pop(3)
print(a)
print(removed_element)
print('--------------------------------------------')
a = [1, 2, 3, 4]
a.reverse()
print(a)
print('--------------------------------------------')
# sort() - сортирует список. Если указать в параметрах reverse=True, тогда сортировка будет в обратном порядке
my_list = [2, 1, 4, 5, 6, 3]
my_list.sort()
print(my_list)
print('--------------------------------------------')
my_list = [2, 1, 4, 5, 6, 3]
my_list.sort(reverse=True)
print(my_list)
print('--------------------------------------------')
a = [2, 1, 4, 5, 6, 3]
a.sort()
print(a)
print('--------------------------------------------')
a = [2, 1, 4, 5, 6, 3]
a.sort(reverse=True)
print(a)
print('--------------------------------------------')
# Обход списков
for elem in my_list:
    print(elem)
print('--------------------------------------------')
my_list = [4, 3, 2, 1]
print(my_list)
for element in my_list:
    print(element)
print('--------------------------------------------')
# Задача: наути и удалить все четные элементы списка
my_list = [1, 2, 3, 4, 5, 6]
for list_elemet in my_list:
    if list_elemet % 2 == 0:
        print(list_elemet)
print('--------------------------------------------')
my_list = [1, 2, 3, 4, 5, 6]
even_list = []
for list_elemet in my_list:
    if list_elemet % 2 == 0:
        even_list.append(list_elemet)
        print(even_list)
        print(my_list)
print('--------------------------------------------')
# задача: Возвести все элементы списка в квадрат
my_list = [2, 4, 6, 8]
squares_list = []
for list_elemet in my_list:
    squares_list.append(list_elemet**2)
    print(squares_list)
print('--------------------------------------------')
# Задача: Найти максимальный элемент списка
x = [3, 2, 1, 7, 0, -3, 25, -78, 45, 100, -1, 10]
max_element = x[0]
for element in x:
    if element > max_element:
        max_element = element
        print(max_element)
