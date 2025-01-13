# Global Conversion Factors for the two function.
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # Conversion factor for Fahrenheit to Celsius
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # Conversion factor for Celsius to Fahrenheit

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    Uses the global FAHRENHEIT_TO_CELSIUS_FACTOR for conversion.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    Uses the global CELSIUS_TO_FAHRENHEIT_FACTOR for conversion.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def user_interaction():
    """
    Handles user input and performs temperature conversion.
    Implements error handling for invalid inputs.
    """
    try:
        # Prompt the user for temperature
        temperature = input("Enter the temperature to convert: ")
        if not temperature.replace('.', '', 1).isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        temperature = float(temperature)

        # Prompt the user for the unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            # Convert Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp:.2f}°F")
        elif unit == 'F':
            # Convert Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp:.2f}°C")
        else:
            # Raise an error for invalid unit
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as ve:
        # Handle invalid input (non-numeric or invalid unit)
        print(f"Error: {ve}")

if __name__ == "__main__":
    user_interaction()

