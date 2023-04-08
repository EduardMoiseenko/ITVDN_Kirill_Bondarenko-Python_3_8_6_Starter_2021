# if-else
counter = 0
if counter < 10:
    counter += 1
else:
    print(counter)
print('----------------------------------------------------')
# Заглушка для f-else
counter = 0
if counter < 10:
    counter += 1
else:
    pass
print(counter)
print('----------------------------------------------------')
# if-elif
animal = 'cat'
if animal == 'cat':
    print('Meo')
elif animal == 'dog':
    print('Wof')
else:
    print("I don't know this animal")
print('----------------------------------------------------')
# if-elif
animal = 'bird'
if animal == 'cat':
    print('Meo')
elif animal == 'dog':
    print('Wof')
elif animal == 'bird':
    print('tweet')
else:
    print("I don't know this animal")
print('----------------------------------------------------')
# Тернарный оператор <expresion on true> if <predicate> else <expression on false>
value = 1 if 2 > 2 else 0
print(value)
print('----------------------------------------------------')
value1 = 'hello' if 2 < 4 else 'Bye'
print(value1)
print('----------------------------------------------------')
value2 = 10
result_value_greater_than_zero = True if value2 > 0 else False
print(result_value_greater_than_zero)
print('----------------------------------------------------')
product_price = 600
if product_price > 1000:
    product_price = product_price * 0.9
elif product_price > 500:
    product_price = product_price * 0.95
elif product_price > 100:
    product_price = product_price * 0.97
print(product_price)
print('----------------------------------------------------')
a = 10
b = 5
a = a + b
print(a)
a = 10
a += b
print(a)
b += 3
print(b)
a /= 5
print(a)
a *= 3
print(a)
b -= 8
print(b)
print('----------------------------------------------------')
value_str = ""
print(None if value_str == "" else value_str)
print('----------------------------------------------------')
value_str = "Hello"
print(None if not value_str else value_str)
print('----------------------------------------------------')
first_value = 4
second_value = 0
operator = '/'
if operator == '+':
    print(first_value + second_value)
elif operator == '-':
    print(first_value - second_value)
elif operator == '/':
    if second_value == 0:
        print("Can't divide by 0")
    else:
        print(first_value / second_value)
elif operator == '*':
    print(first_value * second_value)
else:
  print('Operator is wrong. Choose from given: + - / *')
