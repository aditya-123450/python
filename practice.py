#Write a program that keeps asking the user to enter a password until they enter a password that:
# at least 8 characters long
#contains at least one uppercase letter
#Contains at least one digit Use a whileloop and display appropriate messages for invalid passwords.

while True:
    password = input("Enter a password: ")

    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        continue

    if not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
        continue

    if not any(char.isdigit() for char in password):
        print("Password must contain at least one digit.")
        continue

    print("Password is valid!")
    break

2. #Create a program that prints the following pattern using nested loops:

rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()

#3. Question 
#List Processing
#Given a list of numbers
#[12, 7, 23, 8, 19, 4, 31, 15]
# write a program using loops to:
#Find and print all even numbers
#Calculate the sum of numbers greater than 10
#Count how many numbers are divisible by 3

# Given list
numbers = [12, 7, 23, 8, 19, 4, 31, 15]

# Variables for sum and count
sum_greater_than_10 = 0
count_divisible_by_3 = 0

print("Even numbers:")
for num in numbers:
    # Check for even numbers
    if num % 2 == 0:
        print(num)
    
    # Sum of numbers greater than 10
    if num > 10:
        sum_greater_than_10 += num
    
    # Count numbers divisible by 3
    if num % 3 == 0:
        count_divisible_by_3 += 1

# Output results
print("\nSum of numbers greater than 10:", sum_greater_than_10)
print("Count of numbers divisible by 3:", count_divisible_by_3)

4.# Write a program that takes a sentence as input and uses loops to:
#Count the number of vowels (a, e, i, o, u)
#Replace all spaces with underscores
#Print each word on a separate line

sentence = input("Enter a sentence: ")

# Count vowels
vowels = 'aeiouAEIOU'
vowel_count = 0
for char in sentence:
    if char in vowels:
        vowel_count += 1

# Replace spaces with underscores
replaced_sentence = ""
for char in sentence:
    if char == ' ':
        replaced_sentence += '_'
    else:
        replaced_sentence += char

# Print each word on a new line
print("\n--- Output ---")
print("Number of vowels:", vowel_count)
print("With underscores:", replaced_sentence)
print("Words on separate lines:")
for word in sentence.split():
    print(word)


5. #Create a program that generates a multiplication table for numbers 1-10 using nested loops and formatsit nicely:
11
2222
333333
44444444
55555

# Multiplication Table Pattern
for i in range(1, 6):  # 1 to 5 for 5 rows as in the sample pattern
    print(str(i) * (i * 2 - 1))


6. #Write a function calculate_grade(marks) that:
#Takes a list of marks as input
#Returns the average and letter grade (A: 90+, B: 80-89, C: 70-79, D: 60-69, F: <60)
#Handles empty lists appropriately

def calculate_grade(marks):
    if not marks:
        return "No marks provided", None

    average = sum(marks) / len(marks)

    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'

    return average, grade

# Example usage:
marks_list = [85, 92, 78, 88]
avg, grade = calculate_grade(marks_list)
print(f"\nAverage: {avg}")
print(f"Grade: {grade}")


7. #Create a function is_prime(n)that checks if a number is prime. Then write another function
#get_primes_in_range(start, end)
#that returns a list of all prime numbers in a given range.

print("Is 17 prime?", is_prime(17))  # True
print("Prime numbers between 10 and 50:", get_primes_in_range(10, 50))

8.#Write the following functions: count_words(text): Returns the number of words in a string
#reverse_words(text)
#: Returns the string with words in reverse order
#capitalize_words(text)
#: Capitalizes the first letter of each word
#Test all functions with sample inputs

sample_text = "hello world this is python programming"

print("Original Text:", sample_text)
print("Word Count:", count_words(sample_text))
print("Reversed Words:", reverse_words(sample_text))
print("Capitalized Words:", capitalize_words(sample_text))

9. #Create functions for:
#find_max_min(numbers)
#: Returns a tuple with (max, min) values
#remove_duplicates(items)
#: Returns a list with duplicates removed
#get_common_elements(list1, list2)
#: Returns common elements between two lists

numbers = [10, 20, 30, 10, 40, 30, 50]
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Testing all functions
max_val, min_val = find_max_min(numbers)
print("Max:", max_val, "Min:", min_val)

print("Without duplicates:", remove_duplicates(numbers))
print("Common elements:", get_common_elements(list1, list2))

10.#Write a recursive function factorial(n)
#that calculates the factorial of a number. Also create an iterativeversion and compare their performance for large numbers.

import time

n = 500  # You can increase this value to test performance

# Measure recursive time
start = time.time()
try:
    recursive_result = factorial_recursive(n)
    recursive_time = time.time() - start
except RecursionError:
    recursive_result = "RecursionError"
    recursive_time = "Too Deep"

# Measure iterative time
start = time.time()
iterative_result = factorial_iterative(n)
iterative_time = time.time() - start

# Display results
print(f"Recursive Result: {str(recursive_result)[:10]}... in {recursive_time} seconds")
print(f"Iterative Result: {str(iterative_result)[:10]}... in {iterative_time} seconds")
