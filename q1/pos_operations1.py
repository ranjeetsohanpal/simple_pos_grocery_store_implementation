from datetime import datetime



def display_groceries(groceries_lookup : dict):  #working
    '''Show the existing grocery list'''
    col_widths = {'id': 6, 'name': 20, 'stock': 8, 'price': 8}

    # Header
    header = f"{'ID':<{col_widths['id']}} {'Name':<{col_widths['name']}} {'Stock':<{col_widths['stock']}} {'Price':<{col_widths['price']}}"
    divider = '-' * len(header)

    print(divider)
    print(header)
    print(divider)

    for id in groceries_lookup:
        print(
            f"{id:<{col_widths['id']}} "
            f"{groceries_lookup[id]['name']:<{col_widths['name']}} "
            f"{groceries_lookup[id]['stock']:<{col_widths['stock']}} "
            f"${float(groceries_lookup[id]['price']):<{col_widths['price'] - 1}.2f}"
        )

    print(divider)


def create_transaction(grocery_lookup : dict,grocery_id,quantity): #working 1(1)
    '''Create a dictionary for the transaction'''

    if grocery_id.lower() == 'x' or quantity.lower() == 'x':   
        return None 

    #current quantity of the item in the stock
    stock = int(grocery_lookup[grocery_id]['stock'])
    
    #check if the order quantity is more than the existing stock
    if stock < int(quantity):
        print("Not enough stock")
        return None
    
    
    #update the stock
    stock -= int(quantity)
    grocery_lookup[grocery_id]['stock'] = stock
    payment = int(quantity) * float(grocery_lookup[grocery_id]['price'])
   
    datetime_of_sale = datetime.now()
    date_of_sale = datetime_of_sale.strftime("%d/%m/%Y")
    time_of_sale = datetime_of_sale.strftime("%I:%M:%S %p")

    #final confirmation
    confirm = input("Confirm the transaction. [y/n]")

    if confirm.lower() == 'n':
        return None

    #[date, time, id, quantity, payment]
    transaction = {'date':date_of_sale,'time':time_of_sale,'id':grocery_id,
                   'quantity':quantity,'payment':str(payment)}

    return transaction

  

def add_new_item(grocery_lookup:dict,groceries_columns): #1(2)
    '''Add new items in the groceries'''

    #new id generated for the item
    grocery_id_list = list(grocery_lookup.keys())
    int_ids = [int(i) for i in grocery_id_list]
    new_id = str(max(int_ids) + 1)


    name = input("Enter name of item:")
    stock = input("Enter the stock:")
    price = input("Enter the price:")

    # column structure = ['id','name','price','stock']
    #enter the item in the grocery_lookup
    grocery_lookup[new_id] = {groceries_columns[1]:name, 
                              groceries_columns[2]:price,
                              groceries_columns[3]:stock}


