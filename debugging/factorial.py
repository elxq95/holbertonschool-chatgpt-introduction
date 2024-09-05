#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n to eventually break out of the loop
    return result

# Ensure there is at least one argument passed
if len(sys.argv) < 2:
    print("Usage: {} <number>".format(sys.argv[0]))
    sys.exit(1)

# Try to convert the input to an integer
try:
    number = int(sys.argv[1])
except ValueError:
    print("Please provide a valid integer.")
    sys.exit(1)

# Calculate the factorial and print the result
f = factorial(number)
print(f)
