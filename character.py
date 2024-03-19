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
        self.hp = 0
        self.hit_die = 0
        self.hit_die_avg = 0
        self.ac = 0

    def new_character(self):
        self.name = input("What is your name?: \n")
        self._class = input("What class are you?: \n").lower()

        def get_valid_input(prompt, stat):
            while True:
                try:
                    value = int(input(prompt))
                    return stats[value]
                except ValueError:
                    print(f'Please enter a valid number for {stat}')

        self.str = get_valid_input("What is your strength?: \n", 'strength')
        self.dex = get_valid_input("What is your dexterity?: \n", 'dexterity')
        self.con = get_valid_input("What is your constitution?: \n", 'constitution')
        self.wis = get_valid_input("What is your wisdom?: \n", 'wisdom')
        self.int = get_valid_input("What is your intelligence?: \n", 'intelligence')
        self.cha = get_valid_input("What is your charisma?: \n", 'charisma')

        while True:
            try:
                self.level = int(input("What is your character level?: \n"))
                self.proficiency = proficiency[self.level]
                self.ac = int(input("What is your ac?: \n"))
                break
            except ValueError:
                print('Please enter a valid number for character level and armor class')

        if self._class in {"wizard", 'artificer'}:
            self.casting_mod = self.int + self.proficiency
            self.spell_save = self.int + self.proficiency + 8
        elif self._class in {"sorcerer", "warlock", "paladin", "bard"}:
            self.casting_mod = self.cha + self.proficiency
            self.spell_save = self.cha + self.proficiency + 8
        elif self._class in {"cleric", "druid", "ranger"}:
            self.casting_mod = self.wis + self.proficiency
            self.spell_save = self.wis + self.proficiency + 8
        if self._class in {'sorcerer', 'wizard'}:
            self.hit_die = 6
            self.hit_die_avg = 4
        elif self._class in {'artificer', 'bard', 'cleric', 'druid', 'monk', 'rogue', 'warlock'}:
            self.hit_die = 8
            self.hit_die_avg = 5
        elif self._class in {'fighter', 'paladin', 'ranger'}:
            self.hit_die = 10
            self.hit_die_avg = 6
        elif self._class == 'barbarian':
            self.hit_die = 12
            self.hit_die_avg = 7
        self.hp = (self.con + self.hit_die) + (self.level * self.hit_die_avg - self.hit_die_avg)

    def display_stats(self):
        other_stats_str = '\n'.join([f"{k}:{v}" for stat_dict in self.other_stats for k, v in stat_dict.items()])
        print(f"Name: {self.name} | Level: {self.level} | Class: {self._class}\n"
              f"HP: {self.hp} | AC:{self.ac}\n"
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
