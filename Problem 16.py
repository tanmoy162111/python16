num = int(input("Enter a number for factorial: "))
if num < 1:
    print("Your number should be a positive number.")
elif num == 0:
    print("Your number is 0, not suitable for factorial.")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print("Your factorial is",factorial)