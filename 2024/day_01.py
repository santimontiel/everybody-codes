#!/usr/bin/env python3
# --- everybody.codes 2024: The Kingdom of Algorithmia ---
# --- Day 1: The Battle for the Farmlands ---

# --- Solution to Quest 1.
# Read the file.
with open("day_01_1.input") as f:
    data = f.read()

res = data.count("B") + 3 * data.count("C")
print(f"Result of Quest 1:      {res}")

# --- Solution to Quest 2.
# Read the file.
with open("day_01_2.input") as f:
    data = f.read()
data_pairs = [data[i:i+2] for i in range(0, len(data), 2)]

total_res = 0
for pair in data_pairs:
    res = pair.count("B") + 3 * pair.count("C") + 5 * pair.count("D")
    res = res + 2 if "x" not in pair else res
    total_res += res
print(f"Result of Quest 2:      {total_res}")


# --- Solution to Quest 3.
# Read the file.
with open("day_01_3.input") as f:
    data = f.read()
data_groups = [data[i:i+3] for i in range(0, len(data), 3)]

res, total_res = 0, 0
for group in data_groups:
    res = group.count("B") + 3 * group.count("C") + 5 * group.count("D")
    monsters = len(group) - group.count("x")
    if monsters > 1:
        res += monsters * (monsters - 1)
    total_res += res
print(f"Result of Quest 3:      {total_res}")