#My first ALX shopping list manager in python.
def display_menu():
    """
    Display the menu options for the shopping list manager.
    """
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """
    Main function to manage the shopping list.
    """
    shopping_list = []  # Correctly implemented as an array (list)

    while True:
        display_menu()  # Correctly calling the display_menu function
        try:
            choice = int(input("Enter your choice: "))  # Ensures choice input is a number
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the menu options.")
            continue

        if choice == 1:
            # Add an item to the list
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to the list.")
            else:
                print("Item name cannot be empty.")

        elif choice == 2:
            # Remove an item from the list
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the list.")
            else:
                print(f"'{item}' is not in the shopping list.")

        elif choice == 3:
            # View the shopping list
            if shopping_list:
                print("\nShopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("The shopping list is currently empty.")

        elif choice == 4:
            # Exit the program
            print("Goodbye!")
            break

        else:
            # Handle invalid numeric choice
            print("Invalid choice. Please select a valid menu option.")

if __name__ == "__main__":
    main()


