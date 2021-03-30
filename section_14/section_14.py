# ---------------------------------------- Collections Module ----------------------------------------
# from collections import Counter
# mylist = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,4]
# print(Counter(mylist))

# sentence = "How many times does each word show up in this sentence with a word"
# print(Counter(sentence.lower().split()))

# letters = 'aaaaabbbbbbbbccccccdddddd'
# c = Counter(letters)
# print(c.most_common(1))

# from collections import defaultdict
# d = {'a': 10}
# print(d['a'])

# d2 = defaultdict(lambda: 0)
# print(d2['Wrong Key!'])

# mytuple = (10, 20, 30)
# print(mytuple[0])

# from collections import namedtuple

# Dog = namedtuple('Dog', ['age', 'breed', 'name'])
# sammy = Dog(age=5, breed='Husky', name='Sam')
# print(sammy.breed)

# ---------------------------------------- Opening and reading files and folders ----------------------------------------
# import os
# import shutil

# f = open('practice.txt', 'w+')
# f.write('This is a text string')
# f.close()

# print(os.getcwd())
# print(os.listdir())
# # moves one folder up
# # shutil.move('practice.txt', '/Users/kylereynolds/Documents/Coding/Bootcamps/2020 Complete Python Bootcamp - From Zero to Hero in Python/')

# # for folder, sub_folders,files in os.walk(os.getcwd())

# file_path = '/Users/kylereynolds/Documents/Coding/Bootcamps/2020 Complete Python Bootcamp - From Zero to Hero in Python/section_14/Example_Top_Level'
# for folder, sub_folders,files in os.walk(file_path):
#     print(f'Currently looking at {folder}')
#     print('\n')
#     print('The subfolders are: ')
#     for sub_fold in sub_folders:
#         print(f'Subfolder: {sub_fold}')
#     print('\n')
#     print("The files are: ")
#     for f in files:
#         print(f'File: {f}')
#     print('\n')

# ---------------------------------------- Datetime Module ----------------------------------------
# import datetime

# mytime = datetime.time(2,20)
# print(mytime)

# today = datetime.date.today()
# print(today)
# print(today.ctime())

# from datetime import datetime

# mydatetime = datetime(2021, 10, 3, 14, 20, 1)
# print(mydatetime)

# mydatetime = mydatetime.replace(year = 2020)
# print(mydatetime)

# from datetime import date
# date1 = date(2021, 11, 3)
# date2 = date(2020, 11, 3)
# print(date1 - date2)

# from datetime import datetime

# datetime1 = datetime(2021, 11, 3, 22, 0)
# datetime2 = datetime(2021, 11, 3, 12, 0)

# print(datetime1 - datetime2)

# ---------------------------------------- Math and Random Modules ----------------------------------------
# import math
# value = 4.35
# print(math.floor(value))
# print(math.ceil(value))
# print(round(4.5))
# print(round(5.5))
# print(math.log(100,10))

# mylist = list(range(0,20))
# random.choice(mylist)

# ---------------------------------------- Regex ----------------------------------------
# import re
# (555)-555-5555
# r"(\d\d\d)-\d\d\d-\d\d\d\d"
# text = "The agent's phone number is 408-555-1234. Call soon!"
# 'phone' in text
# pattern = 'phone'
# match = print(re.search(pattern, text))
# text = 'my phone once, my phone twice'
# match = re.search('phone', text)
# print(match)
# matches = re.findall('phone', text)
# print(matches)
# for match in re.finditer('phone', text):
#     print(match)

# text = 'My phone number is 408-555-1234'
# phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)
# print(phone.group())

# phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
# print(phone)

# phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
# results = re.search(phone_pattern, text)
# print(results.group(1))

# print(re.search(r'cat|dog','The cat is here'))
# print(re.findall(r'...at','The cat in the hat went splat'))
# print(re.findall(r'^\d','The 2 is a number'))

# ---------------------------------------- Timing your python code ----------------------------------------
# def func_one(n):
#     return [str(num) for num in range(n)]
# print(func_one(10))

# def func_two(n):
#     return list(map(str, range(n)))
# print(func_two(10))

# import time

# # STEP 1: Get start time
# start_time = time.time()
# # Step 2: Run your code you want to time
# result = func_one(1000000)
# # Step 3: Calculate total time elapsed
# end_time = time.time() - start_time
# print(end_time)

# # STEP 1: Get start time
# start_time = time.time()
# # Step 2: Run your code you want to time
# result = func_two(1000000)
# # Step 3: Calculate total time elapsed
# end_time = time.time() - start_time
# print(end_time)

# import timeit
# setup = '''
# def func_one(n):
#     return [str(num) for num in range(n)]
# '''
# stmt = 'func_one(100)'
# print(timeit.timeit(stmt,setup,number=100000))

# setup2 = '''
# def func_two(n):
#     return list(map(str,range(n)))
# '''
# stmt2 = 'func_two(100)'
# print(timeit.timeit(stmt2,setup2,number=100000))

# ---------------------------------------- Unzipping and Zipping Files ----------------------------------------
# # slashes may need to change for MacOS or Linux
# f = open("new_file.txt",'w+')
# f.write("Here is some text")
# f.close()


# # slashes may need to change for MacOS or Linux
# f = open("new_file2.txt",'w+')
# f.write("Here is some text")
# f.close()

# import zipfile
# comp_file = zipfile.ZipFile('comp_file.zip','w')
# comp_file.write("new_file.txt",compress_type=zipfile.ZIP_DEFLATED)
# comp_file.write('new_file2.txt',compress_type=zipfile.ZIP_DEFLATED)
# comp_file.close()
# zip_obj = zipfile.ZipFile('comp_file.zip','r')
# zip_obj.extractall("extracted_content")

# ---------------------------------------- Advanced Python Module Puzzle ----------------------------------------
import shutil
shutil.unpack_archive('./unzip_me_for_instructions.zip', '', 'zip')
with open('extracted_content/Instructions.txt') as f:
    content = f.read()
    print(content)

import re
pattern = r'\d{3}-\d{3}-\d{4}'
test_string = 'here is a phone number 123-123-1234'
re.findall(pattern, test_string)

def search(file, pattern=r'\d{3}-\d{3}-\d{4}'):
    f = open(file, 'r')
    text = f.read()

    if re.search(pattern, text):
        return re.search(pattern, text)
    else:
        return ''

import os
results = []
for folder,sub_folders,files in os.walk(os.getcwd()+'/extracted_content'):
    for f in files:
        full_path = folder+'/'+f

        results.append(search(full_path))
for r in results:
    if r != '':
        print(r.group())