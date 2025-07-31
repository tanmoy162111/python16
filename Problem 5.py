import math

a = float(input("Enter a value: "))
b = float(input("Enter another value: "))
c = float(input("Enter another value: "))
def solve_quadratic(a, b, c):
    if a == 0:
        return "Not a quadratic equation (a cannot be zero)."

    discriminant = (b**2) - 4*(a*c)

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return "Roots are real and distinct: x1 = {root1}, x2 = {root2}"
    elif discriminant == 0:
        root = -b / (2*a)
        return "Roots are real and equal: x1 = x2 = {root1}"
    else:
        real_part = -b / (2*a)
        imag_part = math.sqrt(abs(discriminant)) / (2*a)
        return"Roots are complex: x1 = {real_part} + {imag_part}i, x2 = {real_part} - {imag_part}i"

    print(solve_quadratic(a, b, c))
