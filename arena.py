from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self):
        # instance variables named team_one and team_two that will hold our teams.
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        name = input("What is the ability name? ")
        max_damage = input("What is the max damage of ability? ")

        return Ability(name, max_damage)
    
    def create_weapon(self):
        # Prompt the user for weapon information
        name = input("What is the weapon name? ")
        max_damage = input("What is the max damage of the weapon? ")

        # Create a new Weapon object using the input values and return it
        return Weapon(name, max_damage)
    
    def create_armor(self):
        # Prompt the user for armor information
        name = input("What is the armor name? ")
        max_block = input("What is the max block of the armor? ")

        # Create a new Armor object using the input values and return it
        return Armor(name, max_block)
    
    def create_hero(self):
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            if add_item == "1":
                # Add an ability to the hero
                ability = self.create_ability()
                hero.add_ability(ability)
            elif add_item == "2":
                # Add a weapon to the hero
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
            elif add_item == "3":
                # Add an armor to the hero
                armor = self.create_armor()
                hero.add_armor(armor)
        return hero
    
    def build_team_one(self):
        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        # Battle the teams together
        self.team_one.attack(self.team_two)

    
    def show_stats(self):
        '''Prints team statistics to terminal.'''
        print("\n")
        print(self.team_one.name + " statistics: ")
        self.print_team_stats(self.team_one)

        print("\n")
        print(self.team_two.name + " statistics: ")
        self.print_team_stats(self.team_two)
        print("\n")

        # This is how to calculate the average K/D for Team One
        print(self.team_one.name + " average K/D was: " + str(self.calculate_avg_kd(self.team_one)))

        # Calculate the average K/D for Team Two
        print(self.team_two.name + " average K/D was: " + str(self.calculate_avg_kd(self.team_two)))

        # Here is a way to list the heroes from Team One that survived
        print("\nSurvived from " + self.team_one.name + ":")
        self.list_surviving_heroes(self.team_one)

        # List the heroes from Team Two that survived
        print("\nSurvived from " + self.team_two.name + ":")
        self.list_surviving_heroes(self.team_two)

    def print_team_stats(self, team):
        '''Prints the statistics of a team.'''
        team.stats()

    def calculate_avg_kd(self, team):
        '''Calculates the average kill/death ratio for a team.'''
        team_kills = sum(hero.kills for hero in team.heroes)
        team_deaths = sum(hero.deaths for hero in team.heroes) or 1
        return team_kills / team_deaths

    def list_surviving_heroes(self, team):
        '''Lists the surviving heroes of a team.'''
        for hero in team.heroes:
            if hero.is_alive():
                print(hero.name)

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    # Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:
        arena.team_battle()
        arena.show_stats()

        play_again = input("Do you want to play again? (Y/N): ")

        # Check for Player Input
        if play_again.lower() == "n":
            print("Thanks for playing! Exiting the game.")
            game_is_running = False
        elif play_again.lower() == "y":
            # Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
            print("Teams have been revived for another battle.")
        else:
            print("Invalid input. Please enter 'Y' to play again or 'N' to exit.")

    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()