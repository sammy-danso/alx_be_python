#My first ALX shopping list manager in python.

def display_menu():
    """
    Display the menu options for the shopping list manager.
    """
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """
    Main function to manage the shopping list.
    """
    shopping_list = []  # Initializing an empty shopping list

    while True:
        display_menu()  # Displaying the menu
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            # Adding an item to the list
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to the list.")
            else:
                print("Item name cannot be empty.")

        elif choice == '2':
            # Removing an item from the list
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the list.")
            else:
                print(f"'{item}' is not in the shopping list.")

        elif choice == '3':
            # Viewing the shopping list
            if shopping_list:
                print("\nShopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("The shopping list is currently empty.")

        elif choice == '4':
            # Exiting the program
            print("Goodbye!")
            break

        else:
            # Handling invalid input
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

