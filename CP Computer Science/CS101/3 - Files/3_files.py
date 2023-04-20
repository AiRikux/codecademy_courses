# Importing a File
## simple opening and printing a file content using with

with open('welcome.txt') as text_file:
  text_data = text_file.read()
print(text_data)

# Iterating Through Lines

with open('how_many_lines.txt') as lines_doc:
  for line in lines_doc.readlines():
    print(line)

# Reading a Line
## Show that if we use readline one after the other it takes the next line

with open('millay_sonnet.txt') as sonnet_doc:
  first_line = sonnet_doc.readline()
  second_line = sonnet_doc.readline()
  print(second_line)

# Writing a file
## open file with write mode and overwrite anything inside

with open('generated_file.txt', 'w') as gen_file:
  gen_file.write("What an incredible file!")

# Appending to a File
## opening the file using a for append mode

with open('generated_file.txt', 'a') as gen_file:
  gen_file.write("\n... and it still is")

# Reading CSV

import csv

with open('cool_csv.csv') as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  for line in cool_csv_dict:
    print(line['Cool Fact'])

# another delimiter

with open('books.csv') as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter='@')
  isbn_list = []
  for line in books_reader:
    isbn_list.append(line['ISBN'])
  print(isbn_list)