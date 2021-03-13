# ---------------------------------------- Errors and Exception Handling ----------------------------------------
# def add(n1, n2):
#     print(n1+n2)

# # number1 = 10
# # number2 = input("Please provide a number")

# # add(number1, number2)

# try:
#     result = 10 + '10'
# except:
#     print("Hey it looks like you aren't adding correctly!")
# else:
#     print("Add went well!")
#     print(result)

# try:
#     f = open('testfile', 'w')
#     f.write("Write a test line")
# except TypeError:
#     print("There was a type error!")
# except OSError:
#     print("Hey you have an OS error")
# except:
#     print("All other exceptions")
# finally:
#     print("I always run")

# def ask_for_int():
    
#     while True:
#         try:
#             result = int(input("Please provide number: "))
#         except:
#             print("Whoops! that is not a number")
#             continue
#         else:
#             print("Yes thank you")
#             break
#         finally:
#             print("End of try/except/finally.")

# ask_for_int()

# ---------------------------------------- Errors and Exception Handling Homework ----------------------------------------
# try:
#     for i in ['a', 'b', 'c']:
#         print(i**2)
# except TypeError:
#     print("Type error! Watch out!")

# try:
#     x = 5
#     y = 0
#     z = x/y
# except:
#     print("error!!")
# finally:
#     print('All done')

# def ask():
#     while True:
#         try:
#             n = int(input("Enter a number "))
#         except:
#             print("Please try again! \n")
#             continue
#         else:
#             break
#     print("Your number squared is: ")
#     print(n**2)

# ask()

# ---------------------------------------- Pylint Overview ----------------------------------------
# '''
# A very simple script
# '''

# def myfunc():
#     '''
#     A simple function
#     '''
#     first = 1
#     second = 2
#     print(first)
#     print(second)

# myfunc()

# ---------------------------------------- Running test with the Unittest Library ----------------------------------------
