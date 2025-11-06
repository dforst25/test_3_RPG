from random import randrange
from time import sleep

from core.goblin import Goblin
from core.orc import Orc
from core.player import Player


class Game:

    @staticmethod
    def start():
        choice = ''
        while choice != 'E':
            Game.show_menu()
            choice = input().upper()
            if choice == 'B':
                player = Game.create_player()
                monster = Game.choose_random_monster()
                Game.battle(player, monster)
            elif choice != 'E':
                print("Invalid Input, try again: ")

    @staticmethod
    def show_menu():
        print(f"{'=' * 25} MENU {'=' * 25}\nType 'B' for Battle or 'E' for exit: ")

    @staticmethod
    def create_player():
        return Player("David")

    @staticmethod
    def choose_random_monster():
        rand = randrange(2)
        if rand:
            return Goblin("Joe")
        else:
            return Orc("Bob")

    @staticmethod
    def battle(player, monster):
        player_result_val = Game.roll_dice(6) + player.speed
        print(f"{player.name}'s result, dice: {player_result_val - player.speed} speed: {player.speed} total: {player_result_val}")
        monster_result_val = Game.roll_dice(6) + monster.speed
        print(f"{monster.name}'s result, dice: {monster_result_val - monster.speed} speed: {monster.speed} total: {monster_result_val}")
        attacker, attacked = (monster, player) if monster_result_val > player_result_val else (player, monster)

        print(f"{attacker.name} is beginning the battle!!!")
        while True:
            attacker_result_val = Game.roll_dice(20) + attacker.speed
            print(f"{attacker.name}'s result, dice: {attacker_result_val - attacker.speed} speed: {attacker.speed} total: {attacker_result_val}")
            print(f"the armor rating of {attacked.name} is: {attacked.armor_rating}")
            attacker.speak()
            if attacker_result_val > attacked.armor_rating:
                print(f"{attacker.name} hit the target!!!")
                damage = Game.roll_dice(6) + attacker.power
                print(f"{attacker.name}'s result, dice: {damage - attacker.power} power: {attacker.power} total damage: {damage}")
                attacker.attack(damage, attacked)
                if attacked.hp <= 0:
                    break
            else:
                print(f"{attacker.name} missed the target!!!")
            attacker, attacked = attacked, attacker

    @staticmethod
    def roll_dice(sides):
        sleep(5)
        result = randrange(1, sides + 1)
        return result
