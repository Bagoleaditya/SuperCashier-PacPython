import pandas as pd
import numpy as np
from tabulate import tabulate
from datetime import datetime

# Initialize DataFrame
cart = pd.DataFrame(columns=['quantity', 'price'])

# Function to add transaction ID
def transaction():
    """
    Create transaction_id variable from information that customer inputted.

    Returns:
        transaction_id variable
    """
    while True:
        cust_name = str(input("Please input your name: \n")).upper()
        no_hp = str(input("Please input your phone number: \n"))
        if len(no_hp)<6:
            print("ERROR: Phone number must have at least 6 digits.")
        else:
            current_time = datetime.now().strftime('%H%M%S')
            transaction_id = no_hp[-4:]+current_time
            return transaction_id



# Function to add items
def add_item(cart):
    """
    Function to ask customer about item information 

    Args:
        cart : a DataFrame to store item information
    
    Returns:
        a DataFrame filled by item information
    """
    while True:
        try:
            item_name = str(input("1. Add the item you want to purchase: \n")).upper()
            item_qty = int(input("2. Add the quantity of the item: \n"))
            item_price = float(input("3. Add the price of the item: \n"))
            

            if item_qty <= 0 or item_price <= 0:
                print("ERROR: Item quantity and price must be greater than 0!")
            else:
                cart.loc[item_name] = [item_qty, item_price]
                print("Your order has been added! \n    ")
                
                cont_input = input("Do you want to add anything else?(y/n) \n ").lower()
                if cont_input == "y":
                    continue
                elif cont_input =="n":
                    break
                
                    

            
        except ValueError:
            print(f"ERROR:Please input the correct value or number!")


# Function to update item name
def update_item_name(cart, old_name, new_name):
    """
    Function to update item name

    Args:
        cart: a DataFrame to store item information
        old_name: current item name 
        new_name: new item name
    """
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
    print("Your cart is empty")
    print("-"*30)
    print("\n")



# Function to calculate total per-items
def calculate_total_price(final_cart):
    final_cart['total_price'] = final_cart['quantity'] * final_cart['price']
    
    return final_cart

def discount(final_cart):
    discounts = []
    for index, row in final_cart.iterrows():
        total_price = row['total_price']
        if total_price > 500000:
            discounts.append(7)
        elif total_price > 300000:
            discounts.append(6)
        elif total_price > 200000:
            discounts.append(5)
        else:
            discounts.append(0)
    final_cart['disc'] = discounts

    return final_cart
    
def calculate_discount_price(final_cart):
    final_cart['disc_price'] = final_cart['total_price']*(1-(final_cart['disc']/100))

    return final_cart

