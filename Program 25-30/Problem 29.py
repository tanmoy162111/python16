num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
print("What calculation you want to do?")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice = int(input("Enter your choice: 1-4 "))
if choice == 1:
    print("Addition of your numbers are: ",num1 + num2)
elif choice == 2:
    print("Subtraction of your numbers are: ",num1 - num2)
elif choice == 3:
    print("Multiplication of your numbers are: ",num1 * num2)
elif choice == 4:
    print("Division of your numbers are: ",num1 / num2)
else:
    print("Invalid choice")