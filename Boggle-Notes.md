# Classes

## WordList (wordlist.py)

- reads list of words from file
- provides API for check if word is in the list
- `def _read_dict(self, dict_path):`
  - opens dictionary file
  - strips each word of whitespace in the file
  - changes each word to uppercase
  - closes the file
  - RETURNS a SET of words
    - `{CAT, DOG}`
- `def check_word(self, word):`
  - Checks if the word given is inside the words SET

TODO: Write WordList DocTest for `check_word`

## Boggle (boggle.py)

- manage the state of a Boggle game (keeps track of the board, the letters played, the score, and more).

- Imports english_words from the wordlist.py

BoggleGame Class

- takes in
  - word_list (dictionary)
  - board size
  - fill letters - letters filled in by frequency
  - word length score (min score is 3, max val is 7)
    - any word that is 8 or longer gets 11 points
  - max word length score is 11
- To play a word `game.play_and_score_word("CAT")`
  - calculates score

## App.py

### Homepage '/'

- renders the board


Testing
- test that it returns Json
- that that it includes:
(json.loads turns this into an object)
    - game id
    - list
- check for dictionary

### New game '/api/new-game'
make sure this returns JSON
- Starts new game, returns JSON
- assigns board random id number
- creates a game instance
- Gives that instance random game id


Testing for Valid Words Played on Board:
- Using /api/new-game route to make a new game -- calling this to make a new game and get game id
- Use the random seed on this call
- Test all the possible results for /api/score-word. (not on board, ok, not word)