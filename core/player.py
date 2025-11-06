from core.super_player import *


class Player(SuperPlayer):
    def __init__(self, name):
        super().__init__(name, 50, randrange(5, 11), randrange(5, 11), randrange(5, 15))
        self.profession = PROFESSION[randrange(2)]
        if self.profession == "healer":
            self.hp += 10
        if self.profession == "warrior":
            self.power += 2

    def speak(self, player=""):
        super().speak("player")

