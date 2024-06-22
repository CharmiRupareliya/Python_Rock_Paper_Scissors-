import random
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)

user_wins = 0        #variable that tracks user's score.
computer_wins = 0    #variable that tracks computer's score.
ties = 0

options = ["rock", "paper", "scissors"]

while True:

    user_input = input(Fore.BLACK + Style.BRIGHT + "Type Rock/Paper/Scissors or Q to quit game: ").lower()

    if user_input == "q":  #it check conditoion to quit game
        break

    if user_input not in ["rock", "paper", "scissors"]:   #to check invalid data.
        print(Fore.RED + Style.BRIGHT + "Please enter valid data....")
        print()
        continue

    random_num = random.randint(0,2)
    # rock = 0 , paper = 1, scissors = 2

    computer_pick = options[random_num]
    print(Fore.BLUE + "Computer Picked", Fore.BLUE + Style.BRIGHT + computer_pick + ".")

   #checking user's winnig conditions

    if user_input == "rock" and computer_pick == "scissors":
        print(Fore.MAGENTA + Style.BRIGHT +  "You Won!")
        user_wins += 1
        print()
        continue

    elif user_input == "paper" and computer_pick == "rock":
        print(Fore.MAGENTA + Style.BRIGHT +  "You Won!")
        user_wins += 1
        print()
        continue

    elif user_input == "scissors" and computer_pick == "paper":
        print(Fore.MAGENTA + Style.BRIGHT +  "You Won!")
        user_wins += 1
        print()
        continue

    elif user_input == computer_pick:
        print(Fore.YELLOW + Style.BRIGHT + "It's a tie.")
        ties += 1
        print()

    else:
        print(Fore.RED + Style.BRIGHT +  "You Lost!")
        computer_wins += 1
        print()

print()
print(Fore.MAGENTA + "You won",Fore.MAGENTA + str(user_wins) + " times.")
print(Fore.BLUE + "The computer won", Fore.BLUE + str(computer_wins) + " times.")
print(Fore.YELLOW + f"Total number of ties: {ties}")

print()
print("Thank you for Playing, Good Bye :)")




