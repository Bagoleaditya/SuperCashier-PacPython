from tabulate import tabulate



def cashier_menu():
    print("-"*30)
    print("Ojo Kendor Menu: ")
    print("-"*30)
    print("1. Add item to cart")
    print("2. Update item from cart")
    print("3. Delete item from cart")
    print("4. Reset cart")
    print("5. Check order from your cart")
    print("-"*30)

    return cashier_menu

def display_cart(cart):
    cart['total'] = cart['quantity']*cart['price']
    print(tabulate(cart, headers=["Item", "Quantity", "Price","Total"]))
