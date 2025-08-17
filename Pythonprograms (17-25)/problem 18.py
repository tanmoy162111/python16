terms = int(input("How Many terms?: "))
n1, n2 = 0, 1
count = 0
if terms <0:
    print("Sorry, can't be less than zero")
elif terms == 1:
    print("Fibonacchi sequence:", n1)
else:
    while count < terms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1