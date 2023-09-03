from src.function import *
from src.menu import *

transaction_id = transaction()

#cashier_menu()

cart = pd.DataFrame(columns=['quantity', 'price'])
pd.set_option('display.float_format', '{:.2f}'.format)

while True:
    cashier_menu()
    menu = input("Please choose menu (1-7): \n")
    try:
        if menu == '1': 
            add_item(cart)
            display_cart(cart)
            
            
        elif menu == '2':
            cashier_menu()
            while True:
                display_cart(cart)
                item_name = input("Which item you want to update? (type 'no' to cancel) \n").upper()
                if item_name == 'no':
                    break
                elif item_name not in cart.index:
                    print("Item not found, check your input")
                    continue
                else:
                    while True:
                        new_name = input("1. Please input new item name: \n").upper()
                        new_qty = input("2. Please input new quantity: \n")
                        new_price = input("3. Please input new price: \n")

                        update_item_name(cart,item_name,new_name)

                        try:
                            new_qty = int(new_qty)
                            if new_qty <= 0:
                                print("Please input positive number")
                            else:
                                update_item_qty(cart,new_name,new_qty)
                        except ValueError:
                            print("Please input the correct quantity")

                        try:
                            new_price = float(new_price)
                            if new_price <=0:
                                print("Please input positive number")
                            else:
                                update_item_price(cart,new_name,new_price)
                        except ValueError:
                            print("Please input the correct price")
                        
                        display_cart(cart)
                        break




            
        
        # elif menu == '3':
        #     delete_item(cart)
        
        # elif menu == '4':
        #     reset_cart(cart)

        # elif menu == '5':
        #     display_item_prices_column(cart)
        #     break


    except Exception as e:
        print(f"ERROR: {e}")