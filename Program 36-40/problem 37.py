R = int(input("Enter the number of rows: "))
C = int(input("Enter the number of columns: "))

print("Enter the first matrix row-wise:")
matrix1 = []
for i in range(R):
    row = []
    for j in range(C):
        element = int(input(f"Enter element at ({i}, {j}): "))
        row.append(element)
    matrix1.append(row)

result = [[0 for _ in range(R)] for _ in range(C)]

for i in range(R):
    for j in range(C):
        result[j][i] = matrix1[i][j]

print("The transpose is:")
for r in result:
    print(r)
