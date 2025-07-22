import random
import string

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(length):
        password += random.choice(chars)
    return password

print("Password Generator")

while True:
    length_input = input("Enter password length: ")
    try:
        length = int(length_input)
    except:
        print("Not a number. Try again.")
        continue
    if length < 4:
        print("Length should be at least 4.")
        continue
    while True:
        password = generate_password(length)
        print("Your password is:", password)
        print("****************************")
        print("What do you want to do?")
        print("1. Accept password")
        print("2. Generate new password")
        print("3. Change length")
        print("4. Exit")
        choice = input("Type 1, 2, 3 or 4: ")
        if choice == '1':
            print("Password saved. Thank you")
            exit()
        elif choice == '2':
            continue
        elif choice == '3':
            break
        elif choice == '4':
            print("Thanks for using.")
            exit()
        else:
            print("Wrong choice. Try again.")