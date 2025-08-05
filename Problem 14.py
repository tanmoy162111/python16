import math

num = int(input("Enter a number: "))
if num <= 1:
    print("Your number is not prime.")
elif num == 2:
    print("Your number is prime.")
elif num % 2 == 0:
    print("Your number is not prime.")
else:59
        for i in range(3, int(math.sqrt(num)) + 1, 2):
          if num % i == 0:
            print("Your number is not prime.")
            break
        else:
             print("Your number is prime.")