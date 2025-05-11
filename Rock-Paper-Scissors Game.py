import random

def get_user_choice():
    while True:
        choice = input("Choose rock, paper, or scissors: ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        print("Invalid input. Please choose rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    if (user == "rock" and computer == "scissors") or \
       (user == "scissors" and computer == "paper") or \
       (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user, computer, winner):
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")
    if winner == "tie":
        print("Result: It's a tie!")
    elif winner == "user":
        print("Result: You win!")
    else:
        print("Result: Computer wins!")

def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1

    print("Welcome to Rock-Paper-Scissors!")
    print("Rules: Rock beats Scissors, Scissors beat Paper, Paper beats Rock.\n")

    while True:
        print(f"--- Round {round_number} ---")
        user = get_user_choice()
        computer = get_computer_choice()
        winner = determine_winner(user, computer)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        display_result(user, computer, winner)
        print(f"Score => You: {user_score} | Computer: {computer_score}")

        again = input("\nDo you want to play another round? (yes/no): ").lower()
        if again != "yes":
            print("\nThanks for playing! Final Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            break

        round_number += 1

# Start the game
play_game()
