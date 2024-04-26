from unittest import TestCase
import random

from app import app, games

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True


class BoggleAppTestCase(TestCase):
    """Test flask app of Boggle."""

    def setUp(self):
        """Stuff to do before every test."""

        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure information is in the session and HTML is displayed"""

        with app.test_client() as client:
            response = client.get('/')
            html = response.get_data(as_text=True)
            ...
            # test that you're getting a template
            self.assertEqual(response.status_code, 200)
            self.assertIn('<!-- Home page template for test-->', html)

    def test_api_new_game(self):
        """Test starting a new game."""

        with app.test_client() as client:
            response = client.post("/api/new-game")
            data = response.get_json()
            ...
            # write a test for this route
            self.assertEqual(response.status_code, 200)
            self.assertIsInstance(data, dict)
            self.assertIsInstance(data["board"], list)
            self.assertIsNotNone(data["gameId"])
            self.assertIsNotNone(data["board"])

    def test_api_invalid_word(self):
        """Testing for invalid word"""

        with app.test_client() as client:
            random.seed(1)
            game_data_resp = client.post("/api/new-game")
            game_data = game_data_resp.get_json()
            data = client.post('/api/score-word', json={
                "gameId": game_data["gameId"],
                "word": "OOTY"
            })
            resp = data.get_json()

        self.assertEqual({'result': 'not-word'}, resp)

    def test_api_valid_word(self):
        """Testing for a valid word"""

        with app.test_client() as client:
            random.seed(1)
            game_data_resp = client.post("/api/new-game")
            game_data = game_data_resp.get_json()
            data = client.post('/api/score-word', json={
                "gameId": game_data["gameId"],
                "word": "DATES"
            })
            resp = data.get_json()

        self.assertEqual({'result': 'ok'}, resp)

    def test_api_not_on_board(self):
        """Testing for a valid word that but is not on the board"""

        with app.test_client() as client:
            random.seed(1)
            game_data_resp = client.post("/api/new-game")
            game_data = game_data_resp.get_json()
            data = client.post('/api/score-word', json={
                "gameId": game_data["gameId"],
                "word": "SOCCER"
            })
            resp = data.get_json()

        self.assertEqual({'result': 'not-on-board'}, resp)
