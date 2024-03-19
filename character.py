from proficiency_bonus import proficiency, stats
class Character:
    def __init__(self):
        self.name = ""
        self._class = ""
        self.str = 0
        self.dex = 0
        self.con = 0
        self.wis = 0
        self.int = 0
        self.cha = 0
        self.level = 0
        self.proficiency = 0
        self.other_stats = []
        self.casting_mod = 0
        self.spell_save = 0

    def new_character(self):
        self.name = input("What is your name?: \n")
        self._class = input("What class are you?: \n").lower()
        strength = int(input("What is your strength?: \n"))
        self.str = stats[strength]
        dexterity = int(input("What is your dexterity?: \n"))
        self.dex = stats[dexterity]
        constitution = int(input("What is your constitution?: \n"))
        self.con = stats[constitution]
        wisdom = int(input("What is your wisdom?: \n"))
        self.wis = stats[wisdom]
        intelligence = int(input("What is your intelligence?: \n"))
        self.int = stats[intelligence]
        charisma = int(input("What is your charisma?: \n"))
        self.cha = stats[charisma]
        self.level = int(input("What is your character level?: \n"))
        self.proficiency = proficiency[self.level]
        if self._class == "wizard" or self._class == 'artificer':
            self.casting_mod = self.int + self.proficiency
            self.spell_save = self.int + self.proficiency + 8
        elif self._class == "sorcerer" or self._class == "warlock" or self._class == "paladin" or self._class == "bard":
            self.casting_mod = self.cha + self.proficiency
            self.spell_save = self.cha + self.proficiency + 8
        elif self._class == "cleric" or self._class == "druid" or self._class == "ranger":
            self.casting_mod = self.wis + self.proficiency
            self.spell_save = self.wis + self.proficiency + 8

    def display_stats(self):
        other_stats_str = '\n'.join([f"{k}:{v}" for stat_dict in self.other_stats for k, v in stat_dict.items()])
        print(f"Name: {self.name} | Level: {self.level} | Class: {self._class}\n"
              f"Proficiency bonus: {self.proficiency}\n"
              f"Strength: {self.str}\n"
              f"Dexterity: {self.dex}\n"
              f"Constitution: {self.con}\n"
              f"Wisdom: {self.wis}\n"
              f"Intelligence: {self.int}\n"
              f"Charisma: {self.cha}\n"
              f"Spell casting modifier: {self.casting_mod}\n"
              f"Spell save DC: {self.spell_save}\n"
              f"{other_stats_str}\n")

    def add_stats(self):
        stat = input("Which stat would you like to add or change? "
                     "Type a new stat to add and existing stat to change: \n")
        value = input("Which modifier does the stat have?: \n")
        new_stat = {stat: value}
        self.other_stats.append(new_stat)

    def remove_stats(self):
        name = input("Which stat would you like to remove?: \n")
        for stat in self.other_stats:
            if name in stat:
                self.other_stats.remove(stat)
                print(f'{name} has been removed')
                break
