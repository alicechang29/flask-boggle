from flask import Flask, request, render_template, jsonify
from uuid import uuid4


from boggle import BoggleGame

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-secret"

debug = DebugToolbarExtension(app)

# The boggle games created, keyed by game id
games = {}


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
        # FIXME: this is already a string, can take out all of game_info
        "gameId": str(game_id),
        "board": game.board
    }

    return jsonify(game_info)  # TODO: gameId=game_id, board=game.board

# post request
# /api/score-word
# request.json - not request.form
# accepts request {gameId: "example-game-id", word: "example"}
# check if word is legal -> needs to be in word list, can find it on board
# return json with {result: "not-word"},{result: "not-on-board"}, {result: "ok"}


@app.post('/api/score-word')
def check_valid_word():
    """Checks if the word played is a valid word and is a valid word
    on the board.
    Returns a JSON result of: "not-word", "ok", or "not-on-board"
#FIXME: add in what is taken in (game data)
    Example of what is Returned: JSON of {
      result: "not-word"
    }
    """

    game_data = request.json
    game_id = game_data['gameId']
    word = game_data['word'].upper()
    current_game = games[game_id]

    result = current_game.check_valid_word_on_board(word)

    json_answer = {
        'result': result
    }

    return jsonify(json_answer)
