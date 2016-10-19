"""
Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
Once 'done' is entered, print out the largest and smallest of the numbers.
If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message
and ignore the number. Enter the numbers from the book for problem 5.1 and Match the desired output as shown.
"""

largest = None
smallest = None

while True:
    num = raw_input("Enter a number or type 'done' to quit: ")

    # Check if user entered done to exit the loop
    if num.lower() == "done":
        break

    # Attempt to convert input string to an integer
    try:
        num = int(num)
    except ValueError:
        print "Invalid input"
        continue

    # Check for largest number
    if largest is None:
        largest = num
    elif num > largest:
        largest = num

    # Check for the smallest number
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num

# After program exits print our largest and smallest numbers
print "Maximum is", largest
print "Minimum is", smallest
