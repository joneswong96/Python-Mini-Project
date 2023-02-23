# Ask user if they want to generate a password or not 
# If yes, ask for password length 
# Generate password 
# Print Password 
# If initial response is no, exit program 

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_Password():
    password_length = int(input("How long would you like your password to be?" ))

    random.shuffle(characters)

    password = []

    for x in range(password_length): 
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)

option = input("Do you want to generate a password? (y/n): ")

if option == "y":
    generate_Password()
elif option == "n":
    print("Progrm end")
    quit()
else:
    print("Invalid input, Please enter y or n")
    quit()
