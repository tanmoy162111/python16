import string
punctuations = string.punctuation
my_str = input("Enter a string: ")

no_punctuation = ""
for char in my_str:
    if char not in punctuations:
        no_punctuation = no_punctuation + char

print("String without punctuation:", no_punctuation)
