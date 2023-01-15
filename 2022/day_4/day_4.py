from collections.abc import Generator
from pathlib import Path


def str_to_range(*ranges: str) -> Generator:
    return (
        range(int(low), int(high) + 1)
        for low, high in (rng.split("-") for rng in ranges)
    )


def check_subsets(x, y) -> bool:
    return x.issubset(y) or y.issubset(x)


def make_sets(pair: Generator) -> dict:
    return {key: set(range_set) for key, range_set in zip(("x", "y"), pair)}


def part_one(puzzle_input: list) -> Generator:
    return (
        check_subsets(**make_sets(pair))
        for pair in (str_to_range(*pair.split(",")) for pair in puzzle_input)
    )


if __name__ == "__main__":
    puzzle_input = Path("./input").read_text().splitlines()
    print(sum(part_one(puzzle_input)))
