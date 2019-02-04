"""The classic Towers of Hanoi game."""

__author__ = "kaga"

class HanoiError(Exception):
    pass

class HanoiGame:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.towers = [[] for _ in range(width)]
        self.towers[0] = list(range(height, 0, -1))

    def __str__(self):
        row = lambda i: " ".join(str(tower[i])  if i < len(tower) else "|" for tower in self.towers)
        towers_str = '\n'.join(row(i) for i in range(self.height-1, -1, -1))
        return f"\n{' '.join(str(i) for i in range(self.width))}\n\n{towers_str}\n"

    def move(self, pop_tower, append_tower):
        if not self.towers[pop_tower]:
            raise HanoiError("You can't take a disk from an empty tower.")
        if self.towers[append_tower] and self.towers[pop_tower][-1] > self.towers[append_tower][-1]:
            raise HanoiError("You can't put a disk on that tower.")
        self.towers[append_tower].append(self.towers[pop_tower].pop())
        return len(self.towers[-1]) == self.height


if __name__ == "__main__":
    game = None
    while not game:
        try:
            game = HanoiGame(*map(int, input("Enter the game's height and width:\n").split()))
        except (TypeError, ValueError):
            print("\nPlease enter two numbers separated by a space.\n")

    while True:
        print(game)
        try:
            if game.move(*map(int, input("What's your next move?\n").split())):
                print(f"{game}\nCongrats! You won the game.\n")
                break
        except (TypeError, ValueError):
            print("\nPlease enter two numbers separated by a space.\n")
        except IndexError:
            print(f"\nChoose numbers between 0 and {game.width-1}")
        except HanoiError as e:
            print(f"\n{e}\n")
