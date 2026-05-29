import unittest
from game.player import Player
from game.enemy import Enemy

class TestCombat(unittest.TestCase):

    def test_damage_reduction(self):
        player = Player("Test", 100, 20, 5)
        player.take_damage(20)
        self.assertTrue(player.health < 100)

    def test_enemy_death(self):
        enemy = Enemy("Test", 10, 10)
        enemy.take_damage(15)
        self.assertTrue(enemy.health <= 0)

if __name__ == "__main__":
    unittest.main()
