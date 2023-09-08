from src.function import *
from src.menu import *
from src.db import insert_to_db

transaction_id = transaction()
print(transaction_id)

#cashier_menu()

cart = pd.DataFrame(columns=['quantity', 'price'])
pd.set_option('display.float_format', '{:.2f}'.format)


while True:
    cashier_menu()
    menu = input("Please choose menu (1-7): \n")
    print("\n")
    try:
        if menu == '1': 
            add_item(cart)
            display_cart(cart)
            
            
        elif menu == '2':
            cashier_menu()
            while True:
                display_cart(cart)
                item_name = input("Which item you want to update? (type 'no' to cancel) \n").upper()
                if item_name == 'NO':
                    break
                elif item_name not in cart.index:
                    print("Item not found, check your input \n")
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
        elif menu == '3':
            display_cart(cart)
            #print("Pick item you want to delete. \n")
            while True:
                item_name = input('Pick item you want to delete : \n').upper()
                if item_name not in cart.index:
                   print("Selected item didn't exist")
                else:
                    delete_item(cart,item_name)
                    display_cart(cart)
                    break
        
        elif menu == '4':
            reset_cart(cart)
            display_cart(cart)
        
        elif menu == '5':
            display_cart(cart)

        elif menu == '6':
            #display_cart(cart)
            final_cart = cart.copy()

            
            calculate_total_price(final_cart)
            discount(final_cart)
            calculate_discount_price(final_cart)
            
            display_checkout_cart(final_cart)
            final_cart.reset_index(inplace=True)
            final_cart['transaction_id'] = transaction_id
            print(final_cart)
            #print(final_cart)

            #insert cart order into database
            insert_to_db(final_cart)

        elif menu == '7':
            print('-'*44)
            print('='*44)
            print("Thank you for shopping with Ojo Kendor Mart!")
            print('='*44)
            print('-'*44)
            break
        else:
            raise ValueError("The Menu choice is not available. Please choose 1-7")
        

 

    except Exception as e:
        print(f"ERROR: {e}")