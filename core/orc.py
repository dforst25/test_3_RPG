from core.monster import *


class Orc(Monster):
    def __init__(self, name):
        super().__init__(name, 50, randrange(6), randrange(10, 16), randrange(2, 9), "orc")
