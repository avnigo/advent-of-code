from dataclasses import dataclass
from enum import Enum
from functools import total_ordering
from itertools import cycle
from typing import List, Optional
from pathlib import Path


@total_ordering
class Choice(Enum):
    ROCK = (1, "SCISSORS", "PAPER")
    PAPER = (2, "ROCK", "SCISSORS")
    SCISSORS = (3, "PAPER", "ROCK")

    def __init__(self, points, beats, loses):
        self.points = points
        self.beats = beats
        self.loses_to = loses

    def __gt__(self, other):
        return self.beats == other.name


class Result(Enum):
    LOSS = 0
    DRAW = 3
    WIN = 6

    
@dataclass
class RockPaperScissorsGame:
    elf: Choice
    human: Optional[Choice] = None
    result: Optional[Result] = None

    def __post_init__(self):
        self.human = self.choice_from_result() if not self.human else self.human
        self.result = self.battle() if not self.result else self.result
        self.points = self.result.value + self.human.points

    def battle(self) -> Result:
        return (
            Result.WIN if self.human > self.elf
            else Result.DRAW if self.human == self.elf
            else Result.LOSS
        )

    def choice_from_result(self) -> Choice:
        return (
            Choice[self.elf.loses_to] if self.result == Result.WIN
            else self.elf if self.result == Result.DRAW
            else Choice[self.elf.beats]
        )


def part_one(puzzle_input: List[tuple], cipher: dict[str, Choice]) -> int:
    return sum(
        play.points for play in [
            RockPaperScissorsGame(
                elf=cipher[elf],
                human=cipher[human],
            ) for elf, human in puzzle_input
        ]
    )


def part_two(
        puzzle_input: List[tuple],
        play_cipher: dict[str, Choice],
        result_cipher: dict[str, Result]
    ) -> int:
    return sum(
        play.points for play in [
            RockPaperScissorsGame(
                elf=play_cipher[elf],
                result=result_cipher[result],
            ) for elf, result in puzzle_input
        ]
    )


def decode_cipher(letters: str, map_to: Choice|Result) -> dict[str, Choice|Result]:
    return {play: choice for play, choice in zip(letters, cycle(map_to))}  # type: ignore # issue: python/mypy#2305


def read_input(file: Path) -> List[tuple]:
    with open(file) as f:
        return [tuple(hands) for line in f if (hands := line.strip().split(" "))]


if __name__ == "__main__":
    puzzle_input = read_input(Path("./input"))

    points_1 = part_one(
        puzzle_input,
        cipher=decode_cipher("ABCXYZ", Choice)  # type: ignore
    )

    points_2 = part_two(
        puzzle_input,
        play_cipher=decode_cipher("ABC", Choice),  # type: ignore
        result_cipher=decode_cipher("XYZ", Result),  # type: ignore
    )

    print("Part One:", points_1)
    print("Part Two:", points_2)
    
