# Assignment 3
# Class: Software Testing
# Professor: Esa Huiskonen
# Student: Dan Le
# Team : 4

import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    outcomes = {
        ("rock", "scissors"): "You win!",
        ("paper", "rock"): "You win!",
        ("scissors", "paper"): "You win!",
        ("rock", "paper"): "You lose!",
        ("paper", "scissors"): "You lose!",
        ("scissors", "rock"): "You lose!"
    }
    if user_choice == computer_choice:
        return "It's a tie!"
    return outcomes.get((user_choice, computer_choice), "Invalid game result")

def convert_choice(choice):
    mapping = {
        "1": "rock",
        "2": "paper",
        "3": "scissors"
    }
    return mapping.get(choice, None)

def main():
    while True:
        user_input = input("\n\nEnter\n(1) for rock\n(2) for paper\n(3) for scissors\nType 'exit' to quit\n\n")
        if user_input == "exit":
            print("Thanks for playing!")
            break
        
        user_choice = convert_choice(user_input)
        if user_choice is None:
            print("Invalid choice, please try again.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))

if __name__ == "__main__":
    main()
