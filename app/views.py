from flask import jsonify
from app.utils import invert_diagonals, count_submatrix

@app.route('/invert-diagonals', methods=['POST'])
def api_invert_diagonals():
    matrix = request.json.get('matrix')
    inverted_matrix = invert_diagonals(matrix)
    return jsonify({'inverted_matrix': inverted_matrix})

@app.route('/count-submatrix', methods=['POST'])
def api_count_submatrix():
    matrix = request.json.get('matrix')
    submatrix = request.json.get('submatrix')
    count = count_submatrix(matrix, submatrix)
    return jsonify({'count': count})
