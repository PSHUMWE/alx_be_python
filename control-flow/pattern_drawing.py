# pattern_drawing.py

# Prompt user to input the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop: while loop to handle each row
while row < size:
    # Inner loop: for loop to print stars in one row
    for column in range(size):
        print("*", end="")  # Print star without newline
    print()  # Move to the next line after each row
    row += 1  # Move to the next row

