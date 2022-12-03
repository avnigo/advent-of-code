from pathlib import Path

input_file = Path('day_2/input')

with open(input_file) as f:
    lines = [line.strip().split(' ') for line in f.readlines()]

x, y, z = 0, 0, 0

for direction, amount in lines:
    match direction:
        case 'forward':
            x += int(amount)
            y += int(amount) * z
        case 'up':
            z -= int(amount)
        case 'down':
            z += int(amount)

print(f'{x=}, {y=}, {x*y=}')
