from pathlib import Path

input_file = Path('day_2/input')

with open(input_file) as f:
    lines = [line.strip().split(' ') for line in f.readlines()]

x, y = 0, 0

for direction, amount in lines:
    match direction:
        case 'forward':
            x += int(amount)
        case 'up':
            y -= int(amount)
        case 'down':
            y += int(amount)

print(f'{x=}, {y=}, {x*y=}')
