from itertools import pairwise
from pathlib import Path

input_file = Path('input')

with open(input_file) as f:
    lines = [int(line.strip()) for line in f.readlines()]

print(sum([True for i,j in pairwise(lines) if j > i]))

