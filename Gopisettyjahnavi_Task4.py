import random
import string

print("===== Password Generator =====")

while True:
    length = int(input("Enter password length: "))

    characters = ""

    if input("Include letters? (y/n): ").lower() == "y":
        characters += string.ascii_letters

    if input("Include numbers? (y/n): ").lower() == "y":
        characters += string.digits

    if input("Include symbols? (y/n): ").lower() == "y":
        characters += "!@#$%&*?"

    if characters == "":
        print("Please select at least one character type.")
    else:
        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("\nGenerated Password:", password)
        print("Password Length:", len(password))

        if length < 8:
            print("Strength: Weak")
        elif length < 12:
            print("Strength: Medium")
        else:
            print("Strength: Strong")
    choice = input("\nGenerate another password? (y/n): ").lower()
    if choice != "y":
        print("Thank you for using the Password Generator!")
        break