email = "robert@gmail.com"
password = "testpas123"

user_email = input("Email?")
user_password = input("Password?")

#         True                      True
if (email == user_email) and (password == user_password):
    print(f"Wellcome back {email}")
else:
    print("Invalid credentials!")