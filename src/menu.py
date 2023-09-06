from tabulate import tabulate
import pandas as pd




def cashier_menu():
    print("-"*30)
    print("Ojo Kendor Menu: ")
    print("-"*30)
    print("1. Add item to cart")
    print("2. Update item from cart")
    print("3. Delete item from cart")
    print("4. Reset cart")
    print("5. Check order from your cart")
    print("6. Checkout your cart")
    print("7. Exit")
    print("-"*30)

    return cashier_menu

def display_cart(cart):
    #cart['total'] = cart['quantity']*cart['price']
   
    print("Your Cart Order: \n")
    print(tabulate(cart, headers=["Item", "Quantity", "Price"],floatfmt=[".0f",".0f",".2f"]))

def display_checkout_cart(final_cart):
    print("Your Cart Receipt: \n")
    print(tabulate(final_cart, headers=["Item", "Quantity", "Price","Total Price","Discount(%)","Total Discounted Price"],floatfmt=[".0f",".0f",".2f",".2f",".2f",".2f"]))
