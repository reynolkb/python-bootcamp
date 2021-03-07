# def myfunc(*args):
#     for item in args:
#         print(item)

# myfunc(40,60,100,1,34)

# def myfunc(**kwargs):
#     print(kwargs)
#     if 'fruit' in kwargs:
#         print('My fruit of choice is {}'.format(kwargs['fruit']))
#     else:
#         print('I did not my any fruit here')

# myfunc(fruit='apple', veggie = 'lettuce')

# def myfunc(*args,**kwargs):
#     print(args)
#     print(kwargs)
#     print('I would like {} {}'.format(args[0],kwargs['food']))

# myfunc(10,20,30,fruit='orange,',food='eggs',animal='dog')

# def myfunc(*args):
#     list = []
#     for item in args:
#         if (item % 2) == 0:
#             list.append(item)
#     return(list)

# myfunc(5,6,7,8)

# def myfunc(st):
#     res = []
#     for index, value in enumerate(st):
#         if index % 2 == 0:
#             res.append(value.upper())
#         else:
#             res.append(value.lower())
#     return ''.join(res)

# myfunc('test')

# def lesser_of_two_evens(a,b):
#     if a % 2 == 0 and b % 2 == 0:
#         # both numbers are even
#         # if a < b:
#         #     result = a
#         # else:
#         #     result = b
#         result = min (a,b)
#     else:
#         # one or both numbers are odd
#         # if a > b:
#         #     result = a
#         # else: 
#         #     result = b
#         result = max (a,b)
#     # return result
#     print(result)

# lesser_of_two_evens(2,4)
# lesser_of_two_evens(7,5)

# def animal_crackers(text):
#     wordlist = text.lower().split()

#     print(wordlist[0][0] == wordlist[1][0])

# animal_crackers('Levelheaded lama')
# animal_crackers('hungry tiger')

# def makes_twenty(n1,n2):
    # return (n1+n2) == 20 or n1==20 or n2==20
    # if n1 + n2 == 20 :
    #     print('true')
    # elif n1 == 20:
    #     print('true')
    # elif n2 == 20:
    #     print('true')
    # else:
    #     print('false')

# ---------------------------------- Level 1 Problems ----------------------------------
# def old_macdonald(name):

#     first_letter = name[0]
#     inbetween = name[1:3]
#     fourth_letter = name[3]
#     rest = name[4:]

#     print(first_letter.upper() + inbetween + fourth_letter.upper() + rest)

# old_macdonald('macdonald')

# def old_macdonald(name):
    
#     first_half = name[:3]
#     second_half = name[3:]

#     print (first_half.capitalize() + second_half.capitalize())

# old_macdonald('macdonald')

# def master_yoda(text):
#     wordlist = text.split()
#     reverse_word_list = wordlist[::-1]
#     print (' '.join(reverse_word_list))

# master_yoda('we are ready')

# def almost_there(n):

#     print((abs(100-n) <= 10) or (abs(200-n) <= 10))

# almost_there(104)
# almost_there(150)
# almost_there(209)

# ---------------------------------- Level 2 Problems ----------------------------------

# def has_33(nums):

#     for i in range(0,len(nums)-1):
#         if nums[i] == 3 and nums[i+1] == 3:
#             print('true')
#             return

#     print('false')

# has_33([1,3,3])
# has_33([1,3,1,3])

# def paper_doll(text):
#     result = ''

#     for char in text:
#         result += char*3
#     print(result)

# paper_doll('hello')

# def blackjack(a,b,c):

#     if sum([a,b,c]) <= 21:
#         print (sum([a,b,c]))
#     elif 11 in [a,b,c] and sum([a,b,c]) <= 31:
#         print ((sum([a,b,c])) - 10)
#     else:
#         print ('bust')

# blackjack(5,6,7)
# blackjack(9,9,9)
# blackjack(9,9,11)

# def summer_69(arr):

#     total = 0
#     add = True
#     for num in arr:
#         while add:
#             if num != 6:
#                 total += num
#                 break
#             else:
#                 add = False
#         while not add:
#             if num != 9:
#                 break
#             else:
#                 add = True
#                 break
#     print (total)

# summer_69([1,3,5])
# summer_69([4,5,6,7,8,9])
# summer_69([2,1,6,9,11])

# ---------------------------------- Challenging Problems ----------------------------------

