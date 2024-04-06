magic_number = 6

player_number = input("Guess my number:")

if magic_number == player_number:
    print(f"You win! {magic_number} was my number :)")
else:
    print("You lost the game :(")