import pandas as pd
import numpy as np

# ----------------------------------
# MENU stored using DICTIONARY
# ----------------------------------
menu = {
    "Burger": 80,
    "Pizza": 150,
    "Pasta": 120,
    "Coffee": 60,
    "Sandwich": 70
}

# Convert menu to Pandas DataFrame
menu_df = pd.DataFrame(list(menu.items()), columns=["Item", "Price"])

# ----------------------------------
# Function: Show Menu
# ----------------------------------
def show_menu():
    print("\n----- MENU -----")
    print(menu_df.to_string(index=False))


# ----------------------------------
# Function: Take Order
# ----------------------------------
def take_order():
    order_list = []
    price_list = []

    print("\nEnter items one by one (type 'done' to finish):")

    while True:
        item = input("Enter Item: ").title()

        if item == "Done":
            break

        if item in menu:
            order_list.append(item)
            price_list.append(menu[item])
            print(f"{item} added!")
        else:
            print("Item not available in menu!")

    return order_list, price_list


# ----------------------------------
# Function: Generate Bill using NumPy
# ----------------------------------
def generate_bill(order_list, price_list):
    print("\n----- BILL -----")
    bill_df = pd.DataFrame({
        "Item": order_list,
        "Price": price_list
    })

    # Use NumPy to calculate total price
    total_amount = np.sum(price_list)

    print(bill_df.to_string(index=False))
    print(f"\nTotal Amount: ₹{total_amount}")
    print("-------------------")


# ----------------------------------
# MAIN PROGRAM
# ----------------------------------
def main():
    print("\n===== Restaurant Management System =====")

    while True:
        print("\n1. Show Menu")
        print("2. Take Order")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            show_menu()

        elif choice == "2":
            orders, prices = take_order()
            generate_bill(orders, prices)

        elif choice == "3":
            print("Thank you for visiting!")
            break

        else:

            print("Invalid choice. Try again!")


# Run program
main()