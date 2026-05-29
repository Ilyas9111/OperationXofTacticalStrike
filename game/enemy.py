import random

class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    @staticmethod
    def random_enemy():
        enemies = [
            ("Drone", 50, 10),
            ("Soldier", 80, 15),
            ("Tank", 120, 20)
        ]
        e = random.choice(enemies)
        return Enemy(e[0], e[1], e[2])

    def attack_damage(self):
        return random.randint(self.attack - 3, self.attack + 3)

    def take_damage(self, dmg):
        self.health -= dmg