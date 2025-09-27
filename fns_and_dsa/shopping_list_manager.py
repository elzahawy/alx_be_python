# shopping_list_manager.py

def display_menu():
    """Displays the menu options to the user."""
    print("\n--- Shopping List Manager ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print("----------------------------")

def main():
    """
    Main function to run the shopping list manager application.
    It uses a loop to continuously display the menu and process user choices.
    """
    # 1. Your script should start with an empty list named shopping_list.
    shopping_list = []
    
    # 2. Use a loop to continuously display a menu... until they choose to exit.
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            # Prompt for and add an item
            item_to_add = input("Enter the item to add: ").strip()
            if item_to_add:
                # For adding items, prompt the user for the item name and append it to shopping_list.
                shopping_list.append(item_to_add)
                print(f"'{item_to_add}' has been added to the list.")
            else:
                print("Item name cannot be empty.")
            
        elif choice == '2':
            # Prompt for and remove an item
            if not shopping_list:
                print("The shopping list is already empty. Nothing to remove.")
                continue

            item_to_remove = input("Enter the item to remove: ").strip()
            
            if not item_to_remove:
                print("Item name cannot be empty.")
                continue

            try:
                # For removing items, ask the user for the item name and remove it from shopping_list.
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' has been removed from the list.")
            except ValueError:
                # If the item is not found, display a message indicating so.
                print(f"'{item_to_remove}' was not found in the list.")
            
        elif choice == '3':
            # Display the shopping list
            # To view the list, print each item in shopping_list to the console.
            if shopping_list:
                print("\n--- Current Shopping List ---")
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
                print("-----------------------------")
            else:
                print("\nYour shopping list is currently empty.")
            
        elif choice == '4':
            print("Thank you for using the Shopping List Manager. Goodbye! 👋")
            # Exit the loop
            break 
            
        else:
            # Ensure your script handles invalid menu choices gracefully.
            print("❌ Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()