from collections import deque
from itertools import islice, pairwise
from pathlib import Path

def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) -> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


input_file = Path('input')

with open(input_file) as f:
    lines = [int(line.strip()) for line in f.readlines()]


groups = [sum(window) for window in sliding_window(lines, 3)]

print(sum([True for i,j in pairwise(groups) if j > i]))

