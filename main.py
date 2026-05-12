from game.player import Player
from game.enemy import Enemy
from game.mission import Mission
from game.save_system import save_game, load_game
import random

def fight(player, enemy):
    print(f"Fight starts: {player.name} vs {enemy.name}")

    while player.health > 0 and enemy.health > 0:
        input("Enter to attack")
        damage = player.attack_damage()
        enemy.take_damage(damage)
        print(f"You deal {damage} damage. Enemy HP: {enemy.health}")

        if enemy.health <= 0:
            break

        enemy_damage = enemy.attack_damage()
        player.take_damage(enemy_damage)
        print(f"Enemy deals {enemy_damage} damage. Your HP: {player.health}")

    return player.health > 0


def main():
    player = Player("Player", 100, 20, 10)

    while True:
        print("\n1. Mission\n2. Save\n3. Load\n4. Quit")
        choice = input("> ")

        if choice == "1":
            enemy = Enemy.random_enemy()
            mission = Mission(enemy)
            win = fight(player, enemy)
            print("Mission complete" if win else "You lost")

        elif choice == "2":
            save_game(player)
            print("Saved")

        elif choice == "3":
            player = load_game()
            print("Loaded")

        elif choice == "4":
            break


if __name__ == "__main__":
    main()