import numpy as np

R1 = int(input("Enter rows for first matrix: "))
C1 = int(input("Enter columns for first matrix: "))

print("Enter elements of first matrix row-wise:")
A = []
for i in range(R1):
    row = []
    for j in range(C1):
        row.append(int(input(f"A[{i}][{j}] = ")))
    A.append(row)

A = np.array(A)

R2 = int(input("Enter rows for second matrix: "))
C2 = int(input("Enter columns for second matrix: "))

print("Enter elements of second matrix row-wise:")
B = []
for i in range(R2):
    row = []
    for j in range(C2):
        row.append(int(input(f"B[{i}][{j}] = ")))
    B.append(row)

B = np.array(B)

if C1 != R2:
    print("Matrix multiplication not possible (columns of A != rows of B).")
else:
    result = A @ B
    print("Resultant Matrix:")
    print(result)
