import random

def rock_paper_scissors(player_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print("Player choice:", player_choice)
    print("Computer choice:", computer_choice)

    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

print("Rock-Paper-Scissors Game")
player_choice = input("Enter your choice (rock/paper/scissors): ").lower()
print(rock_paper_scissors(player_choice))
