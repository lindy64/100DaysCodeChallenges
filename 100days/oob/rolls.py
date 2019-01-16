import random

class Roll:

    def __init__(self, name, outcomes):
        self.name = name
        self.outcomes = outcomes


class Player:
    
    def __init__(self, name):
        self.name = name

    def roll(self, attacking_options):
        return random.choice(attacking_options)

