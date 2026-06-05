import random

class Enemy:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def attack_damage(self):
        return self.attack

    def take_damage(self, damage):
        self.health -= max(0, damage - self.defense)

    @staticmethod
    def random_enemy():
        enemies = [
            Enemy("Rogue", 70, 15, 5),
            Enemy("Soldier", 100, 20, 10),
            Enemy("Heavy", 140, 25, 15)
        ]
        return random.choice(enemies)