# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hello world, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Paul')
    print('0----')
    print(' ||||')
    print('*' * 19)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Variables
# price = 209
# name = 'Me'
# print('The price is ')
# is_published = True
# print(price)
#
# name = input('What is your name? ')
# fav_color = input('What is your favourite color? ')
# birth_year = input('What is your year of birth? ')
# age = 2021 - int(birth_year)
# print(type(age))
# print(name + ' likes ' + fav_color + ' and he is ' + str(age) + ' years old')

# **We use three quotes to define a multiline string
message = '''This it just a 
multiline string in python'''
print(message)
print(message[2])
print(message[-1]) #last character
print(message[-2]) #secondlast character
print(message[0:4]) #from 0 to the 3 character
print(message[0:]) #All charcters
print(message[:]) #All charcters
print(message[2:]) #excluding 2
print(message[1:-1]) #excluding 1 and the last one

# Formatted string in python
f_name = 'John'
l_name = 'Doe'
full_name = f'{f_name} {l_name} is a [coder]'
print(full_name)
print(len(full_name))
print(full_name.upper())
print(full_name.find('o')) #returns the first index of the occurence otherwise -1
print(full_name.replace('o', 'j')) #replaces the first with the second
print('John' in full_name)

# Operators
print(4 / 3) #division
print(4 // 3) #division returns whole number

# if stratements in python
is_hot = True
is_cold = False
if is_hot:
    print('Today is a hot day')
elif is_cold:
    print('It is a cold day, wear warm clothes')
else:
    print('It is a lovely day')


#A simple task
has_good_credit = False
price = 1000000
if has_good_credit:
    print('You need to pay ' + str(0.1 * price))
else:
    print('You need to pay ' + str(0.2 * price))

#Logical operators
has_high_income = False
has_good_crdt = True
if has_high_income and has_good_crdt:
    print('This is real good')
elif has_good_crdt and not has_high_income:
    print('Your Credit is good')
elif not has_good_crdt and has_high_income:
    print('You are almost there')
else:
    print('You do not got this')


#Comparison operators
temperature = 30
if temperature > 10:
    print('It is a hot day')

#program for converting weight
# weight = int(input('What is your weight? '))
# unit = input('Whay is the unit (k) for Kgs and (l) for pounds ')
# if unit.upper() == 'K':
#     converted_weight = weight / 0.45
#     print(f'Your weight is {converted_weight} Pounds')
# elif unit.upper() == 'L':
#     converted_weight = weight * 0.45
#     print(f'Your weight is {converted_weight} Kilos')
# else:
#     print(f'The unit is invalid')

#While condition
i = 1
while i <=18:
    print(i)
    i += 1
print("Done")

# i = 1
# while i <=10:
#     print('*' * i)
#     i += 1
# print("Done")


#A program for guessing a number
# guess_count = 0
# guess_limit = 3
# correct_guess = 5
# while guess_count < guess_limit:
#     guess_input = int(input('Guess number '))
#     guess_count += 1
#     if guess_input == correct_guess:
#         print('You won')
#         break
# else:
#     print('You lost')

# For loops
text = 'Python'
for list in text:
    print(list)

for item in range(4,10):
    print(item)

for item in range(0 ,10 ,2): #2 is the step
    print(item)

sum = 0
for item in range(0 ,50):
    sum += item
print(sum)


#nested loops -> generating coordinates
for x in range(5):
    for y in range(5):
        print(f'({y}, {x})')


#program to display f
numbers = [5, 2, 5, 2, 2]
for num in numbers:
    print('x' * num)

#Lists in python (arrays)
names = ['John', 'Doe', 'Paul', 'Jan']
print(names[0:2])

#2d lists
matrix = [
    [1, 3, 4],
    [2, 3, 3],
    [4, 6, 2]
]
print(matrix[0][1])

#list methods
# insert(i, value)
# remove(value)
# clear()
# pop(value)
# index(value)
#list.copy(list_two)
#count(value) returns the number of value in the lists


#tupples
number = (2, 23, 43)

# it has only index and count functions
# they are immutable
# can not be modified


#unpacking can also apply to lists
numbers = (2, 23, 43)
x, y , z = numbers

#disctionaris (objects in js)
customers = {
    'name': 'Paul',
    'age': 25,
    'is_verified': True
}
customers['is_new'] = True
print(customers['name'])
print(customers.get('name'))
print(customers.get('gender', 'The value is blank'))

#Functions in python
def greet_user (name):
    print(f'Hi there {name}')
    print('Welcome aboard')


print('start')
greet_user('Paul')
greet_user('Dilly')
greet_user('Mary')
print('Stop')

# In python, we always define function then call them
# by default, all functions return None
# 2 blank lines after python functions

#exceptions in python
try:
    age = int(input('Enter your age? '))
    print(age)
    income = 2000000
    random_number = income / int(age)
except ValueError:
    print('Invalid value')
except ZeroDivisionError:
    print('Age cannot be zero')