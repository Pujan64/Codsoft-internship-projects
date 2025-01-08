import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("Computer wins!")

def main():
    print("Welcome to Rock-Paper-Scissors!")
    print("Rules: Rock beats Scissors, Scissors beat Paper, Paper beats Rock.")
    
    user_score = 0
    computer_score = 0

    while True:
        print("\nOptions: rock, paper, scissors")
        user_choice = input("Enter your choice: ").lower()
        
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        
        display_result(user_choice, computer_choice, winner)
        print(f"Scores - You: {user_score}, Computer: {computer_score}")
        
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing!")
            print(f"Final Scores - You: {user_score}, Computer: {computer_score}")
            break


main()
