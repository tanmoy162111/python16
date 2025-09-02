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

print("Enter the second matrix row-wise:")
matrix2 = []
for i in range(R):
    row = []
    for j in range(C):
        element = int(input(f"Enter element at ({i}, {j}): "))
        row.append(element)
    matrix2.append(row)


result = []
for i in range(R):
    row = []
    for j in range(C):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

print("The resulting matrix is:")
for row in result:
    print(row)
