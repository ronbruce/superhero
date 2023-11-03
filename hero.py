import random

class Hero:
    def __init__(self, name, starting_health=10):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

        # self.name = name
        # self.starting_health = starting_health
        # self.current_health = starting_health

    def fight(self, opponent):
        print(f"{self.name} vs. {opponent.name} - Fight!")

        round_number = 1
        while self.current_health > 0 and opponent.current_health > 0:
            # Continue the fight while both heroes have health remaining.
            print(f"Round {round_number}")
            attack = random.randint(0, 1)
            if attack == 0:
                opponent.current_health -= random.randint(1, 10)
            else:
                self.current_health -= random.randint(1, 10)
            round_number += 1
        # Determine the winner or declare a draw.
        if self.current_health > 0:
            print(f"{self.name} wins! Defeated {opponent.name}")
        elif opponent.current_health > 0:
            print(f"{opponent.name} wins! Defeated {self.name}")
        else:
            print("It's a draw!")

if __name__ == "__main__":
    my_hero = Hero("Spiderman", 10)
    opponent_hero = Hero("Superman", 10)
   
    my_hero.fight(opponent_hero)


    # choose random hero
    # if random hero == this random hero
    # print "this hero vs this hero begin fight!"
    # call fight.random
    # substract int between 0-1 on random hero
    # if this.hero got 0 - 1
    # then that hero lose
    # print (hero who won!)

    # print round 2 fight
    # repeat loop

    # if draw repeat loop
    # else after round 2 
    # print winner and end game

    