import pandas as pd
import random
import re

slots = pd.read_csv('spells.csv')
pd.DataFrame(slots)

class Spells:
    def __init__(self, character_instance):
        self.spell_list = []
        self.character_instance = character_instance

    def add_spell(self):
        name = input("What is spell name?: \n").title()
        description = input("What description?: \n")
        spell_details = {"name": name, "description": description}
        self.spell_list.append(spell_details)

    def display_spells(self):
        print("Spell list: \n")
        for spells_dict in self.spell_list:
            for k, v in spells_dict.items():
                print(f'{v}', end='|')
            print()

    def remove_spell(self):
        name = input("What is spell name?: \n").title()
        for spell in self.spell_list:
            if name == spell.get('name'):
                self.spell_list.remove(spell)
                print(f'{name} has been removed')

    def display_slots(self):
        print(f"{'-'*30}\n")
        current_slots = slots.loc[slots['Level'] == self.character_instance.level]
        print(f"{current_slots}\n")
        print(f"{'-'*30}\n")

    @staticmethod
    def roll_dice(dice_notation):
        rolls = []
        for dice in re.findall(r'(\d+)d(\d+)', dice_notation):
            num_dice = int(dice[0])
            dice_type = int(dice[1])
            for _ in range(num_dice):
                rolls.append(random.randint(1, dice_type))
            return rolls

    def cast_spell(self):
        spell_to_cast_name = input("Which spell would you like to cast?: \n").title()
        spell_to_cast = None
        for spell in self.spell_list:
            if spell["name"] == spell_to_cast_name:
                spell_to_cast = spell
                break
        if spell_to_cast is None:
            print(f"The spell '{spell_to_cast_name}' is not in your spell list.")
            return

        level = input("Which level slot would you like to use to cast?"
                      "Type 0 for a Cantrip: \n").title()
        level_cast = f"Slot{level}"
        spell_description = spell_to_cast["description"]
        if len(spell_description) < 10:
            if level >= '1' or self.character_instance.level < 5:
                rolls = self.roll_dice(spell_description)
            elif 5 <= self.character_instance.level < 11:
                rolls = (self.roll_dice(spell_description) +
                         self.roll_dice(spell_description))
            elif 11 <= self.character_instance.level < 17:
                rolls = (self.roll_dice(spell_description) +
                         self.roll_dice(spell_description) +
                         self.roll_dice(spell_description))
            else:
                rolls = (self.roll_dice(spell_description) +
                         self.roll_dice(spell_description) +
                         self.roll_dice(spell_description) +
                         self.roll_dice(spell_description))
        else:
            rolls = self.roll_dice(spell_description)

        if rolls is not None:
            total_damage = sum(rolls)
            if level == '0':
                message = f'You cast {spell_to_cast_name}, dealing {total_damage} damage (rolls:{rolls})'
                print(f'{"*" * len(message)}')
                print(message)
                print(f'{"*" * len(message)}')
            else:
                available_slots = slots.loc[slots['Level'] == self.character_instance.level, level_cast]
                if available_slots.iloc[0] == 0:
                    message = f'No more spell slots for {level_cast}'
                    print(f'{"*" * len(message)}')
                    print(message)
                    print(f'{"*" * len(message)}')
                else:
                    slots.loc[slots['Level'] == self.character_instance.level, level_cast] -= 1
                    message = f'You cast {spell_to_cast_name}, dealing {total_damage} damage (roll(s):{rolls})'
                    print(f'{"*" * len(message)}')
                    print(message)
                    print(f'{"*" * len(message)}')
        else:
            message = f'You cast {spell_to_cast_name}, {spell_description}'
            print(f'{"*" * len(message)}')
            print(message)
            print(f'{"*" * len(message)}')
