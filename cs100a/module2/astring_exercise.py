#define int input function
def int_input_function():
    valid = False
    while valid == False:
        try:
            int = int(input())
            if int == '':
                raise ValueError('empty sring')
            valid = True
        except ValueError:
            print('Invalid Input.')
    return int

#1

#request for user to input any string
string = input('please input a string: ')

#request case selection from user
case = input('would you like to see the string in 1. upper case, 2. lower case, or 3. title case? ')
#repeat request for case selection until user responds with numerals '1', '2', or '3'
while case != '1' and case != '2' and case != '3':
    case = input('would you like to see the string in 1. upper case, 2. lower case, or 3. title case?')

#generate formatted string based on user input
if case == '1':
    print (string.upper())
elif case == '2':
    print(string.lower())
elif case == '3':
    print(string.title())

#2

#request for user to input a link in a string
link = input('please enter a link to a website: ')

#check if string starts with http, display results
if link.startswith('http'):
    print('thank you for entering a valid link.')
else:
    print('you entered an invalid link.')

#3

#request for user to input their name in a string
name = input('what is your name? ')

#strip consonants and vowels, for an extra fun time
if name[-1] in ('a', 'e', 'i', 'o', 'u'):
    namestrip = name.strip('aeiou')
else:
    namestrip = name.strip('bcdfghjklmnpqrstvwxyz')
#welcome message, using stripped name
print(f'hello, {namestrip}, and welcome to the strip club')





    



