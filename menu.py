from dice_roller import DiceRoller

class Menu:
    def __init__(self, character_instance,
                 inventory_instance,
                 weapons_instance,
                 spells_instance,
                 save_instance,
                 battle_instance,
                 short_rest_instance):
        self.character_instance = character_instance
        self.inventory_instance = inventory_instance
        self.weapons_instance = weapons_instance
        self.spells_instance = spells_instance
        self.save_instance = save_instance
        self.battle_instance = battle_instance
        self.short_rest_instance = short_rest_instance

    @staticmethod
    def intro():
        print("Welcome to DnD character buddy")

    def main_structure(self):
        menu = True
        while menu:
            print("Type:\n"
                  "(s) for stats,\n"
                  "(sp) for spell list and slots\n"
                  "(i) for inventory,\n"
                  "(w) for weapons,\n"
                  "(d) for diceroller,\n"
                  "(b) for battle options,\n"
                  "(sr) for short rest, \n"
                  "(lr) for a long rest,\n"
                  "(sa) for save,\n"
                  "(l) for load\n")
            option = input("Where would you like to navigate?: \n")
            if option == 's':
                while True:
                    self.character_instance.display_stats()
                    options = input("Type:\n"
                                    "(a) to add stats,\n"
                                    "(r) to remove stats,\n"
                                    "(b) for back \n")
                    if options == 'a':
                        self.character_instance.add_stats()
                    elif options == 'r':
                        self.character_instance.remove_stats()
                    elif options == 'b':
                        break
            elif option == 'sp':
                while True:
                    self.spells_instance.display_slots()
                    self.spells_instance.display_spells()
                    option_spells = input("Type:\n"
                                          "(a) to add spell,\n"
                                          "(r) to remove,\n"
                                          "(b) for back\n")
                    if option_spells == 'a':
                        self.spells_instance.add_spell()
                    elif option_spells == 'r':
                        self.spells_instance.remove_spell()
                    elif option_spells == 'b':
                        break
            elif option == 'i':
                while True:
                    self.inventory_instance.display_inventory()
                    option_inventory = input("Type:\n"
                                             "(a) to add item(s),\n"
                                             "(r) to remove item(s),\n"
                                             "(b) for back \n")
                    if option_inventory == 'a':
                        self.inventory_instance.add_item()
                    elif option_inventory == 'r':
                        self.inventory_instance.remove_item()
                    elif option == 'b':
                        break
            elif option == 'w':
                while True:
                    self.weapons_instance.display_weapons()
                    option_weapons = input("Type: \n"
                                           "(a) to add weapon,\n"
                                           "(r) to remove,\n"
                                           "(b) for back\n")
                    if option_weapons == 'a':
                        self.weapons_instance.add_weapon()
                    elif option_weapons == 'r':
                        self.weapons_instance.remove_weapon()
                    elif option_weapons == 'b':
                        break
            elif option == 'd':
                dice_roller = DiceRoller()
                dice_roller.roller()
            elif option == 'b':
                self.battle_instance.battle_menu()
            elif option == 'sr':
                self.short_rest_instance.use_hit_die()
                self.short_rest_instance.restore_slots_short_rest()
            elif option == 'lr':
                self.character_instance.current_hp = self.character_instance.max_hp
                self.spells_instance.restore_slots()
            elif option == 'sa':
                self.save_instance.save()
            elif option == 'l':
                self.save_instance.load()
