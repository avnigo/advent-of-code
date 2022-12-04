with open("./input") as file:
    inventory = file.read().split("\n")

# Scrappy solution, but it'll do for now.
totals = []
total = 0
for i in inventory:
    if not i:
        totals.append(total)
        total = 0
        continue

    total += int(i)

print(
    "PART 1 - top elf calories:",
    max(totals)
)
print(
    "PART 2 - calories of top 3 elves:",
    sum(sorted(totals, reverse=True)[:3])
)
