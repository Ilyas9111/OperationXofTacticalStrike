import json
from game.player import Player

SAVE_FILE = "save.json"

def save_game(player):
    data = {
        "name": player.name,
        "health": player.health,
        "attack": player.attack,
        "defense": player.defense
    }

    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)


def load_game():
    with open(SAVE_FILE, "r") as f:
        data = json.load(f)

    return Player(
        data["name"],
        data["health"],
        data["attack"],
        data["defense"]
    )