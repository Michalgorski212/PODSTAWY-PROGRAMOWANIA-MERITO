def exercise1():
    # Code for exercise 1
    def sort_dict_by_value(d, ascending=True):
        return dict(sorted(d.items(), key=lambda item: item[1], reverse=not ascending))

    # Example dictionary
    sample_dict = {'a': 3, 'b': 1, 'c': 2, 'd': 4}

    # Sort the dictionary in ascending order by value
    sorted_dict_asc = sort_dict_by_value(sample_dict, True)
    print('Ascending:', sorted_dict_asc)

    # Sort the dictionary in descending order by value
    sorted_dict_desc = sort_dict_by_value(sample_dict, False)
    print('Descending:', sorted_dict_desc)

def exercise2():
    # Code for exercise 2
    # Python script to add a key to a dictionary

    def add_key_to_dict(d, key, value):
        d[key] = value
        return d

    # Sample dictionary
    sample_dict = {0: 10, 1: 20}

    # Add a new key-value pair
    sample_dict[2] = 30

    # Now sample_dict is {0: 10, 1: 20, 2: 30}
    print(sample_dict)

def exercise3():
    def concatenate_dicts(*args):
        result = {}
        for dictionary in args:
            result.update(dictionary)
        return result

    # Sample dictionaries
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}

    # Concatenate dictionaries
    concatenated_dict = concatenate_dicts(dic1, dic2, dic3)
    print(concatenated_dict)
def exercise4():
    def key_exists(dict, key):
        return key in dict

    # Sample dictionary
    sample_dict = {1: 10, 2: 20, 3: 30}

    # Check if a key exists
    key_to_check = 2
    does_key_exist = key_exists(sample_dict, key_to_check)

    print(f"Does key {key_to_check} exist in the dictionary? {does_key_exist}")
def exercise5():
    def iterate_dictionary(d):
        for key, value in d.items():
            print(f"Key: {key}, Value: {value}")

    # Sample dictionary
    sample_dict = {1: 'apple', 2: 'banana', 3: 'cherry'}

    # Iterate over the dictionary
    iterate_dictionary(sample_dict)
def exercise6():
    # Python script to generate and print a dictionary where the keys are numbers between 1 and n and the values are squares of keys

    def generate_squares(n):
        return {i: i ** 2 for i in range(1, n + 1)}

    # Example usage for n = 5
    squares = generate_squares(5)
    print(squares)
def exercise7():
    # Python script to print a dictionary where the keys are numbers between 1 and 15 and the values are squares of the keys

    def generate_squares():
        squares_dict = {i: i ** 2 for i in range(1, 16)}
        return squares_dict

    # Call the function and print the dictionary
    squares = generate_squares()
    print(squares)
def exercise8():
    def merge_dictionaries(dict1, dict2):
        # In Python 3.5+ you can use the {**dict1, **dict2} syntax
        merged_dict = {**dict1, **dict2}
        return merged_dict

    # Example dictionaries to merge
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}

    # Merging the dictionaries
    merged_dict = merge_dictionaries(dict1, dict2)
    print("Merged Dictionary:", merged_dict)
def exercise9():
    def iterate_dictionary(d):
        for key, value in d.items():
            print(f"Key: {key}, Value: {value}")

    # Sample dictionary
    sample_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    # Iterate over the dictionary
    print("Iterating over dictionary:")
    iterate_dictionary(sample_dict)
def exercise10():
    def sum_all_items(d):
        return sum(d.values())

    # Sample dictionary
    sample_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    # Calculate the sum
    total_sum = sum_all_items(sample_dict)
    print("Sum of all items:", total_sum)
def exercise11():
    def multiply_all_items(d):
        result = 1
        for value in d.values():
            result *= value
        return result

    # Sample dictionary
    sample_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    # Calculate the product
    total_product = multiply_all_items(sample_dict)
    print("Product of all items:", total_product)

def exercise12():
    def remove_key(d, key):
        if key in d:
            del d[key]
        return d

    # Sample dictionary
    sample_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    # Key to remove
    key_to_remove = 'b'

    # Remove the key
    updated_dict = remove_key(sample_dict, key_to_remove)
    print("Dictionary after removing key:", updated_dict)
def exercise13():
    def map_lists_to_dict(keys, values):
        return dict(zip(keys, values))

    # Sample lists
    keys = ['one', 'two', 'three']
    values = [1, 2, 3]

    # Create the dictionary
    mapped_dict = map_lists_to_dict(keys, values)
    print("Mapped dictionary:", mapped_dict)
def exercise14():
    def sort_dict_by_key(d):
        return dict(sorted(d.items()))

    # Sample dictionary
    sample_dict = {'b': 2, 'c': 3, 'a': 1, 'd': 4}

    # Sort the dictionary by key
    sorted_dict = sort_dict_by_key(sample_dict)
    print("Sorted dictionary by key:", sorted_dict)

def exercise15():
    def get_max_min_values(d):
        max_value = max(d.values())
        min_value = min(d.values())
        return max_value, min_value

    # Sample dictionary
    sample_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    # Get the maximum and minimum values
    max_value, min_value = get_max_min_values(sample_dict)
    print("Maximum value:", max_value)
    print("Minimum value:", min_value)
def exercise16():
    class SampleObject:
        def __init__(self):
            self.x = 'apple'
            self.y = 'banana'
            self.z = 'cherry'

    def object_to_dict(obj):
        return vars(obj)

    # Creating an instance of SampleObject
    sample_obj = SampleObject()

    # Converting object fields to a dictionary
    obj_dict = object_to_dict(sample_obj)
    print("Object fields as dictionary:", obj_dict)
def exercise17():
    def remove_duplicates(d):
        reverse_d = {}
        for key, value in d.items():
            if value not in reverse_d:
                reverse_d[value] = key
        # Inverting the dictionary again
        return {value: key for key, value in reverse_d.items()}

    # Sample dictionary with duplicate values
    sample_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 2, 'e': 3}

    # Removing duplicates
    unique_dict = remove_duplicates(sample_dict)
    print("Dictionary after removing duplicates:", unique_dict)
def exercise18():
    def is_dict_empty(d):
        return not bool(d)

    # Sample dictionaries
    empty_dict = {}
    non_empty_dict = {'a': 1}

    # Check if dictionaries are empty
    print("Is empty dict empty?", is_dict_empty(empty_dict))
    print("Is non-empty dict empty?", is_dict_empty(non_empty_dict))
def exercise19():
    from collections import Counter

    def combine_dictionaries(d1, d2):
        # Creating Counter objects for both dictionaries
        counter_d1 = Counter(d1)
        counter_d2 = Counter(d2)
        # Combining the dictionaries by adding values of common keys
        combined_counter = counter_d1 + counter_d2
        return combined_counter

    # Sample dictionaries
    d1 = {'a': 100, 'b': 200, 'c': 300}
    d2 = {'a': 300, 'b': 200, 'd': 400}

    # Combine dictionaries
    combined_dict = combine_dictionaries(d1, d2)
    print("Combined Dictionary:", combined_dict)
def exercise20():
    def get_unique_values(data):
        # Using a set to store unique values
        unique_values = set()
        for dictionary in data:
            unique_values.update(dictionary.values())
        return unique_values

    # Sample data: list of dictionaries
    sample_data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
                   {"VIII": "S007"}]

    # Get unique values
    unique_values = get_unique_values(sample_data)
    print("Unique Values:", unique_values)

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