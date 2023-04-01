# Цикл While
counter = 5
while counter > 0:
    print('Iteration, counter =', counter)
    counter -= 1
print(counter)
print('-------------------------------------')
# Цикл for
for number in range(5):
    print(number)
print('-------------------------------------')
for element in range(9):
    if element == 3:
        continue
    print(element)
print('-------------------------------------')
for element in range(4):
    if element == 1:
        break
    print(element)
print('-------------------------------------')
for number in range(20):
    if number % 2 == 0:
        print(number)
print('-------------------------------------')
counter = 0
end_value = 20
while counter < end_value:
    if counter % 2 == 0:
        print(counter)
    counter += 1
print('-------------------------------------')
word = 'hello'
for char in word:
    if char == 'l':
        print('s')
    else:
        print(char)    
print('-------------------------------------')
back_counter = 30
end_value = 0
while back_counter > end_value:
    if back_counter % 5 == 0:
        print(back_counter)
    back_counter -= 1
