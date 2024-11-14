# Q.1 Write a Python program to remove punctuations from the given string.

import string

# Function to remove punctuations from the given string
def remove_punctuations(input_string):
    # Create a translation table that maps punctuation characters to None
    translator = str.maketrans('', '', string.punctuation)
    # Use translate to remove punctuation
    return input_string.translate(translator)

# Input string from the user
input_string = input("Enter a string: ")

# Remove punctuations and print the result
print("String without punctuation:", remove_punctuations(input_string))


Output:
Enter a string: Hello, world! How's it going?
String without punctuation: Hello world Hows it going