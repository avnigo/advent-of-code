from pathlib import Path

input_file = Path('day_3/input')

with open(input_file) as f:
    codes = [line.strip() for line in f.readlines()]
    # lines = [bin(int(line.strip(), base=2)) for line in f.readlines()]

most = b''
for i in range(len(codes[0])): # I hate this, but it's a must...
    tally = {'0': 0, '1': 0}
    for code in codes:
        tally[code[i]] += 1

    most += b'0' if tally['0'] > tally['1'] else b'1'

least = bytes(x^1 for x in most)

print(most)
print(least)

print(int(most, 2) * int(least, 2))

