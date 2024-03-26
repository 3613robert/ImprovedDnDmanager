import random

class ShortRest:
    def __init__(self, character_instance, spells_instance):
        self.character_instance = character_instance
        self.spells_instance = spells_instance

    def use_hit_die(self):
        print(f"Hit die: {self.character_instance.hit_die_left}/{self.character_instance.hit_die_max}")
        use_die = int(input('How many hit die would you like to use?'))
        while True:
            if use_die >= 1:
                self.character_instance.hit_die_left -= use_die
                if self.character_instance.hit_die_left >= 0:
                    for i in range(use_die):
                        heal_roll = random.randint(1, self.character_instance.hit_die)
                        self.character_instance.current_hp += heal_roll
                        print(f"{'*'*5}Roll:{heal_roll}{'*'*5}")
                        if self.character_instance.current_hp > self.character_instance.max_hp:
                            self.character_instance.current_hp = self.character_instance.max_hp
                    print(f"Your current HP: {self.character_instance.current_hp} | "
                          f"Hit die:{self.character_instance.hit_die_left}/{self.character_instance.hit_die_max}")
                    break
                else:
                    print('Not enough hit die left, try again with valid number of hit die')
            else:
                print(f"You've not used any hit die\n"
                      f"Your current HP: {self.character_instance.current_hp}"
                      f"Hit die:{self.character_instance.hit_die_left}/{self.character_instance.hit_die_max}")
                break

    def restore_slots_short_rest(self):
        if self.character_instance._class == 'warlock':
            self.spells_instance.restore_slots()