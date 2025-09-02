my_string = input("Enter the string: ")
my_string = my_string.casefold()
rev_string = reversed(my_string)
if list(my_string) == list(rev_string):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")
