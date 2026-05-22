
from pos_operations1 import create_transaction,add_new_item,display_groceries

def login(users_lookup:dict):

    '''login interface which will loop on until the user does not successfully login. Returns the role of the user'''
    username = input("Enter Username:")
    password = input("Enter password:")

    
    if username in users_lookup:
        if password == users_lookup[username]['password']:
            role = users_lookup[username]['type']
            print(f"Welcome {username}. Logged in as {role}")
            return role
        else:
            print("Incorrect password")
            return None
    else:
        print("User not found")
        return None

def manager_menu(grocery_lookup : dict, transactions_log : list,groceries_columns):

    while(True):
        
        print("Press 1 to add transactions.\n" \
        "Press 2 to add new grocery item.\n" \
        "Press 3 to logout.")
        option = input("Enter the number:")

        if option == '1':
            display_groceries(grocery_lookup)
            grocery_id = input("Enter grocery id, or Press X to cancel:")
            quantity = input("Enter item quantity or Press X to cancel:")
            transaction = create_transaction(grocery_lookup, grocery_id, quantity)
            if transaction: #check if the transaction actually exists
                transactions_log.append(transaction)
        elif option == '2':
            add_new_item(grocery_lookup,groceries_columns)
        elif option == '3':
            print("Logged out successfully")
            break
            
def cashier_menu(grocery_lookup : dict, transactions_log : list):

    while(True):
        
        print("Press 1 to add transactions.\n" \
        "Press 3 to logout.")
        option = input("Enter the number:")

        if option == '1':
            display_groceries(grocery_lookup)
            grocery_id = input("Enter grocery id, or Press X to cancel:")
            quantity = input("Enter item quantity or Press X to cancel:")
            transaction = create_transaction(grocery_lookup, grocery_id, quantity)
            if transaction: #check if the transaction actually exists
                transactions_log.append(transaction)
        elif option == '3':
            print("Logged out successfully")
            break
        else:
            print("Invalid input")
            
