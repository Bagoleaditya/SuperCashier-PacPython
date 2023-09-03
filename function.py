from tabulate import tabulate
import pandas as pd

def main_menu():
    """
    This function show super cashier features
    """

    print("Super Cashier Menu:")
    print("-"*40)
    print("1. Add item to cart")
    print("2. Update item from cart")
    print("3. Delete item from cart")
    print("4. Reset transaction")
    print("5. Check order")
    print("6. Checkout order")
    print("7. Generate invoice order")
    print("8. Exit")
    print("-"*40)


def add_item(cart):
    while True:
        try:
            item_name = input("Masukkan nama barang, atau ketik 'stop' untuk selesai: ")
            if item_name.lower() == 'stop':
                break
            item_amount = int(input("Enter item amount: "))
            item_price = float(input("Enter item price: "))
        except ValueError:
            print("Invalid input. Please try again.")
            return
        cart[item_name] = {"amount": item_amount, "price": item_price}

cart = {}
add_item(cart)
cart_df = pd.DataFrame(cart,)
print(tabulate(cart_df,headers=["item_name","amount_item","item_price"]))