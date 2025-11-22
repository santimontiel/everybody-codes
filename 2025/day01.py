#!/usr/bin/env python3
# --- everybody.codes 2025: The Song of Ducks and Dragons ---
# --- Quest 1: Whispers in the Shell ---

# Solution to Part I.
with open("day01_1_input.txt", "r") as f:
    data = f.readlines()

names = data[0].strip().split(",")
raw_instructions = data[-1].strip().split(",")
instructions = [(inst[0], int(inst[1:])) for inst in raw_instructions]

pos = 0
limit = len(names) - 1

for move, steps in instructions:
    if move == "R":
        pos = min(limit, pos + steps)
    elif move == "L":
        pos = max(0, pos - steps)

final_name = names[pos]
print(f"Solution to Part I: {final_name}")    


# Solution to Part II.
with open("day01_2_input.txt", "r") as f:
    data = f.readlines()

names = data[0].strip().split(",")
raw_instructions = data[-1].strip().split(",")
instructions = [(inst[0], int(inst[1:])) for inst in raw_instructions]

pos = 0
limit = len(names) - 1

for move, steps in instructions:
    if move == "R":
        pos = pos + steps
        if pos > limit:
            pos = pos % len(names)
    elif move == "L":
        pos = pos - steps
        if pos < 0:
            pos = len(names) + pos

final_name = names[pos]
print(f"Solution to Part II: {final_name}")


# Solution to Part III.
with open("day01_3_input.txt", "r") as f:
    data = f.readlines()

names = data[0].strip().split(",")
raw_instructions = data[-1].strip().split(",")
instructions = [(inst[0], int(inst[1:])) for inst in raw_instructions]

limit = len(names) - 1
for move, steps in instructions:
    if move == "R":
        index = steps
        if index > limit:
            index = index % len(names)
    elif move == "L":
        index = limit - steps + 1
    names[0], names[index] = names[index], names[0]

final_name = names[0]
print(f"Solution to Part III: {final_name}")