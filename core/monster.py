from core.super_player import *


class Monster(SuperPlayer):
    def __init__(self, name, hp, speed, power, armor_rating, type):
        super().__init__(name, hp, speed, power, armor_rating)
        self.type = type
        self.weapon = WEAPON[randrange(3)]

    def speak(self, player=""):
        super().speak(self.type)

    def attack(self, damage, attacked):
        damage *= WEAPON_DAMAGE_MULT[self.weapon]
        super().attack(damage, attacked)