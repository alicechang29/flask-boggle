from flask import Flask, request, render_template, jsonify
from uuid import uuid4


from boggle import BoggleGame

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-secret"

debug = DebugToolbarExtension(app)

# The boggle games created, keyed by game id
games = {}

game = BoggleGame()
games["1234"] = game


@app.get("/")
def homepage():
    """Show board."""

    return render_template("index.jinja")


@app.post("/api/new-game")
def new_game():
    """Start new game and return JSON about game.

    Returns: JSON of {
       gameId: "...uuid-of-game...",
       board: [ [ 'A', 'B', ... ], ... ]
    }
    """

    # get a unique string id for the board we're creating
    game_id = str(uuid4())
    game = BoggleGame()
    games[game_id] = game

    game_info = {
        "gameId": str(game_id),
        "board": game.board
    }

    return jsonify(game_info)

# post request
# /api/score-word
# request.json - not request.form
# accepts request {gameId: "example-game-id", word: "example"}
# check if word is legal -> needs to be in word list, can find it on board
# return json with {result: "not-word"},{result: "not-on-board"}, {result: "ok"}


@app.post('/api/score-word')
def check_valid_word():
    """TODO: write out something here"""

    # TODO: change variable names, very confusing
    current_game = request.json
    game_id = current_game['gameId']
    word = current_game['word'].upper()
    game_instance = games[game_id]

    is_valid_word = game_instance.is_word_in_word_list(word)

    is_on_board = game_instance.check_word_on_board(word)
    print('!!!!!!!!!! WORD !!!!!!!!!!!!!!', word)
    print('!!!!! VALID WORD!!!!!, ', is_valid_word)

    answer = None
    if not is_valid_word:
        answer = 'not-word'
    elif not is_on_board:
        answer = 'not-on-board'
    elif is_valid_word and is_on_board:
        answer = 'ok'

    json_answer = {
        'result': answer
    }

    return jsonify(json_answer)
