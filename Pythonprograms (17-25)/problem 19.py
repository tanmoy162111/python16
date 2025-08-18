num = input("Enter your number: ")
num2 = int(num)
int_num = [int(i) for i in num]
if int_num[0]**3 + int_num[1]**3 + int_num[2]**3 == num2:
    print("Your number is armstrong number")
else:
    print("Your number is not Armstrong number")