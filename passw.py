import string
import random

# Getting password length
length = int(input("Enter prefered password length: "))

print(''' Choose character set for password from these:
      1. Digits
      2. Letters
      3. Special Characters
      !!!Important!! After picking a number press 4 to Exit!!''')

characterslist = ""

# Getting characters set for the password
while(True):
    choice=int(input("Pick a number: "))
    # Choice 1 (Numbers)
    if choice == 1:
        characterslist += string.digits
    # Choice 2 (Letters)   
    elif choice == 2:
        characterslist += string.ascii_letters
    # Choice 3 (Digits to characters)
    elif choice == 3:
        characterslist += string.punctuation
    elif choice == 4:
        break
    else:
        print("Pick a valid option!")

password = []

for i in range(length):
    # Random number picked from available characters
    randomcharacter = random.choice(characterslist)
    # Adding random character to password
    password.append(randomcharacter)

# printing password as a string
print("Your random password is " + "".join(password))