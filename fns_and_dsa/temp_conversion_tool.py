# Define global conversion factors
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main function for user interaction
def main():
    try:
        # Prompt user for temperature input
        temp = input("Enter the temperature to convert (e.g., 100): ")
        
        # Check if the input is numeric
        if not temp.replace('.', '', 1).isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        
        temp = float(temp)
        
        # Prompt user to specify the unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit == "C":
            # Convert Celsius to Fahrenheit
            result = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {result:.2f}°F")
        elif unit == "F":
            # Convert Fahrenheit to Celsius
            result = convert_to_celsius(temp)
            print(f"{temp}°F is {result:.2f}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(e)

# Entry point of the script
if __name__ == "__main__":
    main()

