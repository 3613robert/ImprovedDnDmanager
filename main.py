from character import Character
from menu import Menu
from weapons import Weapons
from spells import Spells
from save import Save
from dice_roller import DiceRoller
from inventory import Inventory
from battle import Battle
from short_rest import ShortRest

character = Character()
inventory = Inventory()
weapons = Weapons(character_instance=character)
spells = Spells(character_instance=character)
battle = Battle(character_instance=character, spells_instance=spells, weapon_instance=weapons)
save = Save(character_instance=character, weapons_instance=weapons, spells_instance=spells)
short_rest = ShortRest(character_instance=character, spells_instance=spells)
menu = Menu(character_instance=character,
            inventory_instance=inventory,
            weapons_instance=weapons,
            spells_instance=spells,
            save_instance=save,
            battle_instance=battle,
            short_rest_instance=short_rest)
dice_roller = DiceRoller()

menu.intro()
option = input("Type: \n"
               "(l) to load a character or \n"
               "(n) to create a new character?\n")
if option == 'l':
    save.load()
elif option == 'n':
    character.new_character()
menu.main_structure()