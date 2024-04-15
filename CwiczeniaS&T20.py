def exercise1():
    # Code for exercise 1
    def find_numbers():
        results = []
        for number in range(1500, 2701):
            if number % 7 == 0 and number % 5 == 0:
                results.append(number)
        return results

    # Collect and print the numbers
    numbers = find_numbers()
    print("Numbers divisible by 7 and multiple of 5 between 1500 and 2700:", numbers)
def exercise2():
    # Code for exercise 2
    def convert_temperature(temp, scale):
        if scale.lower() == 'celsius':
            # Convert Celsius to Fahrenheit
            return f"{temp}°C is {int(temp * 9 / 5 + 32)} in Fahrenheit"
        elif scale.lower() == 'fahrenheit':
            # Convert Fahrenheit to Celsius
            return f"{temp}°F is {int((temp - 32) * 5 / 9)} in Celsius"
        else:
            return "Invalid scale provided. Please use 'Celsius' or 'Fahrenheit'."

    # Example conversions
    print(convert_temperature(60, 'Celsius'))
    print(convert_temperature(45, 'Fahrenheit'))
def exercise3():
    import random

    def guess_number():
        number_to_guess = random.randint(1, 9)
        while True:
            user_guess = int(input("Guess a number between 1 and 9: "))
            if user_guess == number_to_guess:
                print("Well guessed!")
                break

    # Run the guessing game
    guess_number()
def exercise4():
    def print_star_pattern():
        # Print the upper part of the pattern
        for i in range(1, 6):
            print('* ' * i)
        # Print the lower part of the pattern
        for i in range(4, 0, -1):
            print('* ' * i)

    # Print the star pattern
    print_star_pattern()
def exercise5():
    def reverse_word():
        word = input("Enter a word to reverse: ")
        reversed_word = word[::-1]
        print("Reversed word:", reversed_word)

    # Run the function to reverse a word
    reverse_word()
def exercise6():
    def count_even_odd(numbers):
        even_count = 0
        odd_count = 0
        for number in numbers:
            if number % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        print("Number of even numbers :", even_count)
        print("Number of odd numbers :", odd_count)

    # Sample numbers
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    # Count even and odd numbers
    count_even_odd(numbers)
def exercise7():
    def print_items_and_types(datalist):
        for item in datalist:
            print(f"Item: {item}, Type: {type(item)}")

    # Sample list with various types of elements
    datalist = [1452, 11.23, 1 + 2j, True, 'w3resource', (0, -1), [5, 12], {"class": 'V', "section": 'A'}]

    # Print each item and its type
    print_items_and_types(datalist)
def exercise8():
    def print_selected_numbers():
        for num in range(7):  # Range is from 0 to 6
            if num == 3 or num == 6:
                continue
            print(num, end=' ')

    # Execute the function
    print_selected_numbers()
def exercise9():
    def fibonacci_series(limit):
        # Start with the first two Fibonacci numbers
        a, b = 0, 1
        while b <= limit:
            print(b, end=' ')
            a, b = b, a + b  # Update values for the next iteration

    # Print Fibonacci numbers up to 50
    fibonacci_series(50)
def exercise10():
    def fizz_buzz(limit):
        for num in range(1, limit + 1):
            if num % 3 == 0 and num % 5 == 0:
                print("FizzBuzz")
            elif num % 3 == 0:
                print("Fizz")
            elif num % 5 == 0:
                print("Buzz")
            else:
                print(num)

    # Execute FizzBuzz for numbers from 1 to 50
    fizz_buzz(50)
def exercise11():
    def generate_2d_array(rows, columns):
        return [[i * j for j in range(columns)] for i in range(rows)]

    # Example usage
    rows = 3
    columns = 4
    result_array = generate_2d_array(rows, columns)
    print("Generated 2D Array:")
    for row in result_array:
        print(row)
def exercise12():
    def accept_and_print_lines():
        lines = []
        print("Enter text (leave a blank line to stop):")
        while True:
            line = input()
            if line:
                lines.append(line.lower())
            else:
                break
        print("\nAll lines in lower case:")
        for line in lines:
            print(line)

    # Execute the function to read and print lines
    accept_and_print_lines()
