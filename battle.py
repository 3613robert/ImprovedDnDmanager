import random
import re

class Battle:
    def __init__(self, character_instance, spells_instance, weapon_instance):
        self.character_instance = character_instance
        self.spells_instance = spells_instance
        self.weapon_instance = weapon_instance

    def battle_menu(self):
        while True:
            message = f"Current hp: {self.character_instance.current_hp}/{self.character_instance.max_hp} and AC: {self.character_instance.ac}"
            print(f'{"*" * len(message)}')
            print(message)
            print(f'{"*" * len(message)}')
            print("Type:\n"
                  "(a) to make a weapon attack\n"
                  "(c) to cast a spell \n"
                  "(hit) if you're attacked \n"
                  "(healed) if you're healed \n"
                  "(d) for rolling death saving throws \n"
                  "(b) to go back")
            battle_option = input('What would you like to do?: \n')
            if battle_option == 'a':
                self.weapon_attack()
            elif battle_option == 'c':
                self.cast_spell()
            elif battle_option == 'hit':
                self.is_attacked()
            elif battle_option == 'healed':
                self.healed()
            elif battle_option == 'd':
                self.roll_saving_throws()
            elif battle_option == 'b':
                break

    def is_attacked(self):
        to_hit = int(input("What is the enemy attack roll?: \n"))
        if to_hit >= self.character_instance.ac:
            print("You've been hit")
            damage_taken = int(input("What is the damage?"))
            self.character_instance.current_hp -= damage_taken
            print(f"You're hp is currently {self.character_instance.current_hp}/{self.character_instance.max_hp}")
            if self.character_instance.current_hp <= 0:
                if self.character_instance.current_hp <= -self.character_instance.max_hp:
                    print('You are killed instantly')
                else:
                    self.character_instance.current_hp = 0
                    print('You are unconscious')

    def healed(self):
        healed_amount = int(input("How many hit points are you healed?: \n"))
        self.character_instance.current_hp += healed_amount
        if self.character_instance.current_hp > self.character_instance.max_hp:
            self.character_instance.current_hp = self.character_instance.max_hp
            print(f"You're hp is currently {self.character_instance.current_hp}/{self.character_instance.max_hp}")
        else:
            print(f"You're hp is currently {self.character_instance.current_hp}/{self.character_instance.max_hp}")

    @staticmethod
    def roll_dice(dice_notation):
        rolls = []
        for dice in re.findall(r'(\d+)d(\d+)', dice_notation):
            num_dice = int(dice[0])
            dice_type = int(dice[1])
            for _ in range(num_dice):
                rolls.append(random.randint(1, dice_type))
        return rolls

    def weapon_attack(self):
        weapon = input('With which weapon?: \n').lower()
        if weapon in self.weapon_instance.weapons:
            weapon_dice = self.weapon_instance.weapons[weapon]['damage']
            rolls = self.roll_dice(weapon_dice)
            attack_roll = random.randint(1, 20) + self.weapon_instance.weapons[weapon]['modifier']
            total_damage = sum(rolls) + self.weapon_instance.weapons[weapon]['stat']
            message = f"Attack Roll:{attack_roll} and damage is: {total_damage} (rolls: {rolls})"
            print(f'{"*" * len(message)}')
            print(message)
            print(f'{"*" * len(message)}')
        else:
            print(f"{weapon} not equipped as weapon")

    def cast_spell(self):
        self.spells_instance.display_spells()
        self.spells_instance.display_slots()
        spell_to_cast_name = input("Which spell would you like to cast?: \n").title()
        spell_to_cast = None
        for spell in self.spells_instance.spell_list:
            if spell["name"] == spell_to_cast_name:
                spell_to_cast = spell
                break
        if spell_to_cast is None:
            print(f"The spell '{spell_to_cast_name}' is not in your spell list.")
            return

        level = str(input("Which level slot would you like to use to cast?"
                          "Type 0 for a Cantrip: \n"))
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
        if self.character_instance._class in {'wizard', 'sorcerer', 'druid', 'cleric', 'bard'}:
            if rolls is not None:
                total_damage = sum(rolls)
                if level == '0':
                    message = f'You cast {spell_to_cast_name}, dealing {total_damage} damage (rolls:{rolls})'
                    print(f'{"*" * len(message)}')
                    print(message)
                    print(f'{"*" * len(message)}')
                else:
                    available_slots = self.spells_instance.slots.loc[self.spells_instance.slots['Level'] == self.character_instance.level, level_cast]
                    if available_slots.iloc[0] == 0:
                        message = f'No more spell slots for {level_cast}'
                        print(f'{"*" * len(message)}')
                        print(message)
                        print(f'{"*" * len(message)}')
                    else:
                        self.spells_instance.slots.loc[self.spells_instance.slots['Level'] == self.character_instance.level, level_cast] -= 1
                        message = f'You cast {spell_to_cast_name}, dealing {total_damage} damage (roll(s):{rolls})'
                        print(f'{"*" * len(message)}')
                        print(message)
                        print(f'{"*" * len(message)}')
            else:
                message = f'You cast {spell_to_cast_name}, {spell_description}'
                print(f'{"*" * len(message)}')
                print(message)
                print(f'{"*" * len(message)}')
        elif self.character_instance._class in {'paladin', 'ranger', 'artificer'}:
            if rolls is not None:
                total_damage = sum(rolls)
                if level == '0':
                    message = f'You cast {spell_to_cast_name}, dealing {total_damage} damage (rolls:{rolls})'
                    print(f'{"*" * len(message)}')
                    print(message)
                    print(f'{"*" * len(message)}')
                else:
                    available_slots = self.spells_instance.slots_half_caster.loc[self.spells_instance.slots_half_caster['Level'] == self.character_instance.level, level_cast]
                    if available_slots.iloc[0] == 0:
                        message = f'No more spell slots for {level_cast}'
                        print(f'{"*" * len(message)}')
                        print(message)
                        print(f'{"*" * len(message)}')
                    else:
                        self.spells_instance.slots_half_caster.loc[self.spells_instance.slots_half_caster['Level'] == self.character_instance.level, level_cast] -= 1
                        message = f'You cast {spell_to_cast_name}, dealing {total_damage} damage (roll(s):{rolls})'
                        print(f'{"*" * len(message)}')
                        print(message)
                        print(f'{"*" * len(message)}')

            else:
                message = f'You cast {spell_to_cast_name}, {spell_description}'
                print(f'{"*" * len(message)}')
                print(message)
                print(f'{"*" * len(message)}')
        elif self.character_instance._class == 'warlock':
            if rolls is not None:
                total_damage = sum(rolls)
                if level == '0':
                    message = f'You cast {spell_to_cast_name}, dealing {total_damage} damage (rolls:{rolls})'
                    print(f'{"*" * len(message)}')
                    print(message)
                    print(f'{"*" * len(message)}')
                else:
                    available_slots = self.spells_instance.slots_warlock.loc[self.spells_instance.slots_warlock['Level'] == self.character_instance.level, level_cast]
                    if available_slots.iloc[0] == 0:
                        message = f'No more spell slots for {level_cast}'
                        print(f'{"*" * len(message)}')
                        print(message)
                        print(f'{"*" * len(message)}')
                    else:
                        self.spells_instance.slots_warlock.loc[self.spells_instance.slots_warlock['Level'] == self.character_instance.level, level_cast] -= 1
                        message = f'You cast {spell_to_cast_name}, dealing {total_damage} damage (roll(s):{rolls})'
                        print(f'{"*" * len(message)}')
                        print(message)
                        print(f'{"*" * len(message)}')

            else:
                message = f'You cast {spell_to_cast_name}, {spell_description}'
                print(f'{"*" * len(message)}')
                print(message)
                print(f'{"*" * len(message)}')

    def roll_saving_throws(self):
        failed_rolls = 0
        success_rolls = 0
        unconscious = True
        while unconscious:
            option = input("Would you like to roll a death saving throw? y/n:\n")
            if option == 'y':
                death_roll = random.randint(1, 20)
                message = f"Roll: {death_roll}"
                print(f'{"*" * len(message)}')
                print(message)
                print(f'{"*" * len(message)}')
                if death_roll >= 10:
                    success_rolls += 1
                if death_roll < 10:
                    failed_rolls += 1
                print(f"Successful saving throws: {success_rolls} | Failed saving throws: {failed_rolls}")
                if success_rolls == 3:
                    self.character_instance.current_hp += 1
                    print('You are no longer unconscious and have 1 Hit Point')
                    break
                if failed_rolls == 3:
                    print('You are dead')
                    break
            if option == 'n':
                break