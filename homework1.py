# Homework: The mood checker

mood = input("What is your mood today? ")

if mood == "happy":
    print("It is great to see you happy!")
elif mood == "nervous":
    print("Take a deep breath 3 times.")
elif mood == "sad":
    print("Cheer up.")
elif mood == "excited":
    print("Come on, relax.")
elif mood == "relaxed":
    print("Enjoy your day.")
else:
    print("I don't recognize this mood")


# Homework: Guess the secret number

secret = int(28)
guess = int(input("Enter a number: "))
if secret != guess:
    print("Sorry, your number is wrong.")
else:
    print("Congratulations, your number is right!")


# Homework: Calculator

first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
operation = input("Enter an arithmetic operation (+, -, * or /): ")

if operation == "+":
    print(first_num + second_num)
elif operation == "-":
    print(first_num - second_num)
elif operation == "*":
    print(first_num * second_num)
elif operation == "/":
    print(first_num / second_num)
else:
    print("You didn't enter a valid arithmetic operation!")