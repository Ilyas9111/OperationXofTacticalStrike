class Mission:
    def __init__(self, enemy):
        self.enemy = enemy

    def finish(self):
        print(f"{self.enemy.name} defeated!")