# def spy_game(nums):

#     code = [0,0,7,'x']

#     for num in nums:
#         if num == code[0]:
#             code.pop(0)
#     print (len(code) == 1)

# spy_game([1,2,4,0,0,7,5])
# spy_game([1,0,2,4,0,5,7])
# spy_game([1,7,2,0,4,5,0])

# def count_primes(num):

#     if num < 2:
#         return 0
    
#     primes = [2]
#     x = 3

#     while x <= num:
#         # check if x is prime
#         # for y in range(3,x,2):
#         for y in primes:
#             if x % y == 0:
#                 x += 2
#                 break
#         else:
#             primes.append(x)
#             x += 2
#     print(primes)

# count_primes(10)

# def square(num):
#     return num**2

# my_nums = [1,2,3,4,5]

# print(list(map(square, my_nums)))

# for num in my_nums:
#     print(square(num))

# def splicer(mystring):
#     if len(mystring)%2 == 0:
#         return 'EVEN'
#     else:
#         return mystring[0]

# names = ['Andy', 'Eve', 'Sally']
# names = {
#     "one": "andy",
#     "two": "eve",
#     "three": "sally"
# }

# print(list(map(splicer,names.values())))

# def check_even(num):
#     return num%2 == 0

# mynums = [1,2,3,4,5,6]

# print(list(filter(check_even, mynums)))

# for n in filter(check_even, mynums):
#     print(n)

# use lambda function one time like anonymous functions
# lambda num: num ** 2

# mynums = [1,2,3,4,5,6]
# names = ['Andy', 'Eve', 'Sally']

# print(list(map(lambda num: num ** 2, mynums)))
# print(list(filter(lambda num: num % 2 == 0, mynums)))
# print(list(map(lambda x:x[0], names)))

# x = 25

# def printer():
#     x = 50
#     return x

# print(x)
# print(printer())

# x = 50

# def func():
#     global x
#     print(f'X is {x}')

#     # local reassignment on a global variable
#     x = 200
#     print(f'I just locally changed global x to {x}')

# func()
# print(x)

# x = 50

# def func(x):
#     print(f'X is {x}')

#     # local reassignment on a global variable
#     x = 200
#     print(f'I just locally changed global x to {x}')
#     return x
# x = func(x)

# func(x)
# print(x)

# ---------------------------------- Methods and Functions Homework ----------------------------------

# def vol(rad):
#     return (4/3)*(3.14)*(rad**3)

# print(vol(2))

# def ran_check(num,low,high):
#     if num in range(low,high+1):
#         print(f'{num} is in range of {low} and {high}')
#     else:
#         print('not in range')

# ran_check(5,2,7)

# def up_lows(s):
#     d = {'upper': 0, 'lower': 0}

#     for char in s:
#         if char.isupper():
#             d['upper'] += 1
#         elif char.islower():
#             d['lower'] += 1
#         else:
#             pass
    
#     print(f'Original String: {s}')
#     print(f'Lowercase count: {d["lower"]}')
#     print(f'Uppercase count: {d["upper"]}')

# up_lows('Hello Mr. Rogers, how are you this fine Tuesday?')

# def unique_list(first):
#     # print(list(set(first)))
#     seen_numbers = []
#     for number in first:
#         if number not in seen_numbers:
#             seen_numbers.append(number)
#     return seen_numbers

# print(unique_list([1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,]))

# def multiply(numbers):
#     total = 1

#     for num in numbers:
#         total = total * num
#     return total

# print(multiply([1,2,3,-4]))

# def palindrome(s):
#     # remove spaces from string
#     s = s.replace(' ','')
#     # check if string is == reversed version of the string
#     # ::-1 starting at the beginning, going all the way to the end, step size of -1 so going back 1
#     return s == s[::-1]

# print(palindrome('nurses run'))

# import string

# def ispangram(str1, alphabet=string.ascii_lowercase):
#     # create a set of the alphabet
#     alphaset = set(alphabet)
#     # remove any spaces from the input string
#     str1 = str1.replace(' ','')
#     # convert into all lower case
#     str1 = str1.lower()
#     # grab all unique letters from the string set()
#     str1 = set(str1)
#     # alphabet set == string set input
#     return str1 == alphaset

# print(ispangram('The quick brown fox jumps over the lazy dog'))