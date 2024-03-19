import random

class DiceRoller:
    def __init__(self):
        self.d4 = 4
        self.d6 = 6
        self.d8 = 8
        self.d10 = 10
        self.d12 = 12
        self.d20 = 20

    def roller(self):
        while True:
            dice_map = {'d4': self.d4, 'd6': self.d6, 'd8': self.d8, 'd10': self.d10, 'd12': self.d12, 'd20': self.d20}
            dice = input("What dice would you like to roll? Type d4, d6, d8, d10, d12 or d20. Type (b) for return \n")
            if dice in dice_map:
                amount = int(input("How many dice?: \n"))
                dice_function = dice_map[dice]
                for i in range(amount):
                    roll = random.randint(1, dice_function)
                    print(f"{'*'*5}Result {dice}: {roll}{'*'*5} ")
            elif dice == 'b':
                break
            else:
                print("Invalid dice choice. Please try again")
