import random
from ability import Ability
from armor import Armor
from weapon import Weapon


class Hero:
    def __init__(self, name, starting_health=100, power=50):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.power = power
        self.abilities = []
        self.armor = []
        self.deaths = 0
        self.kills = 0
    
    # My ability
    def add_ability(self, ability):
        self.ability = ability
        # Appended my ability objects to my ability list.
        self.abilities.append(ability)
    
    # Attack 
    def attack(self):
    # Calculate the total damage from all ability attacks.
    # return: total_damage: int
        
        total_damage = 0

        for ability in self.abilities:
            # Add damage of each character to total
            total_damage += ability.attack()

        return total_damage
    
    # Shield
    def add_armor(self, armor):
        self.armor = armor
    
    # Defense
    def defend(self):
        total_block = 0

        for armor in self.armor:
            total_block += armor.block()
        
        return total_block
    
    # This allows me to store multiple weapons in my abilities list. 
    def add_weapon(self, weapon):
        self.abilities.append(weapon)
        
    
    # def take_damage(damage):
    
    # def is_alive():

    # Kill method
    def add_kill(self, num_kills):
        self.kills += num_kills

    # Add death statistics
    def add_death(self, num_deaths):
        self.deaths += num_deaths


    def fight(self, opponent):
        print(f"{self.name} vs. {opponent.name} - Fight!")

        # Calculate the toal power for both heroes.
        total_power = self.power + opponent.power

        # Calculate the chances of winning for each hero based on their power.
        self_chance = self.power / total_power
        opponent_chance = opponent.power / total_power

    
        
        # Continue the fight while both heros have health remaining.
        while self.current_health > 0 and opponent.current_health > 0: 
            winner = random.choices([self, opponent], [self_chance, opponent_chance])[0] # Randomly choose who attacks.
            if winner == self:
                opponent.current_health -= random.randint(1, 10) # Reduce opponents health by a random amount. 
            else:
                self.current_health -= random.randint(1, 10) # Reduce the hero's health by a random amount.

        # Determine the winner or declare a draw.
        if self.current_health > 0:
            print(f"{self.name} wins the battle against {opponent.name}!")

            #Update statistics
            self.add_kill(1)
            opponent.add_death(1)
        elif opponent.current_health > 0:
            print(f"{opponent.name} wins the battle against {self.name}!")

            #Update statistics
            self.add_kill(1)
            opponent.add_death(1)
        else:
            print("It's a draw!")

if __name__ == "__main__":
    hero = Hero("Thor")
    weapon = Weapon("Hammer", 200)
    hero.add_weapon(weapon)
    print(f"Bash!!! Damage: {hero.attack()}")
    hero.add_death(1)
    print("Deaths:", hero.deaths)



# ability = Ability("Great Debugging", 50)
#     # ability2 = Ability("Fire", 200)
#     hero1 = Hero("Spiderman", 300)
#     # hero2 = Hero("Superman", 250)
#     # hero1.add_ability(ability)
#     # hero1.add_ability(ability2)
#     armor1 = Armor("Shield", 40)
#     armor2 = Armor("Breast Plate", 60)

#     hero1.add_armor(armor1)
#     hero1.add_armor(armor2)

#     block_amount = hero1.defend()

#     # print(hero1.attack())
   
#     # hero1.fight(hero2) # Initiate a fight between our two heros.

