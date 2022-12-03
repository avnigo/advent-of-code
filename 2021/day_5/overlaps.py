import numpy as np
from pathlib import Path
from dataclasses import dataclass
from enum import Enum, auto

class Line(Enum):
    VER = auto()
    HOR = auto()
    SLOPE = auto()

@dataclass
class Points:
    x: int
    y: int


@dataclass
class Pair:
    coords: list

    def parse(self, coords: list) -> list:
        return [int(coord) for coord in coords.split(',')]


    def slope(self) -> Line:
        # return (self.y2 - self.y1) / (self.x2 - self.x1)
        match self:
            case self if self.y1 == self.y2:
                return Line.VER
            case self if self.x1 == self.x2:
                return Line.HOR
            case _:
                return Line.SLOPE

    def __post_init__(self):
        start, stop = self.coords

        self.x1, self.y1 = self.parse(start)
        self.x2, self.y2 = self.parse(stop)

        self.coords = [Points(self.x1, self.y1), Points(self.x2, self.y2)]

        #self.slope = self.slope()


def main():
    input_file = Path('day_5/input')

    with open(input_file) as f:
        lines = [line.strip().split(' -> ') for line in f.readlines()]

    pairs = [Pair(line) for line in lines]
    ver_hor = [pair for pair in pairs if pair.slope() in (Line.VER, Line.HOR)]

if __name__ == '__main__':
    lines = main()
