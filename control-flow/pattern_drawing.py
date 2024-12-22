# pattern_drawing.py

# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a row counter
row = 0

# Use a while loop to iterate through rows
while row < size:
    # Use a for loop to print asterisks (*) for the current row
    for col in range(size):
        print("*", end="")  # Print asterisk without a newline
    print()  # Move to the next line after each row
    row += 1

