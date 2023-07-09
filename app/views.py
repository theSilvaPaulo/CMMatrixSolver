from flask import jsonify, request
from app.utils import conta_submatriz, inverte_diagonais
from flask import Blueprint

app_views = Blueprint('app_views', __name__)

@app_views.route('/inverte-diagonais', methods=['POST'])
def api_inverte_diagonais():
    matriz = request.json.get('matriz')
    matriz_invertida = inverte_diagonais(matriz)
    return jsonify({'matriz_invertida': matriz_invertida})

@app_views.route('/conta-submatriz', methods=['POST'])
def api_conta_submatriz():
    matriz = request.json.get('matriz')
    submatriz = request.json.get('submatriz')
    contagem = conta_submatriz(matriz, submatriz)
    return jsonify({'contagem': contagem})