def exercise1():
    # Python program to calculate the length of a string

    def string_length():
        # Ask the user to enter a string
        user_input = input("Enter a string: ")

        # Calculate the length of the string
        length = len(user_input)

        # Display the length of the string
        print(f"The length of the entered string is: {length}")

    # Call the function
    string_length()
def exercise2():
    # Code for exercise 2
    def count_characters(string):
        # Initialize a dictionary to store the frequency of characters
        frequency = {}

        # Iterate over each character in the string
        for char in string:
            # If the character is already in the dictionary, increment its count
            if char in frequency:
                frequency[char] += 1
            # If the character is not in the dictionary, add it with count 1
            else:
                frequency[char] = 1

        return frequency

    # Sample string
    sample_string = 'google.com'
    # Call the function and store the result
    char_frequency = count_characters(sample_string)

    return(char_frequency)

def exercise3():
    # Define a function named string_both_ends that takes one argument, 'str'.
    def string_both_ends(str):
        # Check if the length of the input string 'str' is less than 2 characters.
        if len(str) < 2:
            # If the string is shorter than 2 characters, return an empty string.
            return ''

        # If the string has at least 2 characters, concatenate the first two characters
        # and the last two characters of the input string and return the result.
        return str[0:2] + str[-2:]

    # Call the string_both_ends function with different input strings and print the results.
    return (string_both_ends('w3resource')), (string_both_ends('w3')), (string_both_ends('w'))
def exercise4():
    def change_chars(s):
        if s:
            first_char = s[0]
            s = s.replace(first_char, '$')
            s = first_char + s[1:]
        return s

    # Sample String
    sample_string = 'restart'
    # Expected Result
    result = change_chars(sample_string)
    return(result)  # This should print 'resta$t'
def exercise5():
    def swap_string(s1, s2):
        # Get the first two characters of each string
        first_two_s1 = s1[:2]
        first_two_s2 = s2[:2]

        # Swap the first two characters and concatenate with the remaining part of the strings
        new_s1 = first_two_s2 + s1[2:]
        new_s2 = first_two_s1 + s2[2:]

        # Combine the new strings with a space in between
        return new_s1 + ' ' + new_s2

    # Sample strings
    sample_string1 = 'abc'
    sample_string2 = 'xyz'

    # Expected Result
    result = swap_string(sample_string1, sample_string2)
    return(result)  # Should print 'xyc abz'
def exercise6():
    def add_ing_or_ly(str):
        if len(str) < 3:
            return str
        if str.endswith('ing'):
            return str + 'ly'
        else:
            return str + 'ing'

    # Sample strings and their expected results
    return(add_ing_or_ly('abc')), (add_ing_or_ly('string'))
def exercise7():
    def not_poor(s):
        s_not = s.find('not')
        s_poor = s.find('poor')

        if s_poor > s_not and s_not > 0 and s_poor > 0:
            s = s.replace(s[s_not:(s_poor + 4)], 'good')

        return s

    sample_string1 = 'The lyrics is not that poor!'
    sample_string2 = 'The lyrics is poor!'

    return(not_poor(sample_string1)), (not_poor(sample_string2))
def exercise8():
    def find_longest_word(word_list):
        longest_word = max(word_list, key=len)
        return longest_word, len(longest_word)

    # Example usage:
    words = ['Python', 'function', 'Exercises', 'longest', 'list']
    longest_word, length_of_longest = find_longest_word(words)

    return("Longest word:", longest_word), ("Length of the longest word:", length_of_longest)
def exercise9():
    def remove_char_at_n(string, n):
        # Check if n is a valid index
        if n < len(string):
            return string[:n] + string[n + 1:]
        else:
            return "Index out of range."

    # Example usage:
    sample_string = "Python"
    n = 3
    result = remove_char_at_n(sample_string, n)
    return(result)  # Expected output: "Pyton", since it removes the character at index 3 ('h')
def exercise10():
    def swap_first_last(string):
        if len(string) > 1:
            return string[-1] + string[1:-1] + string[0]
        else:
            return string

    # Example usage:
    sample_string = "python"
    result = swap_first_last(sample_string)
    return(result)  # Expected output: "nythop"
def exercise11():
    def remove_odd_index_chars(string):
        return ''.join(char for index, char in enumerate(string) if index % 2 == 0)

    # Example usage:
    sample_string = "python"
    result = remove_odd_index_chars(sample_string)
    return(result)  # Should print "pto" since 'y', 'h', and 'n' are at odd indices
def exercise12():
    from collections import Counter

    def count_word_occurrences(sentence):
        # Split the sentence into words
        words = sentence.split()
        # Count the occurrences of each word
        word_counts = Counter(words)
        return word_counts

    # Example usage:
    sample_sentence = "This is a test sentence with some words, some words repeated."
    # Note: If you want to count words without punctuation, you could preprocess the sentence to remove it.
    result = count_word_occurrences(sample_sentence)
    return(result)
def exercise13():
    # Take input from the user
    user_input = input("Please enter some text: ")

    # Display the input in upper case
    print("Upper case: ", user_input.upper())

    # Display the input in lower case
    print("Lower case: ", user_input.lower())

def exercise14():
    # Python program to sort unique words alphanumerically

    def sort_unique_words(words):
        # Split the words, remove duplicates by creating a set, and then sort them
        unique_words = sorted(set(words.split(', ')))
        # Return the sorted words as a comma-separated string
        return ', '.join(unique_words)

    # Sample usage:
    input_words = 'red, white, black, red, green, black'
    return(sort_unique_words(input_words))
def exercise15():
    def add_tags(tag, words):
        return f"<{tag}>{words}</{tag}>"

    # Sample usage
    print(add_tags('i', 'Python'))  # Output: <i>Python</i>
    print(add_tags('b', 'Python Tutorial'))  # Output: <b>Python Tutorial</b>

def exercise16():
    def insert_string_middle(brackets, word):
        middle_index = len(brackets) // 2
        return brackets[:middle_index] + word + brackets[middle_index:]

    # Sample function calls
    print(insert_string_middle('<<>>', 'Python'))  # Expected Output: [[Python]]
    print(insert_string_middle('{{}}', 'PHP'))  # Expected Output: {{PHP}}
def exercise17():
    def insert_end(text):
        if len(text) < 2:
            return "The string is too short."
        return text[-2:] * 4

    # Example usage
    print(insert_end('Python'))  # Should return 'onononon'
    print(insert_end('Exercises'))  # Should return 'eseseses'
def exercise18():
    def first_three(text):
        return text[:3] if len(text) > 2 else text

    # Example usage
    print(first_three('ipy'))  # Output: 'ipy'
    print(first_three('python'))  # Output: 'pyt'
def exercise19():
    def get_last_part(string, character):
        # Split the string by the specified character and return the part before the last occurrence
        parts = string.rsplit(character, 1)
        return parts[0] if len(parts) > 1 else string

    # Example usage
    print(get_last_part('example.txt', '.'))  # Output: 'example'
    print(get_last_part('another_example.txt', '_'))  # Output: 'another'
def exercise20():
    def reverse_if_multiple_of_four(s):
        # Check if the length of the string is a multiple of 4
        if len(s) % 4 == 0:
            # Return the reversed string
            return s[::-1]
        else:
            # Return the original string if the condition is not met
            return s

    # Example usage
    print(reverse_if_multiple_of_four('Python'))  # Output: 'Python' (since its length is not a multiple of 4)
    print(reverse_if_multiple_of_four('abcd'))  # Output: 'dcba' (since its length is a multiple of 4)

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