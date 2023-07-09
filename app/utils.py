
def inverte_diagonais(matriz):
    n = len(matriz)
    for i in range(n):
        matriz[i][i], matriz[i][n-i-1] = matriz[i][n-i-1], matriz[i][i]
    return matriz

def conta_submatriz(matriz, submatriz):
    m = len(matriz)
    n = len(matriz[0])
    k = len(submatriz)
    l = len(submatriz[0])
    contagem = 0

    for i in range(m - k + 1):
        for j in range(n - l + 1):
            encontrou = True
            for linha in range(k):
                if matriz[i + linha][j:j + l] != submatriz[linha]:
                    encontrou = False
                    break
            if encontrou:
                contagem += 1
    
    return contagem
