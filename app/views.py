from flask import jsonify, request
from app.utils import count_submatrix, invert_diagonals
from flask import Blueprint

app_views = Blueprint('app_views', __name__)

@app_views.route('/invert-diagonals', methods=['POST'])
def api_invert_diagonals():
    matrix = request.json.get('matrix')
    inverted_matrix = invert_diagonals(matrix)
    return jsonify({'inverted_matrix': inverted_matrix})

@app_views.route('/count-submatrix', methods=['POST'])
def api_count_submatrix():
    matrix = request.json.get('matrix')
    submatrix = request.json.get('submatrix')
    count = count_submatrix(matrix, submatrix)
    return jsonify({'count': count})