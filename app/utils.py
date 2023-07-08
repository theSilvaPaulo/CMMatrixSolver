from flask import Flask, jsonify, request

def invert_diagonals(matrix):
    n = len(matrix)
    for i in range(n):
        matrix[i][i], matrix[i][n-i-1] = matrix[i][n-i-1], matrix[i][i]
    return matrix

def count_submatrix(matrix, submatrix):
    # Lógica para contar quantas vezes a submatriz pode ser encontrada na matriz
    pass