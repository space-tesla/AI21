# Q.1 Write a Python program to remove punctuations from the given string.

import string
def remove_punctuations(input_string):
    translator = str.maketrans('', '', string.punctuation)
    return input_string.translate(translator)
input_string = input("Enter a string: ")
print("String without punctuation:", remove_punctuations(input_string))


#Output:
#Enter a string: Hello, world! How's it going?
#String without punctuation: Hello world Hows it going