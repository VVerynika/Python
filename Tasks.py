###2.1
# Write a program that prints the input text a given number of times, line by line.
# The text and the number of repetitions should be entered using input()

i = input('Text: ')
k = int(input('Number: '))
n = 0
while n < k:
    n = n + 1
    print(i)

### 2.2
# Write a program that checks if a year is a leap year.
# Years that are divisible by 4 without a remainder (2004, 2008) and are not centuries (500, 600) are considered leap years.
# However, if a year is divisible by 400 without a remainder, it is also considered a leap year (1200, 2000)

a = int(input('Enter year: '))
if a % 4 == 0 and a % 100 != 0:
    print('Leap Year')
elif a % 400 == 0:
    print('Leap Year')
else:
    print('Not Leap Year')

# or

year = 2027

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(True)
else:
    print(False)

###2.3
# Write a calculator program that takes two numbers and an operator (in str format),
# performs the given arithmetic operation and prints the result in the format: {num1} {operator} {num2} = {result}

i = input('Number1: ')
k = input('Number2: ')
f = input('Operator (+, -, *, /): ')
if f == '+':
    result = float(i) + float(k)
elif f == '-':
    result = float(i) - float(k)
elif f == '*':
    result = float(i) * float(k)
elif f == '/':
    if float(k) == 0:
        result = 'Division by zero'
    else:
        result = float(i) / float(k)

print(f'{i} {f} {k} = {result}')
print(type(result))

### 3.1
# Remove repeated values from the list [1, 2, 3, 4, 5, 3, 2, 1]

my_list = [1, 2, 3, 4, 5, 3, 2, 1]

result = []
for x in my_list:
    if x not in result:
        result.append(x)
print(result)

# or

new_list = list(set(my_list))
print(new_list)

### 3.2
# Given list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
#    - get the sum of all numbers,
#    - print out all the lines that contain the letter 'a'

list_1 = ['Hi', 'ananas', 2, 75, 'pizza', 36, 100]
my_sum = 0
for key in list_1:
    if type(key) in (int, float):
        my_sum += key
print(my_sum)

for key in list_1:
    if type(key) is str and 'a' in key:
        print(key)

# or

sum_of_li = [summ for summ in list_1 if isinstance(summ, int)]
print(sum(sum_of_li))

el_a = [el for el in list_1 if isinstance(el, str) and 'a' in el]
print(el_a)

### 3.3
# Find the sum of all values in my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}

my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
result = 0
for key in my_dictionary:
    result += my_dictionary[key]
print(result)


### 4.1
# Write a square function that takes 1 argument, the side of a square, and returns 3 values (using a tuple):
#      perimeter of the square, area of the square, and diagonal of the square.

intt = int(input())
def square(*args):
    print(args)

square(intt*4, intt*2, intt**(0.5))

# or

a = int(input())
def square(a):
    res = (a*4, a**2, (2*a*a)**0.5)
    return(res)

print(square(a))


### 4.2
# Write a function that takes any number of named arguments and outputs them line by line
#      In the format: argument: value. For example:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer

def introduce(**kwargs):
    for a, b in kwargs.items():
        print(f'{a}: {b}')


introduce(name='John', last_name='Smith', age=35, position='web developer')


### 4.3
# Using a lambda expression, from the list my_list = [20, -3, 15, 2, -1, -21],
# create a new list containing only  positive numbers

my_list = [20, -3, 15, 2, -1, -21]

nlist = list(filter(lambda x: x > 0, my_list))
print(nlist)


### 4.4
# Using a lambda expression, get the result of multiplying the values in the previous list (my_list)

from functools import reduce
my_list = [20, -3, 15, 2, -1, -21]

nlist = reduce(lambda x, y: x*y, my_list)
print(nlist)


### 4.5
# Write a decorator that calculates the running time of the function it takes as a parameter

def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Execution time: {} seconds.'.format(end - start))
        return return_value

    return wrapper

@benchmark
def fetch_webpage(url):
    import requests
    requests.get(url)

fetch_webpage('https://google.com')

