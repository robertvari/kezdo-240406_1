import random, os

# Globals
min_number = 1
max_number = 10

while True:
    try_counter = 3

    # Game intro
    # clear terminal window ("clear" under linux and mac)
    os.system("cls")
    print("*"*50, "Magic Numbers".upper(), "*"*50)
    print(f"I guess a number between {min_number} and {max_number}. I give you {try_counter} chances to guess it.")
    
    # Generate a random number
    magic_number = random.randint(min_number, max_number)

    # Get player number
    player_number = input("Guess my number:")

    # todo while loop for checking valid number
    while str(magic_number) != player_number:
        try_counter -= 1

        if try_counter == 0:
            break

        print(f"Wrong guess! You have {try_counter} tries left. Try again.")
        player_number = input("Guess my number:")


    # End game conditions
    if str(magic_number) == player_number:
        print(f"You win! {magic_number} was my number :)")
    else:
        print(f"You lost the game :( My number was {magic_number}")

    new_game = input("Do you want to play again? (y/n)")

    if new_game != "y":
        print("Thank you for the game. See you next time.")
        break