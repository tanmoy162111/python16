num = input("Enter your number seperated by space: ")
numbersList = list(map(int, num.split()))
numbersList.sort()
print("Your Largest number is:", numbersList[-1])