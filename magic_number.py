import random, os

# Game intro
# clear terminal window ("clear" under linux and mac)
os.system("cls")
print("*"*50, "Magic Numbers".upper(), "*"*50)
print("I guess a number between 1 and 10. I give you 3 chances to guess it.")
print("Are you ready?")
print("*"*50)



# Generate a random number
magic_number = random.randint(1, 10)


# Get player number
player_number = input("Guess my number:")



# todo while loop for checking valid number
try_counter = 3
while str(magic_number) != player_number:
    try_counter -= 1

    print(f"Wrong guess! You have {try_counter} tries left. Try again.")
    player_number = input("Guess my number:")



# End game conditions
if str(magic_number) == player_number:
    print(f"You win! {magic_number} was my number :)")
else:
    print(f"You lost the game :( My number was {magic_number}")