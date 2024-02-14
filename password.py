import random
import string

#Getting Length of password wanted. 
length = int(input("Enter password length: "))

print('''Choose character set for password from these: 
         1. Letters
         2. Digits
         3. Special Characters
         4. Exit''' )
characterList = ""

# Getting Characters for password
while(True):
    choice = int(input("Pick a number: "))
    if(choice == 1):
        
        # Adding all possible letters
        characterList += string.ascii_letters
    elif(choice == 2):

        #Adding all possible numbers
        characterList += string.digits
    elif(choice == 3):

        #Adding all special characters
        characterList += string.punctuation
    elif(choice == 4):
        break
    else:
        print("Enter a valid option!")

password = []

for i in range(length):

    #picking a random character from list 
    randomchar = random.choice(characterList)

    #adding characters to password 
    password.append(randomchar)

#printing password as a string
print("The random password is " + "".join(password))


