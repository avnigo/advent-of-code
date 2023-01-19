import re

from copy import deepcopy
from pathlib import Path
from types import SimpleNamespace


def load_stacks(puzzle_input: list) -> None:
    [
        getattr(stacks, mapping[index]).append(col)
        for line in puzzle_input
        for index, col in enumerate(line)
        if index in mapping.keys()
        if col != " "
    ]


def instructions(
    directions: list, stacks: SimpleNamespace, model: str
) -> SimpleNamespace:
    def by_model(times: int, from_: str, to_: str, model: str = model):
        move = getattr(stacks, from_)[-int(times) :]
        getattr(stacks, to_).extend(move if model == "9001" else move[::-1])
        del getattr(stacks, from_)[-int(times) :]

    for direction in directions:
        by_model(*re.findall(r"\d+", direction))

    return stacks


def top_crates(stacks: SimpleNamespace) -> str:
    return "".join(stack.pop() for _, stack in sorted(stacks.__dict__.items()))


if __name__ == "__main__":
    puzzle_input = Path("./input").read_text().splitlines()

    mapping = dict(
        zip(
            [1, 5, 9, 13, 17, 21, 25, 29, 33],
            (numstacks := [str(i) for i in range(1, 10)]),
        )
    )

    stacks = SimpleNamespace(**dict(zip(numstacks, [[] for _ in numstacks])))
    load_stacks(puzzle_input[:8][::-1])

    stacks_9000, stacks_9001 = deepcopy(stacks), deepcopy(stacks)

    print("Part One:", top_crates(instructions(puzzle_input[10:], stacks_9000, "9000")))
    print("Part Two:", top_crates(instructions(puzzle_input[10:], stacks_9001, "9001")))
