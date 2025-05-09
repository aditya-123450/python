import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 for complexity.")
        return None
    
    # Define character sets for complexity
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Combine all characters
    all_chars = lowercase + uppercase + digits + special

    # Ensure at least one character from each set is included
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_chars, k=length - 4)

    # Shuffle to ensure randomness
    random.shuffle(password)

    return ''.join(password)

# Get user input
try:
    length = int(input("Enter the desired password length: "))
    password = generate_password(length)
    if password:
        print("Generated Password:", password)
except ValueError:
    print("Please enter a valid number.")
