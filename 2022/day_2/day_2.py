from dataclasses import dataclass
from enum import Enum
from functools import total_ordering
from itertools import cycle


@total_ordering
class Choice(Enum):
    ROCK = ("SCISSORS", 1)
    PAPER = ("ROCK", 2)
    SCISSORS = ("PAPER", 3)

    def __init__(self, beats, points):
        self.beats = beats
        self.points = points

    def __gt__(self, other):
        return self.beats == other.name


class Result(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6

    
@dataclass
class RockPaperScissorsGame:
    human: Choice
    elf: Choice

    def __post_init__(self):
        self.result = self.battle()
        self.points = self.result.value + self.human.points


    def battle(self) -> Result:
        return (
            Result.WIN if self.human > self.elf
            else Result.DRAW if self.human == self.elf
            else Result.LOSS
        )


def part_one() -> int:
    cipher = {play: choice for play, choice in zip("ABCXYZ", cycle(Choice))}

    with open("./input") as file:
        plays = [
            RockPaperScissorsGame(
                elf=cipher[hands[0]],
                human=cipher[hands[1]],
            ) for line in file if (hands := line.strip().split(" "))
        ]

    return sum(p.points for p in plays)


if __name__ == "__main__":
    points = part_one()
    print(points)
