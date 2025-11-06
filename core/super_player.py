from random import randrange
from time import sleep

PROFESSION = ["warrior", "healer"]
WEAPON = ["knife", "sword", "axe"]
WEAPON_DAMAGE_MULT = {"knife": 0.5, "sword": 1, "axe": 1.5}


class SuperPlayer:
    def __init__(self, player_name, hp, speed, power, armor_rating):
        self.name = player_name
        self.hp = hp
        self.speed = speed
        self.power = power
        self.armor_rating = armor_rating

    def speak(self, player=""):
        print("The {} {} is angry!".format(player, self.name))

    def attack(self, damage, attacked):
        sleep(2)
        attacked.hp -= damage
        print(f"the hp of {attacked.name} was decrease {damage} to {attacked.hp} by {self.name}")
