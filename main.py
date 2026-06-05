from game.player import Player
from game.enemy import Enemy
from game.mission import Mission
from game.save_system import save_game, load_game


def fight(player, enemy):
    potions = 3

    print(f"\nMission started against {enemy.name}!")

    while player.health > 0 and enemy.health > 0:

        print("\n------------------")
        print(f"Your HP: {player.health}")
        print(f"Enemy HP: {enemy.health}")
        print(f"Potions: {potions}")
        print("------------------")

        print("1. Attack")
        print("2. Heal")
        print("3. Defend")

        choice = input("> ")

        defending = False

        if choice == "1":
            damage = player.attack_damage()
            enemy.take_damage(damage)
            print(f"You dealt {damage} damage!")

        elif choice == "2":
            if potions > 0:
                player.health += 25
                if player.health > 100:
                    player.health = 100
                potions -= 1
                print("You healed 25 HP!")
            else:
                print("No potions left!")

        elif choice == "3":
            defending = True
            print("You are defending!")

        else:
            print("Invalid choice!")
            continue

        if enemy.health <= 0:
            print(f"\n{enemy.name} defeated!")
            return True

        enemy_damage = enemy.attack_damage()

        if defending:
            enemy_damage = enemy_damage // 2

        player.take_damage(enemy_damage)

        print(f"{enemy.name} dealt {enemy_damage} damage!")

    print("\nYou were defeated!")
    return False


def main():
    print("Choose your character:")
    print("1. Soldier")
    print("2. Sniper")
    print("3. Tank")

    character = input("> ")

    if character == "1":
        player = Player("Soldier", 100, 20, 10)
    elif character == "2":
        player = Player("Sniper", 80, 30, 5)
    elif character == "3":
        player = Player("Tank", 150, 15, 20)
    else:
        player = Player("Soldier", 100, 20, 10)

    while True:
        print("\n====================")
        print("OPERATION X")
        print("====================")
        print("1. Start Mission")
        print("2. Save Game")
        print("3. Load Game")
        print("4. Exit")

        choice = input("> ")

        if choice == "1":
            enemy = Enemy.random_enemy()
            mission = Mission(enemy)

            if fight(player, enemy):
                mission.finish()
                print("Mission completed!")
            else:
                print("Mission failed!")

        elif choice == "2":
            save_game(player)
            print("Game saved!")

        elif choice == "3":
            try:
                player = load_game()
                print("Game loaded!")
            except FileNotFoundError:
                print("No save file found!")

        elif choice == "4":
            break


if __name__ == "__main__":
    main()