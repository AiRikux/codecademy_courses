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

# reading and writing csv

# data
access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'},
              {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'},
              {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'},
              {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'},
              {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'},
              {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'},
              {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'},
              {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'},
              {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'},
              {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

# import module
import csv

with open('logger.csv', 'w') as logger_csv:
	log_writer = csv.DictWriter(logger_csv, fieldnames=fields)

	log_writer.writeheader()

	for each in access_log:
		log_writer.writerow(each)

# reading JSON file
import json

with open('message.json') as message_json:
	message = json.load(message_json)
