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

    @staticmethod
    def roll_dice(dice_notation):
        rolls = []
        for dice in re.findall(r'(\d+)d(\d+)', dice_notation):
            num_dice = int(dice[0])
            dice_type = int(dice[1])
            for _ in range(num_dice):
                rolls.append(random.randint(1, dice_type))
        return rolls

    def display_weapons(self):
        for k, v in self.weapons.items():
            print(f"{k}:{v}")

    def attack(self):
        weapon = input('With which weapon?: \n').lower()
        # damage = self.weapons[weapon]['damage']
        weapon_dice = self.weapons[weapon]['damage']
        # amount_dice = self.weapons[weapon]
        rolls = self.roll_dice(weapon_dice)
        attack_roll = random.randint(1, 20) + self.weapons[weapon]['modifier']
        # damage_rolls = [random.randint(1, damage) for _ in range(amount_dice)]
        total_damage = sum(rolls) + self.weapons[weapon]['stat']
        message = f"Attack Roll:{attack_roll} and damage is: {total_damage} (rolls: {rolls})"
        print(f'{"*" * len(message)}')
        print(message)
        print(f'{"*" * len(message)}')

    def remove_weapon(self):
        name = input("What weapon would you like to remove?: \n").lower()
        if name in self.weapons:
            del self.weapons[name]
            print(f"Weapon '{name}' removed successfully.")
        else:
            print(f"Weapon '{name}' not found.")