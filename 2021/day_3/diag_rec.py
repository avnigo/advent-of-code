from pathlib import Path


def get_leastmost(codes, index=0, most_common=True, filter_list=True):
    tally = {'0': 0, '1': 0}
    for code in codes:
        tally[code[index]] += 1

    most = b'1' if tally['1'] >= tally['0'] else b'0'
    least = bytes(x^1 for x in most)

    check = str(int(most)) if most_common else str(int(least))
    if not filter_list:
        return check

    fcodes = list(filter(lambda x: x[index] == check, codes))
    # print(tally, most, len(fcodes), sep='\t')

    if len(fcodes) > 1:
        return get_leastmost(fcodes, index=index+1, most_common=most_common)

    return fcodes[0]


def part_one(codes):

    # TODO: not currently working...
    for i in range(len(codes[0])): # I hate this, but it's a must...
        print(get_leastmost(codes, index=0, filter_list=False))


def part_two(codes):
    oxy_gen = get_leastmost(codes)
    print(f"{oxy_gen=}")

    co2_scrub = get_leastmost(codes, most_common=False)
    print(f"{co2_scrub=}")

    print(int(oxy_gen, 2) * int(co2_scrub, 2))


def main():
    input_file = Path('day_3/input')

    with open(input_file) as f:
        codes = [line.strip() for line in f.readlines()]

    part_one(codes)
    part_two(codes)

if __name__ == '__main__':
    main()
