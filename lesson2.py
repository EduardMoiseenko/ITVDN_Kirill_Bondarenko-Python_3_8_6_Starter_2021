# import keyword
apples = 10
var_2 = 10000
print(id(apples))
print(id(var_2))

""" keyword.kwlist
and = 5
True = False """

# Строки
a = 'Hello'
b = "Hello"
c = '''Hello world'''
c1 = '''Hello
world'''
d = """Hello
world"""
print(a)
print(b)
print(c)
print(c1)
print(d)

# a = 'This is John's ball' # Между одинарными кавычками нельзя использовать кавычки, так как они будут означать закрывающую кавычку строки, а не сам символ кавычки
# Между одинарными кавычками можно использовать двойные кавычки, так как строка начиналась с одинарной кавычки и двойная кавычка не означает закрытие строки
a = 'This is "project" for me'
print(a)

# Дублирование и конкатенация строк
a = "Hello "
b = "world"
c = a + b
print(c)
print(a * 3)
print(a * 50)

# Методы строк
print(len(a))  # Длинна строки учитывая пробелы

print(a.upper())  # Перевод строки в верхний регистр
print(a.lower())  # Перевод строки в нижний регистр

a = 2
b = 3
c = a + b
print(c)
c = a - b
print(c)
c = a * b
print(c)
c = a ** b
print(c)
c = a / b
print(c)
c = a // b
print(c)
c = a % b
print(c)
d = -4
print(abs(d))
d = -d
print(d)
a = -a
print(a)

# Логические типы
x = True
y = False
print(x)
print(y)
print(bool(1))
print(bool(0))
print(bool(10))
print(bool(-10))
print(bool(0))
c = None
print(bool(c))
print(5 == 2)
print(4 == 4)
print(5 > 3)
print(5 > 9)
print(4 != 4)
print(4 != 45)
a = 4 == 5
print(a)
x = 10
y = 5
a = x != y
print(a)
a = 10
b = 'apple'
c = a == b
print(c)
b2 = "Apple"
print(b == b2)
print(b == b2.lower())
x = b*3
print(x)
x = "banana" + b*3
print(x)
