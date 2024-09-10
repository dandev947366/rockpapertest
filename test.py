import unittest
from unittest.mock import patch
from io import StringIO
from main import determine_winner, convert_choice, main

class TestRockPaperScissors(unittest.TestCase):

    @patch('main.get_computer_choice', return_value="rock")
    def test_user_wins_rock(self, mock_get_computer_choice):
        self.assertEqual(determine_winner("paper", "rock"), "You win!")
        
    @patch('main.get_computer_choice', return_value="paper")
    def test_user_wins_paper(self, mock_get_computer_choice):
        self.assertEqual(determine_winner("scissors", "paper"), "You win!")

    @patch('main.get_computer_choice', return_value="scissors")
    def test_user_wins_scissors(self, mock_get_computer_choice):
        self.assertEqual(determine_winner("rock", "scissors"), "You win!")
    
    @patch('main.get_computer_choice', return_value="rock")
    def test_user_lose_rock(self, mock_get_computer_choice):
        self.assertEqual(determine_winner("scissors", "rock"), "You lose!")
        
    @patch('main.get_computer_choice', return_value="paper")
    def test_user_lose_paper(self, mock_get_computer_choice):
        self.assertEqual(determine_winner("rock", "paper"), "You lose!")

    @patch('main.get_computer_choice', return_value="scissors")
    def test_user_lose_scissors(self, mock_get_computer_choice):
        self.assertEqual(determine_winner("paper", "scissors"), "You lose!")
    
    @patch('main.get_computer_choice', return_value="rock")
    def test_user_tie_rock(self, mock_get_computer_choice):
        self.assertEqual(determine_winner("rock", "rock"), "It\'s a tie!")
        
    @patch('main.get_computer_choice', return_value="paper")
    def test_user_tie_paper(self, mock_get_computer_choice):
        self.assertEqual(determine_winner("paper", "paper"), "It\'s a tie!")

    @patch('main.get_computer_choice', return_value="scissors")
    def test_user_tie_scissors(self, mock_get_computer_choice):
        self.assertEqual(determine_winner("scissors", "scissors"), "It's a tie!")
    
    def test_valid_choices(self):
        self.assertEqual(convert_choice("1"), "rock")
        self.assertEqual(convert_choice("2"), "paper")
        self.assertEqual(convert_choice("3"), "scissors")

        
    def test_invalid_choices(self):
        self.assertEqual(convert_choice("4"), None)  
        self.assertEqual(convert_choice("rock"), None)  
        self.assertEqual(convert_choice(""), None)  
        self.assertEqual(convert_choice(" "), None)  

    def test_numeric_string_choices(self):
        self.assertEqual(convert_choice("01"), None)  
        self.assertEqual(convert_choice("001"), None)  
    
    
    @patch('builtins.input', side_effect=["exit"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_exit_command(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue().strip()
        self.assertIn("Thanks for playing!", output)
        self.assertEqual(mock_input.call_count, 1)  
    
    
if __name__ == "__main__":
    unittest.main()
