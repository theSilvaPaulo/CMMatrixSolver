import unittest

from app.utils import conta_submatriz, inverte_diagonais

class TestFuncoes(unittest.TestCase):
    def test_inverte_diagonais(self):
        matriz = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        matriz_invertida = inverte_diagonais(matriz)
        self.assertEqual(matriz_invertida, [[3, 2, 1],
                                             [4, 5, 6],
                                             [9, 8, 7]])

    def test_conta_submatriz(self):
        matriz = [[1, 2, 3, 4],
                  [2, 3, 4, 5],
                  [3, 4, 1, 6],
                  [4, 5, 6, 7]]
        submatriz = [[3, 4],
                     [4, 5]]
        contagem = conta_submatriz(matriz, submatriz)
        self.assertEqual(contagem, 2)