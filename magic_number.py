import random, os

# Globals
try_counter = 3
min_number = 1
max_number = 10


# Game intro
# clear terminal window ("clear" under linux and mac)
os.system("cls")
print("*"*50, "Magic Numbers".upper(), "*"*50)
print(f"I guess a number between {min_number} and {max_number}. I give you {try_counter} chances to guess it.")
print("Are you ready?")
print("*"*50)


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