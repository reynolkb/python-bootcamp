# def hello(name='Jose'):
#     print('The hello() function has been executed')
    
#     def greet():
#         return '\t This is inside the greet() function'
    
#     def welcome():
#         return "\t This is inside the welcome() function"
    
#     print(greet())
#     print(welcome())
#     print("Now we are back inside the hello() function")

# hello()


# def hello1(name='Jose'):
    
#     def greet():
#         return '\t This is inside the greet() function'
    
#     def welcome():
#         return "\t This is inside the welcome() function"
    
#     if name == 'Jose':
#         return greet
#     else:
#         return welcome

# x = hello1()
# print(x())


# def hello():
#     return 'Hi Jose!'

# def other(func):
#     print('Other code would go here')
#     print(func())

# other(hello)

def new_decorator(func):

    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func

def func_needs_decorator():
    print("This function is in need of a Decorator")

# Reassign func_needs_decorator
func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()

@new_decorator
def func_needs_decorator2():
    print("This function is in need of a Decorator")

func_needs_decorator2()