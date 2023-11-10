import random

class Armor:
    def __init__(self, name, max_block):
          self.name = name
          self.max_block = max_block

    def block(self):
        block = random.randint(0, 7)
        if block == 1:
            print("Blocked!")
            return True
        else:
            print("Block failed")
            return False

if __name__ == "__main__":
    armor = Armor("Debugging Shield", 10)
    print(armor.name)
    print(armor.block())