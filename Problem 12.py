num = int(input("Enter your Year: "))
if num % 4 == 0 and num % 100 != 0 or num % 400 == 0:
    print("Your year is leap year.")
else:
    print("Your year is not leap year.")