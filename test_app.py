def main():
    cashier = Cashier()

    while True:
        print("\nOptions:")
        print("1. Set transaction ID")
        print("2. Add item")
        print("3. Update item")
        print("4. Delete item")
        print("5. Reset transaction")
        print("6. Check order")
        print("7. Apply discount")
        print("8. Generate invoice")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            phone = input("Enter customer phone number: ")
            cashier.set_transaction_id(name, phone)
            print(f"Transaction ID: {cashier.transaction_id}")

        elif choice == "2":
            while True:
                item_name = input("Enter item name (or type 'exit' to return to main menu): ")
                if item_name.lower() == 'exit':
                    break
                item_amount = int(input("Enter item amount: "))
                item_price = float(input("Enter item price: "))
                cashier.add_item(item_name, item_amount, item_price)

        elif choice == "3":
            item_name = input("Enter item name: ")
            item_amount = input("Enter new item amount (press Enter to skip): ")
            item_price = input("Enter new item price (press Enter to skip): ")
            item_amount = int(item_amount) if item_amount else None
            item_price = float(item_price) if item_price else None
            cashier.update_item(item_name, item_amount, item_price)

        elif choice == "4":
            item_name = input("Enter item name to delete: ")
            cashier.delete_item(item_name)

        elif choice == "5":
            cashier.reset_transaction()

        elif choice == "6":
            print(cashier.check_order())

        elif choice == "7":
            threshold = float(input("Enter discount threshold: "))
            discount_percentage = float(input("Enter discount percentage: "))
            cashier.apply_discount(threshold, discount_percentage)

        elif choice == "8":
            print(cashier.generate_invoice())

        elif choice == "9":
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
