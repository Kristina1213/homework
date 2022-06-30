print("Welcome to the fizzbuzz game!")

enter = int(input("Select a number between 1 and 100: "))

for number in range(1, enter+1):
    if number % 3 == 0 and number % 5 == 0:
        print("fizz")
    elif number % 3 == 0:
        print("buzz")
    elif number % 5 == 0:
        print("fizzbuzz")
    else:
        print(number)
