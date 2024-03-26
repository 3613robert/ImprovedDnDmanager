import pandas as pd
import random
import re

original_slots = pd.read_csv('original_spells.csv')
pd.DataFrame(original_slots)
original_half_caster = pd.read_csv('original_half_caster.csv')
pd.DataFrame(original_half_caster)
original_warlock = pd.read_csv('original_warlock.csv')
pd.DataFrame(original_warlock)

class Spells:
    def __init__(self, character_instance):
        self.spell_list = []
        self.character_instance = character_instance
        self.sfc = pd.read_csv('spells.csv')
        self.slots = pd.DataFrame(self.sfc)
        self.shc = pd.read_csv('halfcaster.csv')
        self.slots_half_caster = pd.DataFrame(self.shc)
        self.sw = pd.read_csv('warlock.csv')
        self.slots_warlock = pd.DataFrame(self.sw)

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
            current_slots = self.slots.loc[self.slots['Level'] == self.character_instance.level]
            print(f"{'-'*30}")
            print(f"{current_slots}")
            print(f"{'-'*30}")
        elif self.character_instance._class in {'paladin', 'ranger', 'artificer'}:
            print(f"{'-'*30}")
            current_slots = self.slots_half_caster.loc[self.slots['Level'] == self.character_instance.level]
            print(f"{current_slots}")
            print(f"{'-'*30}")
        elif self.character_instance._class == 'warlock':
            print(f"{'-'*30}")
            current_slots = self.slots_warlock.loc[self.slots['Level'] == self.character_instance.level]
            print(f"{current_slots}")
            print(f"{'-'*30}")

    def restore_slots(self):
        if self.character_instance._class in {'sorcerer', 'wizard', 'bard', 'cleric', 'druid'} :
            self.slots.loc[self.slots['Level'] == self.character_instance.level] = original_slots.loc[original_slots['Level'] == self.character_instance.level].values
        elif self.character_instance._class in {'paladin', 'ranger', 'artificer'} :
            self.slots_half_caster.loc[self.slots_half_caster['Level'] == self.character_instance.level] = original_half_caster.loc[original_half_caster['Level'] == self.character_instance.level].values
        elif self.character_instance._class == 'warlock' :
            self.slots_warlock.loc[self.slots_warlock['Level'] == self.character_instance.level] = original_warlock.loc[original_warlock['Level'] == self.character_instance.level].values


