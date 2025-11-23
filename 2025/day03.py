#!/usr/bin/env python3
# --- everybody.codes 2025: The Song of Ducks and Dragons ---
# --- Quest 3: The Deepest Fit ---

# Solution to Part I.
with open("day03_1_input.txt", "r") as f:
    data = f.readlines()

numbers = [int(x) for x in data[0].strip().split(",")]
res = sum(set(numbers))
print(f"Solution to Part I: {res}")

# Solution to Part II.
with open("day03_2_input.txt", "r") as f:
    data = f.readlines()

numbers = [int(x) for x in data[0].strip().split(",")]
res = sum(sorted(set(numbers))[:20])
print(f"Solution to Part II: {res}")

# Solution to Part III.
with open("day03_3_input.txt", "r") as f:
    data = f.readlines()

numbers = sorted([int(x) for x in data[0].strip().split(",")])
crates = []

for num in numbers:
    pushed = 0
    if len(crates) == 0:
        crates.append([])
        crates[0].append(num)
        pushed = 1
    for crate in crates:
        if crate[-1] < num:
            crate.append(num)
            pushed = 1
            break
    if pushed == 0:
        crates.append([])
        crates[-1].append(num)
         
res = len(crates)
print(f"Solution to Part III: {res}")
