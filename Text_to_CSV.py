import csv

with open('Phone_Number_list.txt', 'r') as file:
    phone_numbers = file.read().splitlines()

with open('phone_numbers.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Phone Number Lists"])
    writer.writerow(phone_numbers)
    if writer:
         print(" ")
         print('Phone_numbers.txt file has been successfully converted to CSV File.')
         print("")
    else: 
         print('Phone_numbers.txt file has not been successfully converted to CSV File.')

        
