import random

if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors game!\n")
    print("""Rules of the game: Two players secretly pick one of "rock," "paper," or "scissors". 
Both players reveal their selection to the other player at once; the winner is chosen
based on what the selections are. Rock beats scissors (by crushing them); scissors
beats paper (by cutting it); and paper beats rock (by covering it). If both players select
the same one, it is a tie""")
    selection = ["rock", "paper", "scissors"]
    computer_choice = random.choice(selection)
    user_choice = input("Enter your choice (rock, paper, scissors): ")
    while True:
        if user_choice not in selection:
            user_choice = input("Invalid choice. Please enter rock, paper, or scissors (lowercase): ")
            continue
            print(f"Computer chose: {computer_choice}")
        if user_choice == computer_choice:
            print("It's a tie!")
            user_choice = input("Enter your choice (rock, paper, scissors): ")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("Computer wins!")
        break