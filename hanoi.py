class HanoiGame:
    def __init__(self, height):
        self.height = height
        self.towers = [list(range(height, 0, -1)), [], []]

    def __str__(self):
        row = lambda i: ' '.join(str(tower[i])  if i < len(tower) else '|' for tower in self.towers)
        towers_str = '\n'.join(row(i) for i in range(self.height-1, -1, -1))
        return f'0 1 2\n\n{towers_str}\n'

    def move(self, pop_tower, append_tower):
        if not self.towers[pop_tower]:
            raise ValueError("You can't take a disk from an empty tower.")
        if self.towers[append_tower] and self.towers[pop_tower][-1] > self.towers[append_tower][-1]:
            raise ValueError("You can't put a disk on that tower.")
        self.towers[append_tower].append(self.towers[pop_tower].pop())


game = HanoiGame(5)
while True:
    print(game)
    try:
        game.move(*map(int, input("What's your next move?").split()))
    except TypeError:
        print("Please enter two numbers followed by a space.")
    except ValueError as e:
        print(e)
