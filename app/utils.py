
def invert_diagonals(matrix):
    n = len(matrix)
    for i in range(n):
        matrix[i][i], matrix[i][n-i-1] = matrix[i][n-i-1], matrix[i][i]
    return matrix

def count_submatrix(matrix, submatrix):
    m = len(matrix)
    n = len(matrix[0])
    k = len(submatrix)
    l = len(submatrix[0])
    count = 0

    for i in range(m - k + 1):
        for j in range(n - l + 1):
            if matrix[i:i+k] == submatrix and all(matrix[row][j:j+l] == submatrix[row-i] for row in range(i, i+k)):
                count += 1
    
    return count