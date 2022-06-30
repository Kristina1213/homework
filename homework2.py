# 9.1 Unit converter

print("Hello, here you can convert kilometers into miles.")

miles = 0.621371
x = "no"

while True:
    kilometers = int(input("Please enter the number of kilometers: "))
    print(kilometers, "kilometers are", kilometers * miles, "miles.")

    choice = input("Do you want to do another conversion? (yes or no): ")
    if choice == x:
        print("Thank you and goodbye.")
        break





