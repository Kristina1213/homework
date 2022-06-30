import random

countries_cities = {"Austria": "Vienna", "Croatia": "Zagreb", "Spain": "Madrid", "Slovenia": "Ljubljana"}

country = random.choice(list(countries_cities.keys()))
users_input = input("What is the capital city of " + country + "? ")

if users_input.capitalize() == countries_cities[country]:
    print("This is correct!")
else:
    print("This is wrong.")