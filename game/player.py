class Player:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def attack_damage(self):
        return self.attack

    def take_damage(self, damage):
        self.health -= max(0, damage - self.defense)