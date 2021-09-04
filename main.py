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