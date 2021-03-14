# def create_cubes(n):
#     result = []
#     for x in range(n):
#         result.append(x**3)
#     return result

# print(create_cubes(10))

# def create_cubes(n):
    
#     for x in range(n):
#         yield x**3

# for x in create_cubes(10):
#     print(x)    

# def genfibon(n):
#     """
#     Generate a fibonnaci sequence up to n
#     """
#     a = 1
#     b = 1
#     for i in range(n):
#         yield a
#         a,b = b,a+b

# for num in genfibon(10):
#     print(num)

# fib list

# def fibon(n):
#     a = 1
#     b = 1
#     output = []
    
#     for i in range(n):
#         output.append(a)
#         a,b = b,a+b
        
#     return output

# fibon(10)

# def simple_gen():
#     for x in range(3):
#         yield x

# # Assign simple_gen 
# g = simple_gen()

# print(next(g))
# print(next(g))
# print(next(g))

# s = 'hello'

# #Iterate over string
# # for let in s:
# #     print(let)

# s_iter = iter(s)
# print(next(s_iter))
# print(next(s_iter))

def gensquares(N):
    for i in range(N):
        yield i**2

for x in gensquares(10):
    print(x)

import random

random.randint(1,10)

def rand_num(low,high,n):
    
    for i in range(n):
        yield random.randint(low, high)

for num in rand_num(1,10,12):
    print(num)

s = 'hello'

s = iter(s)

print(next(s))

my_list = [1,2,3,4,5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)