print("matrix size - n X n")
n = int(input("enter the size of n in the matrix: "))
matrix =[]

#values for the matrix
def get_matrix(matrix):
    for i in range(n):
        row = input("Enter the values of the row, seperated by a comma ({} values): ".format(n))
        lst = row.split(",")
        numlst =[]
        for i in lst:
            numlst.append(int(i))
        matrix.append(numlst) 
    return matrix

def guass(matrix):
    swap = 0
    for i in range(n):   #this for loop is there to swap the rows of the matrix accorindingly in such a way that there is no 0 in the diagonal values
        if matrix[i][i] == 0:
            l = matrix.pop(i)
            matrix.append(l)
            swap += 1
            i -= 1
            continue

    for i in range(n):
        if matrix[i][i] == 0: #after performing few operations on the row, we should again check is the diagonal values or 0, because due to subtraction the vlues might have become zero, if zero we send that row to the end
            l = matrix.pop(i)
            matrix.append(l)
            swap += 1
            continue
        for k in range(i+1,n):
            mul = matrix[k][i]/matrix[i][i]
            for j in range(n+1):  # n+1 because tthe last column of the matrix will be the answer for each equation
                matrix[k][j] = matrix[k][j] - mul*matrix[i][j]
    print(matrix)
    return matrix, swap

def rank(matrix): #rank of the matrix is nothing but the number of non zero rows in a matrix
    rank = 0
    for i in matrix:
        count = 0
        for j in i:
            if j != 0: #if the element is anything other than 0, then we can say that the row has some value, so we increase the rank and leave that row, to check the next row
                rank+=1
                break
    return rank

def det(matrix,swap): #determinent in a lower triangular matrix is nothing but the product of the diagonal values
    dete = 1
    for i in range(n):
        dete = dete * matrix[i][i]
    return dete * (-1)**swap

def solution(matrix): #this solution function works only for the 3*3 matrix, doesnt work for any other dimensions, gotta generalise it for it to work for all other m*m matrices
    x,y,z = 0,0,0
    z = matrix[2][3] / matrix[2][2]
    y = (matrix[1][3] - z*matrix[1][2])/matrix[1][1]
    x = (matrix[0][3] - z*matrix[0][2] - y*matrix[0][1])/matrix[0][0]
    return x,y,z

matrix, swap = guass(get_matrix(matrix))

print(solution(matrix))
