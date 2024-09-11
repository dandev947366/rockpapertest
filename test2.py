import unittest
from unittest.mock import patch
from io import StringIO
from main import determine_winner, convert_choice, main

class TestRockPaperScissors(unittest.TestCase):

    @patch('main.get_computer_choice', return_value="rock")
    def test_user_wins_rock(self, mock_get_computer_choice):
        # Arrange
        user_choice = "paper"
        computer_choice = "rock"
        
        # Act
        result = determine_winner(user_choice, computer_choice)
        
        # Assert
        self.assertEqual(result, "You win!")
        
    @patch('main.get_computer_choice', return_value="paper")
    def test_user_wins_paper(self, mock_get_computer_choice):
        # Arrange
        user_choice = "scissors"
        computer_choice = "paper"
        
        # Act
        result = determine_winner(user_choice, computer_choice)
        
        # Assert
        self.assertEqual(result, "You win!")

    @patch('main.get_computer_choice', return_value="scissors")
    def test_user_wins_scissors(self, mock_get_computer_choice):
        # Arrange
        user_choice = "rock"
        computer_choice = "scissors"
        
        # Act
        result = determine_winner(user_choice, computer_choice)
        
        # Assert
        self.assertEqual(result, "You win!")
    
    @patch('main.get_computer_choice', return_value="rock")
    def test_user_lose_rock(self, mock_get_computer_choice):
        # Arrange
        user_choice = "scissors"
        computer_choice = "rock"
        
        # Act
        result = determine_winner(user_choice, computer_choice)
        
        # Assert
        self.assertEqual(result, "You lose!")
        
    @patch('main.get_computer_choice', return_value="paper")
    def test_user_lose_paper(self, mock_get_computer_choice):
        # Arrange
        user_choice = "rock"
        computer_choice = "paper"
        
        # Act
        result = determine_winner(user_choice, computer_choice)
        
        # Assert
        self.assertEqual(result, "You lose!")

    @patch('main.get_computer_choice', return_value="scissors")
    def test_user_lose_scissors(self, mock_get_computer_choice):
        # Arrange
        user_choice = "paper"
        computer_choice = "scissors"
        
        # Act
        result = determine_winner(user_choice, computer_choice)
        
        # Assert
        self.assertEqual(result, "You lose!")
    
    @patch('main.get_computer_choice', return_value="rock")
    def test_user_tie_rock(self, mock_get_computer_choice):
        # Arrange
        user_choice = "rock"
        computer_choice = "rock"
        
        # Act
        result = determine_winner(user_choice, computer_choice)
        
        # Assert
        self.assertEqual(result, "It's a tie!")
        
    @patch('main.get_computer_choice', return_value="paper")
    def test_user_tie_paper(self, mock_get_computer_choice):
        # Arrange
        user_choice = "paper"
        computer_choice = "paper"
        
        # Act
        result = determine_winner(user_choice, computer_choice)
        
        # Assert
        self.assertEqual(result, "It's a tie!")

    @patch('main.get_computer_choice', return_value="scissors")
    def test_user_tie_scissors(self, mock_get_computer_choice):
        # Arrange
        user_choice = "scissors"
        computer_choice = "scissors"
        
        # Act
        result = determine_winner(user_choice, computer_choice)
        
        # Assert
        self.assertEqual(result, "It's a tie!")
    
    def test_valid_choices(self):
        # Arrange
        inputs = ["1", "2", "3"]
        expected_outputs = ["rock", "paper", "scissors"]
        
        # Act & Assert
        for i, input_value in enumerate(inputs):
            self.assertEqual(convert_choice(input_value), expected_outputs[i])

        
    def test_invalid_choices(self):
        # Arrange
        invalid_inputs = ["4", "rock", "", " "]
        
        # Act & Assert
        for invalid_input in invalid_inputs:
            self.assertEqual(convert_choice(invalid_input), None)

    def test_numeric_string_choices(self):
        # Arrange
        invalid_numeric_inputs = ["01", "001"]
        
        # Act & Assert
        for invalid_input in invalid_numeric_inputs:
            self.assertEqual(convert_choice(invalid_input), None)
    
    
    @patch('builtins.input', side_effect=["exit"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_exit_command(self, mock_stdout, mock_input):
        # Arrange
        expected_output = "Thanks for playing!"
        
        # Act
        main()
        output = mock_stdout.getvalue().strip()
        
        # Assert
        self.assertIn(expected_output, output)
        self.assertEqual(mock_input.call_count, 1)
    
    
if __name__ == "__main__":
    unittest.main()
