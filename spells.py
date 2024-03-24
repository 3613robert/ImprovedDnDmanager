import pandas as pd
import random
import re

slots = pd.read_csv('spells.csv')
pd.DataFrame(slots)

slots_half_caster = pd.read_csv('halfcaster.csv')
pd.DataFrame(slots_half_caster)

slots_warlock = pd.read_csv('warlock.csv')
pd.DataFrame(slots_warlock)

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
        if self.character_instance._class in {'sorcerer', 'wizard', 'bard', 'cleric', 'druid'}:
            current_slots = slots.loc[slots['Level'] == self.character_instance.level]
            print(f"{'-'*30}")
            print(f"{current_slots}")
            print(f"{'-'*30}")
        elif self.character_instance._class in {'paladin', 'ranger', 'artificer'}:
            print(f"{'-'*30}")
            current_slots = slots_half_caster.loc[slots['Level'] == self.character_instance.level]
            print(f"{current_slots}")
            print(f"{'-'*30}")
        elif self.character_instance._class == 'warlock':
            print(f"{'-'*30}")
            current_slots = slots_warlock.loc[slots['Level'] == self.character_instance.level]
            print(f"{current_slots}")
            print(f"{'-'*30}")

    def restore_slots(self):
        pass