def exercise13():
    def filter_binaries_divisible_by_five(data):
        # Split the input string by commas
        binaries = data.split(',')
        # Filter binaries divisible by 5
        divisible_by_five = [binary for binary in binaries if int(binary, 2) % 5 == 0]
        # Return the result as a comma-separated string
        return ','.join(divisible_by_five)

    # Sample data
    sample_data = "0100,0011,1010,1001,1100,1001"
    result = filter_binaries_divisible_by_five(sample_data)
    print("Output:", result)
def exercise14():
    def count_digits_and_letters(s):
        digits = sum(c.isdigit() for c in s)
        letters = sum(c.isalpha() for c in s)
        return digits, letters

    # Sample data
    sample_string = "Python 3.2"
    digits, letters = count_digits_and_letters(sample_string)
    print(f"Letters {letters}")
    print(f"Digits {digits}")
def exercise15():
    import re

    def validate_password(password):
        if len(password) < 6 or len(password) > 16:
            return False
        if not re.search("[a-z]", password):
            return False
        if not re.search("[A-Z]", password):
            return False
        if not re.search("[0-9]", password):
            return False
        if not re.search("[$#@]", password):
            return False
        return True

    # Test the function with sample passwords
    sample_passwords = ['Passw0rd$', 'weakpassword', 'StrongPassword123#', '123456', 'aA1$']
    for password in sample_passwords:
        if validate_password(password):
            print(f"'{password}' is a valid password.")
        else:
            print(f"'{password}' is not a valid password.")
def exercise16():
    def find_even_digit_numbers():
        even_digit_numbers = []
        for num in range(100, 401):
            if all(int(digit) % 2 == 0 for digit in str(num)):
                even_digit_numbers.append(str(num))
        return ', '.join(even_digit_numbers)

    # Print numbers with even digits between 100 and 400
    print("Numbers with even digits:", find_even_digit_numbers())
def exercise17():
    def print_pattern_a():
        for row in range(7):
            for col in range(5):
                if (row == 0 and col in {1, 2, 3}) or (row in {1, 2, 3, 4, 5} and col in {0, 4}) or (
                        row == 6 and col != 0 and col != 4):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

    # Print the 'A' pattern
    print("Alphabet Pattern 'A':")
    print_pattern_a()
def exercise18():
    def print_pattern_d():
        for row in range(7):
            for col in range(5):
                if (row in {0, 6} and col != 4) or (row in {1, 2, 3, 4, 5} and col in {0, 4}) or (
                        col == 4 and row in {1, 5}):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

    # Print the 'D' pattern
    print("Alphabet Pattern 'D':")
    print_pattern_d()
def exercise19():
    def print_pattern_e():
        for row in range(7):
            for col in range(5):
                if (row in {0, 3, 6}) or (row in {1, 2, 4, 5} and col == 0):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

    # Print the 'E' pattern
    print("Alphabet Pattern 'E':")
    print_pattern_e()
def exercise20():
    def print_pattern_g():
        for row in range(7):
            for col in range(5):
                if (row in {0, 6} and col in {1, 2, 3}) or (row == 1 and col == 0) or (row == 5 and col in {0, 4}) or (
                        row == 3 and col > 1) or (col == 0 and row > 1 and row < 5):
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

    # Print the 'G' pattern
    print("Alphabet Pattern 'G':")
    print_pattern_g()
def get_exercise_function(name):
    # Dictionary mapping exercise names to functions
    exercises = {
        'exercise1': exercise1,
        'exercise2': exercise2,
        'exercise3': exercise3,
        'exercise4': exercise4,
        'exercise5': exercise5,
        'exercise6': exercise6,
        'exercise7': exercise7,
        'exercise8': exercise8,
        'exercise9': exercise9,
        'exercise10': exercise10,
        'exercise11': exercise11,
        'exercise12': exercise12,
        'exercise13': exercise13,
        'exercise14': exercise14,
        'exercise15': exercise15,
        "exercise16": exercise16,
        "exercise17": exercise17,
        "exercise18": exercise18,
        "exercise19": exercise19,
        "exercise20": exercise20,
    }
    return exercises.get(name)


def main():
    while True:
        # Prompt for entering the exercise name
        exercise_name = input("Enter the exercise name (e.g., 'exercise1') or 'exit' to quit: ")
        if exercise_name == 'exit':
            break

        # Retrieve the function based on the name
        exercise_function = get_exercise_function(exercise_name)
        if exercise_function:
            result = exercise_function()
            print(result)
        else:
            print("No exercise found with that name.")

# This makes sure the script can be run directly, and main() will be executed
if __name__ == "__main__":
    main()