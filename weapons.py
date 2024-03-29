import random
import re

class Weapons:
    def __init__(self, character_instance):
        self.weapons = {}
        self.character_instance = character_instance

    def add_weapon(self):
        name = input("What weapon?: \n").lower()
        stat_used = input("What stat does the weapon use?: \n").lower()
        if stat_used == 'strength':
            stat = self.character_instance.str
            modifier = self.character_instance.str + self.character_instance.proficiency
            damage = input("what damage does the weapon have?: \n")
            weapon_details = {"stat": stat, "modifier": modifier, "damage": damage}
            self.weapons[f"{name}"] = weapon_details
        elif stat_used == 'dexterity':
            stat = self.character_instance.dex
            modifier = self.character_instance.dex + self.character_instance.proficiency
            damage = input("what damage does the weapon have?: \n")
            weapon_details = {"stat": stat, "modifier": modifier, "damage": damage}
            self.weapons[f"{name}"] = weapon_details

    def display_weapons(self):
        for k, v in self.weapons.items():
            print(f"{k}:{v}")

    def remove_weapon(self):
        name = input("What weapon would you like to remove?: \n").lower()
        if name in self.weapons:
            del self.weapons[name]
            print(f"Weapon '{name}' removed successfully.")
        else:
            print(f"Weapon '{name}' not equipped.")