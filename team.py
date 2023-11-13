import random

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []


    # def add_hero(self):

    def remove_hero(self, name):
        found_hero = False
        # Loop through each hero in my list.
        for hero in self.heroes:
        # If i find the hero im looking for, remove them.
            if hero.name == name:
                self.heroes.remove(hero)
                # Set my indicator to True
                found_hero = True
        # If i looped through my list and didn't find my hero,
        # then indicator would never change, and return 0.
        if not found_hero:
            return 0
        
    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        self.heroes.append(hero)

    def stats(self):
        # Print team statistics
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f"{hero.name} Kill/Deaths:{kd}")
    
    def revive_heroes(self, health=100):
        # Reset all heroes health to starting_health
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        # Battle each team against each other
        living_heroes = list(self.heroes)
        living_opponents = list(other_team.heroes)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
        # Randomly select a living hero from each team
            hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)

        #have the heroes fight each other
            hero.fight(opponent)

        #update the list of living_heroes and living_opponents
        # to reflect the result of the fight
            if hero.is_alive():
                living_opponents.remove(opponent)
            else:
                living_heroes.remove(hero)
    
    # def view_all_heroes(self):


