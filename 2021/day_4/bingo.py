import numpy as np
from pathlib import Path
from dataclasses import dataclass

@dataclass
class Card:
    grid: np.ndarray
    ID: int
    bingoed: bool = False

    def __post_init__(self):
        self.hits = np.zeros(self.grid.shape)

    def bingo(self, draw: int):
        print(f"\nWinning number {draw} in card:\n{self.grid}.\n\nHits:\n{self.hits}\n")

        unmarked = self.grid[np.where(self.hits==0)]

        print(
            f"The unmarked numbers are:\n{unmarked}\n... with a sum of {sum(unmarked)}"
            f"\nThe answer is winning number * sum of unmarked: {draw*sum(unmarked)}"
        )

        self.bingoed = True

        return True

    def check(self, draw: int):
        self.hits[np.where(self.grid==draw)] = 1

        h_sum = self.hits.sum(axis=1)/self.hits.shape[0]
        v_sum = self.hits.sum(axis=0)/self.hits.shape[0]

        if 1 in h_sum or 1 in v_sum:
            return self.bingo(draw)


def read_input(in_file):

    with open(in_file) as f:
        draw = [int(i) for i in f.readline().strip().split(',')]

    read = np.genfromtxt(in_file, skip_header=2, dtype=int)
    SHAPE = read.shape[1]

    # Assuming square bingo cards
    grids = np.split(read, len(read)/SHAPE)  

    cards = [Card(grid=raw, ID=i+1) for i, raw in enumerate(grids)]

    #del read, grids

    return draw, cards


def run_draw(draw, cards):
    for number in draw:
        print(number)
        for card in cards:
            if not card.bingoed:
                bingo = card.check(number)
                if bingo:
                    print(f"Card ID: {card.ID}")


if __name__ == '__main__':
    in_file = Path('day_4/input')
    draw, cards = read_input(in_file)
    run_draw(draw, cards)
