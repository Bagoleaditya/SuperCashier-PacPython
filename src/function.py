import pandas as pd
import numpy as np
from tabulate import tabulate

# Initialize DataFrame
cart = pd.DataFrame(columns=['quantity', 'price'])

# Function to add transaction ID
def transaction():
    while True:
        cust_name = str(input("Please input your name: \n")).upper()
        no_hp = str(input("Please input your phone number: \n"))
        if len(no_hp)<7:
            print("ERROR: Phone number must have at least 7 digits.")
        else:
            transaction_id = cust_name[:2] + no_hp[-6:]
            return transaction_id



# Function to add items
def add_item(cart):
    while True:
        try:
            item_name = str(input("1. Add the item you want to purchase: ")).upper()
            item_qty = int(input("2. Add the quantity of the item: "))
            item_price = float(input("3. Add the price of the item: "))
            
            if item_qty <= 0 or item_price < 0:
                print("ERROR: Item quantity and price must be greater than 0!")
            else:
                cart.loc[item_name] = [item_qty, item_price]
                
                cont_input = input("Do you want to add anything else?(y/n) \n ").lower()
                if cont_input == "y":
                    continue
                elif cont_input =="n":
                    break
                
                    

            
        except ValueError:
            print("ERROR: Please input the correct value or number!")


# Function to update item name
def update_item_name(cart, old_name, new_name):
    try:
        cart.rename(index={old_name: new_name}, inplace=True)
    except KeyError:
        print("ERROR: Item not found!")


# Function to update item quantity
def update_item_qty(cart, item_name, new_qty):
    try:
        if new_qty <= 0:
            print("ERROR: The new quantity must be greater than 0!")
        else:
            cart.loc[item_name, 'quantity'] = new_qty
    except KeyError:
        print("ERROR: Item not found!")


# Function to update item price
def update_item_price(cart, item_name, new_price):
    try:
        if new_price < 0:
            print("ERROR: The new price must be greater than 0!")
        else:
            cart.loc[item_name, 'price'] = new_price
    except KeyError:
        print("ERROR: Item not found!")

# Function to delete item 
def delete_item(cart, item_name):
    try:
        cart.drop(item_name, inplace=True)
    except KeyError:
        print("ERROR: Item not found!")

# Function to empty cart
def reset_cart(cart):
    cart.drop(cart.index, inplace=True)

# Function to calculate total per-items
def display_item_prices_column(cart):
    cart['total_price'] = cart['quantity'] * cart['price']
    print(cart)