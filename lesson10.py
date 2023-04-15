# исключения и их обработка. Исключения - это механизм для обработки заведомо известных ошибок и других возможных проблем, во время выполнения программы.
""" a=10
b=0
c=a/b
print (c) # ZeroDivisionError: division by zero
Print('---------------------------------------------------') """
#  Для обработки исключения используется блок try-except
try:
  1/0
except:
  print("You can't devide on 0")
print('---------------------------------------------------')
a=10
b=20
try:
  c=a/b
except:
  c=0
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

