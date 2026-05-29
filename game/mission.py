class Mission:
    def __init__(self, enemy):
        self.enemy = enemy
        self.completed = False

    def finish(self):
        self.completed = True