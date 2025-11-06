from core.monster import *


class Goblin(Monster):
    def __init__(self, name):
        super().__init__(name, 20, randrange(5, 11), randrange(5, 11), 1, "goblin")

    def run_away(self):
        raise NotImplementedError()