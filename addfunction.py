def add_and_print(a, b):
    # This function just shows the result
    print(a + b)

def add_and_return(a, b):
    # This function gives the result back
    return a + b

# Using the print function
print("Calling add_and_print:")
result1 = add_and_print(5, 3) # This prints 8
print(f"The value of result1 is: {result1}") # Prints: The value of result1 is: None

# Using the return function
print("\nCalling add_and_return:")
result2 = add_and_return(5, 3) # This does NOT print anything
print(f"The value of result2 is: {result2}") # Prints: The value of result2 is: 8