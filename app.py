from flask import Flask, request, jsonify
from chess import Board
from flask_cors import CORS

import random

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def make_move():
    board = Board(request.get_json()["board"])
    print(board)
    legal_moves = list(board.legal_moves)
    if not legal_moves:
        return jsonify({"move": None})
    random_move = random.choice(legal_moves)
    board.push(random_move)
    response=jsonify({"move": str(random_move), "board": board.fen()})
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


if __name__ == "__main__":
    app.run(debug=False,host="0.0.0.0")
