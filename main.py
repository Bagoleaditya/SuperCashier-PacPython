from src.function import *
from src.menu import *
from src.db import insert_to_db

#Create Transaction ID
transaction_id = transaction()
print(f"Your ID transaction is : {transaction_id}")


cart = pd.DataFrame(columns=['quantity', 'price'])
pd.set_option('display.float_format', '{:.2f}'.format)

#Prompt Cashier Menu

while True:
    cashier_menu()
    menu = input("Please choose menu (1-7): \n")
    print("\n")
    try:
        if menu == '1': #Add item to DataFrame
            add_item(cart)
            display_cart(cart)
            
            
        elif menu == '2': #Update item in the DataFrame
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
                        new_name = input("1. Please input new item name: ").upper()
                        new_qty = input("2. Please input new quantity: ")
                        new_price = input("3. Please input new price: ")

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
        elif menu == '3': #Delete item in the DataFrame
            display_cart(cart)  
            while True:
                item_name = input('Pick item you want to delete : ').upper()
                if item_name not in cart.index:
                   print("Selected item didn't exist")
                else:
                    delete_item(cart,item_name)
                    display_cart(cart)
                    break
        
        elif menu == '4': #Delete all items in the DataFrame
            reset_cart(cart)
            display_cart(cart)
        
        elif menu == '5': #Display items in the DataFrame
            display_cart(cart)

        elif menu == '6': #Calculate and Checkout order
            final_cart = cart.copy()

            calculate_total_price(final_cart)
            discount(final_cart)
            calculate_discount_price(final_cart)
            
            display_checkout_cart(final_cart)
            final_cart.reset_index(inplace=True)
            final_cart['transaction_id'] = transaction_id
            total_pay = final_cart['disc_price'].sum()

            print(f"\n The total order amount is {total_pay}. \n Please pay in 30 minutes to Ojo Bank Account Number: 112233445566")

            #insert cart order into database
            insert_to_db(final_cart)

        elif menu == '7': #Exit Program
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