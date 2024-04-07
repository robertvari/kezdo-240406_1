import random

magic_number = random.randint(1, 10)

# cast a string to an int
player_number = input("Guess my number:")



while str(magic_number) != player_number:
    print("Wrong guess! Try again.")
    player_number = input("Guess my number:")





if str(magic_number) == player_number:
    print(f"You win! {magic_number} was my number :)")
else:
    print(f"You lost the game :( My number was {magic_number}")