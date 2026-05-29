import random

class Player:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def attack_damage(self):
        return random.randint(self.attack - 5, self.attack + 5)

    def take_damage(self, dmg):
        reduced = max(0, dmg - self.defense)
        self.health -= reduced