# shopping_list_manager.py

# Global array for shopping list
shopping_list = []

# Function to display the menu
def display_menu():
    print("\nShopping List Manager")
    print("1. View shopping list")
    print("2. Add item")
    print("3. Remove item")
    print("4. Exit")

# Main program
while True:
    display_menu()  # ✅ Call display_menu
    try:
        choice = int(input("Enter your choice (1-4): "))  # ✅ Choice input as number
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 4.")
        continue

    if choice == 1:
        if not shopping_list:
            print("Your shopping list is empty.")
        else:
            print("Your shopping list:")
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")

    elif choice == 2:
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f"'{item}' added to your shopping list.")

    elif choice == 3:
        if not shopping_list:
            print("Your shopping list is empty. Nothing to remove.")
        else:
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")
            try:
                remove_index = int(input("Enter the number of the item to remove: "))
                if 1 <= remove_index <= len(shopping_list):
                    removed = shopping_list.pop(remove_index - 1)
                    print(f"'{removed}' removed from your shopping list.")
                else:
                    print("Invalid item number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == 4:
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
