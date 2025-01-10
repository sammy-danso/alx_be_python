#My first arithmetic operation in python.

def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations based on the given operation.

    Parameters:
    - num1: First number (float)
    - num2: Second number (float)
    - operation: Operation to perform ('add', 'subtract', 'multiply', 'divide')

    Returns:
    - Result of the operation, or a message for division by zero.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Cannot divide by zero."
        return num1 / num2
    else:
        return "Error: Invalid operation."
