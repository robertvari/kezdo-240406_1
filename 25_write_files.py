name = input("What is your name?")
address = input("Where do you live?")
age = input("How old are you?")

file_name = "user_data.txt"

# with context
with open(file_name, "w") as my_file:
    my_file.write(f"Hello {name}. You live in {address}. You are {age} years old.")