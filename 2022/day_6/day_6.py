from more_itertools import windowed
from pathlib import Path


def get_marker(message: str, packet_length: int) -> int:
    return min(
        index + packet_length
        for index, window in enumerate(windowed(message, packet_length))
        if len(set(window)) == packet_length
    )


if __name__ == "__main__":
    puzzle_input = Path("./input").read_text().strip()

    print("Part One:", get_marker(puzzle_input, 4))
    print("Part Two:", get_marker(puzzle_input, 14))
