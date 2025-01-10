#my first time creating date and time prompt in alx python class.

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in a readable format (YYYY-MM-DD HH:MM:SS).
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """
    Calculate and display the future date after adding a specified number of days.
    """
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days_to_add)
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Invalid input. Please enter a valid integer for the number of days.")

def main():
    """
    Main function to execute the datetime operations.
    """
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()

