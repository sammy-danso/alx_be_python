def user_interaction():
    """
    Handles user input and performs temperature conversion.
    Implements error handling for invalid inputs.
    """
    try:
        # Prompt the user for temperature
        temperature = float(input("Enter the temperature to convert: "))
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

