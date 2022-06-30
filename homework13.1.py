import json

class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds


class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


class SoccerPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards


if __name__=="__main__":

    print("Enter some soccer player's data!")
    f_name = input("Enter player's first name: ")
    l_name = input("Enter player's last name: ")
    height = input("Enter player's height in cm: ")
    weight = input("Enter player's weight in kg: ")
    goals = input("Enter the number of player's goals: ")
    y_cards = input("Enter the number of player's yellow cards: ")
    r_cards = input("Enter the number of player's red cards: ")

    new_player = SoccerPlayer(first_name=f_name, last_name=l_name, height_cm=float(height), weight_kg=float(weight), goals=int(goals), yellow_cards=int(y_cards), red_cards=int(r_cards))

with open("soccer_player.json", "w") as soccer_file:
    soccer_file.write(str(new_player.__dict__))

print("You entered a new player!")
print(new_player.__dict__)
