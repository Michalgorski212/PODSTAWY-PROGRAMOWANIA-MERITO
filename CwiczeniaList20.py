def exercise1():
    # Code for exercise 1
    def sum_list(lst):
        return sum(lst)

    # Example usage:
    numbers = [1, 2, 3, 4, 5]
    total_sum = sum_list(numbers)
    return (total_sum)
def exercise2():
    # Code for exercise 2
    def multiply_list(lst):
        product = 1
        for number in lst:
            product *= number
        return product

    # Example usage:
    list_of_numbers = [1, 2, 3, 4, 5]
    result = multiply_list(list_of_numbers)
    print(result)  # This should print 120, which is the product of the numbers in the list
def exercise3():
    def max_number(lst):
        return max(lst)

    # Example usage:
    list_of_numbers = [1, 2, 3, 4, 5]
    largest = max_number(list_of_numbers)
    print(largest)  # This should print 5, which is the largest number in the list
def exercise4():
    def min_number(lst):
        return min(lst)

    # Example usage:
    list_of_numbers = [10, 22, 37, 4, 59]
    smallest = min_number(list_of_numbers)
    print(smallest)  # This should print the smallest number in the list
def exercise5():
    def count_matching_ends(lst):
        return sum(1 for s in lst if len(s) >= 2 and s[0] == s[-1])

    # Example usage:
    list_of_strings = ['abc', 'xyz', 'aba', '1221']
    matching_ends = count_matching_ends(list_of_strings)
    print(matching_ends)  # This should print 2, according to the expected result
def exercise6():
    def sort_tuples_by_last_element(tuples_list):
        # Sort the list of tuples based on the last element of each tuple
        return sorted(tuples_list, key=lambda x: x[-1])

    # Example usage
    sample_tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    sorted_tuples = sort_tuples_by_last_element(sample_tuples)
    print(sorted_tuples)
def exercise7():
    def remove_duplicates(lst):
        return list(set(lst))

    # Example usage
    sample_list = [1, 2, 3, 2, 1, 4, 5, 4]
    unique_items = remove_duplicates(sample_list)
    print(unique_items)  # This will print a list without duplicates, e.g., [1, 2, 3, 4, 5]
def exercise8():
    def is_list_empty(lst):
        return not lst  # Returns True if the list is empty, False otherwise

    # Example usage
    empty_list = []
    non_empty_list = [1, 2, 3]
    print(is_list_empty(empty_list))  # This will print True
    print(is_list_empty(non_empty_list))  # This will print False
def exercise9():
    # Create a list 'original_list' with some elements
    original_list = [10, 22, 44, 23, 4]

    # Create a new list 'new_list' and copy the elements from 'original_list' into it
    new_list = list(original_list)

    # Print the contents of the 'original_list'
    print(original_list)

    # Print the contents of the 'new_list', which is a copy of 'original_list'
    print(new_list)
def exercise10():
    # Define a function called 'long_words' that takes an integer 'n' and a string 'str' as input
    def long_words(n, str):
        # Create an empty list 'word_len' to store words longer than 'n' characters
        word_len = []

        # Split the input string 'str' into a list of words using space as the delimiter
        txt = str.split(" ")

        # Iterate through each word 'x' in the list of words 'txt'
        for x in txt:
            # Check if the length of the current word 'x' is greater than 'n'
            if len(x) > n:
                # If the word is longer than 'n' characters, add it to the 'word_len' list
                word_len.append(x)

        # Return the list of words longer than 'n' characters
        return word_len

    # Call the 'long_words' function with an 'n' value of 3 and a string as input, and print the result
    print(long_words(3, "The quick brown fox jumps over the lazy dog"))
def exercise11():
    def has_common_member(list1, list2):
        return any(elem in list2 for elem in list1)

    # Example usage
    list_a = [1, 2, 3, 4, 5]
    list_b = [5, 6, 7, 8, 9]
    list_c = [10, 11, 12]

    # Check if list_a and list_b have any common members
    common_ab = has_common_member(list_a, list_b)  # This should return True

    # Check if list_a and list_c have any common members
    common_ac = has_common_member(list_a, list_c)  # This should return False

    print(common_ab)
    print(common_ac)
def exercise12():
    def remove_elements(lst, indices):
        return [item for idx, item in enumerate(lst) if idx not in indices]

    sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    # Remove the 0th, 4th, and 5th items
    indices_to_remove = [0, 4, 5]
    updated_list = remove_elements(sample_list, indices_to_remove)
    print(updated_list)
def exercise13():
    def generate_3d_array():
        return [[['*' for _ in range(6)] for _ in range(4)] for _ in range(3)]

    array_3d = generate_3d_array()
    for layer in array_3d:
        print(layer)
def exercise14():
    def remove_even_numbers(lst):
        return [n for n in lst if n % 2 != 0]

    # Example list
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Remove even numbers
    odd_numbers = remove_even_numbers(numbers)
    print(odd_numbers)
def exercise15():
    import random

    def shuffle_list(lst):
        random.shuffle(lst)
        return lst

    # Example usage
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    shuffled_list = shuffle_list(my_list.copy())
    print(shuffled_list)
def exercise16():
    def generate_square_numbers():
        square_numbers = [i ** 2 for i in range(1, 31) if i ** 2 <= 30]
        # Getting the first and last 5 square numbers
        return square_numbers[:5] + square_numbers[-5:]

    # Call the function and print the result
    print(generate_square_numbers())

def exercise17():
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def all_numbers_prime(numbers):
        return all(is_prime(n) for n in numbers)

    # Example usage
    lists_of_numbers = [
        [0, 3, 4, 7, 9],
        [3, 5, 7, 13],
        [1, 5, 3]
    ]

    for numbers in lists_of_numbers:
        print(all_numbers_prime(numbers))
def exercise18():
    from itertools import permutations

    def generate_all_permutations(lst):
        return list(permutations(lst))

    # Example usage:
    my_list = [1, 2, 3]
    all_perms = generate_all_permutations(my_list)
    for perm in all_perms:
        print(perm)
def exercise19():
    def list_difference(list1, list2):
        return [item for item in list1 if item not in list2]

    # Example usage:
    first_list = [1, 2, 3, 4, 5]
    second_list = [4, 5, 6, 7, 8]
    diff = list_difference(first_list, second_list)
    print(diff)  # Expected output: [1, 2, 3]
def exercise20():
    def access_list_indices(lst):
        for index, value in enumerate(lst):
            print(f"Index {index}: {value}")

    # Example list
    my_list = ['apple', 'banana', 'cherry']

    # Access indices and values
    access_list_indices(my_list)

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