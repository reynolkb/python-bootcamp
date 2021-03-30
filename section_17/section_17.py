# ---------------------------------------- Working with CSV FIles in Python ----------------------------------------
# import csv
# data = open('example.csv',encoding="utf-8")
# csv_data = csv.reader(data)
# data_lines = list(csv_data)

# for line in data_lines[:5]:
#     print(line)

# all_emails = []
# for line in data_lines[1:15]:
#     all_emails.append(line[3])

# print(all_emails)

# full_names = []
# for line in data_lines[1:15]:
#     full_names.append(line[1]+' '+line[2])

# print(full_names)

# newline controls how universal newlines works (it only applies to text
# mode). It can be None, '', '\n', '\r', and '\r\n'. 
# file_to_output = open('to_save_file.csv','w',newline='')
# csv_writer = csv.writer(file_to_output,delimiter=',')
# csv_writer.writerow(['a','b','c'])
# csv_writer.writerows([['1','2','3'],['4','5','6']])
# file_to_output.close()

# f = open('to_save_file.csv','a',newline='')
# csv_writer = csv.writer(f)
# csv_writer.writerow(['new','new','new'])
# f.close()

# ---------------------------------------- Working with PDF Files in Python ----------------------------------------
# import PyPDF2

# Notice we read it as a binary with 'rb'
# f = open('Working_Business_Proposal.pdf','rb')
# pdf_reader = PyPDF2.PdfFileReader(f)
# pdf_reader.numPages
# page_one = pdf_reader.getPage(0)
# page_one_text = page_one.extractText()
# print(page_one_text)
# f.close()

# f = open('Working_Business_Proposal.pdf','rb')
# pdf_reader = PyPDF2.PdfFileReader(f)
# first_page = pdf_reader.getPage(0)
# pdf_writer = PyPDF2.PdfFileWriter()
# pdf_writer.addPage(first_page)
# pdf_output = open("Some_New_Doc.pdf","wb")
# pdf_writer.write(pdf_output)
# f.close()

# f = open('Working_Business_Proposal.pdf','rb')

# # List of every page's text.
# # The index will correspond to the page number.
# pdf_text = []

# pdf_reader = PyPDF2.PdfFileReader(f)

# for p in range(pdf_reader.numPages):
    
#     page = pdf_reader.getPage(p)
    
#     pdf_text.append(page.extractText())

# print(pdf_text[3])

# ---------------------------------------- PDFs and Spreadsheets Python Puzzle Exercise ----------------------------------------
import csv
data = open('Exercise_Files/find_the_link.csv',encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)

link_list = []
for row_num,data in enumerate(data_lines):
    link_list.append(data[row_num])
print(''.join(link_list))

link_str = ''
for row_num,data in enumerate(data_lines):
    link_str+=data[row_num]
print(link_str)

import PyPDF2
f = open('Exercise_Files/Find_the_Phone_Number.pdf','rb')
pdf = PyPDF2.PdfFileReader(f)
print(pdf.numPages)

import re
pattern = r'\d{3}.\d{3}.\d{4}'
for n in range(pdf.numPages):
    
    page  = pdf.getPage(n)
    page_text = page.extractText()
    match = re.search(pattern,page_text)
    
    if match:
        print(match.group())