def process_data(data):
    try:
        # Convert to integer
        num = int(data)
        
        # Access list element
        my_list = [1, 2, 3]
        value = my_list[num]
        
        # Perform division
        result = 100 / value
        return result

    except ValueError:
        print("Invalid input: Cannot convert to integer")
    except IndexError:
        print("Index out of range")
    except ZeroDivisionError:
        print("Cannot divide by zero")
