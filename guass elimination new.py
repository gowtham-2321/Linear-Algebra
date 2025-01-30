print("matrix size - n X n")
n = int(input("enter the size of n in the matrix: "))
matrix =[]

#values for the matrix
for i in range(n):
    row = input("Enter the values of the row, seperated by a comma ({} values): ".format(n))
    lst = row.split(",")
    numlst =[]
    for i in lst:
        numlst.append(int(i))
    matrix.append(numlst) 

temp = []



for i in range(n):
    temp = matrix[i]
    num = temp[i]
    if(i+1)== n:
        break

    for k in range(i+1,n):
        mul = matrix[k][i]/num
        for j in range(n):
            matrix[k][j] = matrix[k][j] - mul*temp[j]

print(matrix)
    