import csv
from datetime import datetime
import sys

from login_interface2 import login,manager_menu,cashier_menu

'''
q1.py is the main code file which will be interactive with the terminal

create separate functions for each feature

feature 1: login option and give access based on cashier and manager
feature 2: add the transactions (both cashier and manager)
feature 2: change the grocery details (only manager)

q1.py has a login option also updates the files in the end and closes them

'''
#import the files
try:
    transactions_filepath = sys.argv[1]
    groceries_filepath = sys.argv[2]    
except IndexError:
    print("Usage python q1.py transactions.csv groceries.csv")


#reading the files
try:
    transactions = open(transactions_filepath,newline='')
    #make readers for the files
    transactions_reader = csv.DictReader(transactions)
    transactions_columns = transactions_reader.fieldnames
        
except FileNotFoundError:
    print(f"{transactions_filepath} directory does not exist")


try:
    groceries = open(groceries_filepath,newline='',encoding='UTF-8-sig')
    groceries_reader = csv.DictReader(groceries)
    groceries_columns = groceries_reader.fieldnames

    grocery_lookup = {}

    for row in groceries_reader:
        grocery_lookup[row[groceries_columns[0]]] = {groceries_columns[1]:row[groceries_columns[1]],
                                                       groceries_columns[2]:row[groceries_columns[2]],
                                                       groceries_columns[3]:row[groceries_columns[3]]}
        
except FileNotFoundError:
    print(f"{groceries_filepath} directory does not exist")


users_filepath = "users.csv"
try:
    users= open(users_filepath,newline='',encoding='utf-8-sig')
    users_reader = csv.DictReader(users)
    users_columns = users_reader.fieldnames
    
    #store the users in a dict for instant retrieval
    users_lookup = {}
    
    for row in users_reader:
        users_lookup[row[users_columns[0]]] = {users_columns[1] : row[users_columns[1]], 
                                          users_columns[2] : row[users_columns[2]]}
except FileNotFoundError:
    print(f"{users_filepath} directory does not exist.")

#----------------------------------------------------------------------------#



#global variables

transactions_log = []

# --------login interface -------

while(True):
    #loop will keep on running until user is not validated
    enter_interface = input("Press 1 to login.\n" \
    "Press 2 to exit program.\n"
    "Enter : ")
    
    if enter_interface == '2':
        break
    
    elif enter_interface == '1':
        #login interface entered
        role = login(users_lookup)

        if role == 'manager':
            manager_menu(grocery_lookup,transactions_log,groceries_columns)
            break
        elif role == 'cashier':
            cashier_menu(grocery_lookup,transactions_log)
            break
        else:
            #re run the login interface
            print("Incorrect login credentials")
            continue
    
    else:
        print("Invalid input")
    
#after logging out

#closing the files in reading operation
transactions.close()
groceries.close()
users.close()

#write changes
if len(transactions_log) > 0:
    #write new transactions
    with open(transactions_filepath, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=['date','time','id','quantity','payment'])
        writer.writerows(transactions_log)

with open(groceries_filepath, "w", newline="", encoding="UTF-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=groceries_columns)
    writer.writeheader()
    for id, item in grocery_lookup.items():
        #unpack the item dictionary : {'id', 'name','price','stock'}
        writer.writerow({groceries_columns[0]: id, **item})


print("Program terminated")