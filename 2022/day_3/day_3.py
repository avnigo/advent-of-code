from string import ascii_letters
from pathlib import Path
from typing import Iterator
from more_itertools import divide, chunked


def get_common(*compartments: str | Iterator[str]) -> str:
    return "".join(set.intersection(*(set(c) for c in compartments)))


def get_sum_part_one(puzzle_input: list) -> int:
    return sum(
        bank[get_common(*compartments)]
        for compartments in (divide(2, sack) for sack in puzzle_input)
    )


def get_sum_part_two(puzzle_input: list) -> int:
    return sum(
        bank[group]
        for group in (get_common(*chunks) for chunks in chunked(puzzle_input, 3))
    )


if __name__ == "__main__":
    bank = {letter: index for index, letter in enumerate(ascii_letters, start=1)}
    puzzle_input = Path("./input").read_text().splitlines()

    print("Part One:", get_sum_part_one(puzzle_input))
    print("Part Two:", get_sum_part_two(puzzle_input))
