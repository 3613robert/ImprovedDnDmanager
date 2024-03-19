import random

class DiceRoller:
    def __init__(self):
        pass

    @staticmethod
    def roller():
        while True:
            dice_map = {'d4': 4, 'd6': 6, 'd8': 8, 'd10': 10, 'd12': 12, 'd20': 20}
            dice = input("What dice would you like to roll? Type d4, d6, d8, d10, d12 or d20. Type (b) for return \n")
            if dice in dice_map:
                try:
                    amount = int(input("How many dice?: \n"))
                    dice_function = dice_map[dice]
                    for i in range(amount):
                        roll = random.randint(1, dice_function)
                        print(f"{'*'*5}Result {dice}: {roll}{'*'*5} ")
                except ValueError:
                    print('Please type a valid number of dice')
            elif dice == 'b':
                break
            else:
                print("Invalid dice choice. Please try again")
