# Python program to demonstrate
# writing to CSV

import os
import sys
import csv
import pandas as pd
	
# field names
fields = ['Name', 'Dept', 'Course', 'Scores']
	
# data rows of csv file
rows = [ ['Okechukwu', 'BCH', 'BCH302', '90'],
		['Friday', 'MCB', 'BCH302', '92'],
		['Nicholas', 'BCH', 'BCH302', '91'],
		['Saturday', 'MCB', 'BCH302', '85'],
		['Patrick', 'BCH', 'BCH302', '89'],
		['Desmomd', 'MCB', 'BCH302', '74']]

	
# writing to csv file
with open(os.path.join(sys.path[0], 'school_records.csv'), 'w', newline = '') as csvfile:
	# creating a csv writer object
	my_csvfile = csv.writer(csvfile)
		
	# writing the data fields
	my_csvfile.writerow(fields)
		
	# writing the data rows
	for records in rows:
		print(records)
		my_csvfile.writerow(records)

#Reading the csv file as school_records
with open(os.path.join(sys.path[0], 'school_records.csv'),'r') as my_csvfile:
	read_file = pd.read_csv(my_csvfile)
	print(read_file)
