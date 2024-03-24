import json

class Save:
    def __init__(self, character_instance, spells_instance, weapons_instance):
        self.character_instance = character_instance
        self.spells_instance = spells_instance
        self.weapons_instance = weapons_instance

    def save(self):
        data = {
            'name': self.character_instance.name,
            '_class': self.character_instance._class,
            'str': self.character_instance.str,
            'dex': self.character_instance.dex,
            'con': self.character_instance.con,
            'wis': self.character_instance.wis,
            'int': self.character_instance.int,
            'cha': self.character_instance.cha,
            'level': self.character_instance.level,
            'proficiency': self.character_instance.proficiency,
            'other_stats': self.character_instance.other_stats,
            'casting_mod': self.character_instance.casting_mod,
            'spell_save': self.character_instance.spell_save,
            'current_hp': self.character_instance.current_hp,
            'max_hp': self.character_instance.max_hp,
            'hit_die': self.character_instance.hit_die,
            'hit_die_avg': self.character_instance.hit_die_avg,
            'ac': self.character_instance.ac,
            'weapons': self.weapons_instance.weapons,
            'spell_list': self.spells_instance.spell_list,
        }
        with open(f'{self.character_instance.name}.json', 'w') as f:
            json.dump(data, f)

        message = f'Successfully saved {self.character_instance.name}.json'
        print(f'{"*" * len(message)}')
        print(message)
        print(f'{"*" * len(message)}')

    def load(self):
        while True:
            character_name = input("Name of character?: \n")
            try:
                with open(f"{character_name}.json", 'r') as f:
                    data = json.load(f)
                    self.character_instance.name = data['name']
                    self.character_instance._class = data['_class']
                    self.character_instance.str = data['str']
                    self.character_instance.dex = data['dex']
                    self.character_instance.con = data['con']
                    self.character_instance.wis = data['wis']
                    self.character_instance.int = data['int']
                    self.character_instance.cha = data['cha']
                    self.character_instance.level = data['level']
                    self.character_instance.proficiency = data['proficiency']
                    self.character_instance.other_stats = data['other_stats']
                    self.character_instance.casting_mod = data['casting_mod']
                    self.character_instance.spell_save = data['spell_save']
                    self.character_instance.current_hp = data['current_hp']
                    self.character_instance.max_hp = data['max_hp']
                    self.character_instance.hit_die = data['hit_die']
                    self.character_instance.hit_die_avg = data['hit_die_avg']
                    self.character_instance.ac = data['ac']
                    self.weapons_instance.weapons = data['weapons']
                    self.spells_instance.spell_list = data['spell_list']
                message = f"Character '{self.character_instance.name}' loaded successfully."
                print(f'{"*" * len(message)}')
                print(message)
                print(f'{"*" * len(message)}')
                break
            except FileNotFoundError:
                print("Character not found, please try again")