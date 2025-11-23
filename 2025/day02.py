#!/usr/bin/env python3
# --- everybody.codes 2025: The Song of Ducks and Dragons ---
# --- Quest 2: Whispers in the Shell ---

# Solution to Part I.
with open("day02_1_input.txt", "r") as f:
    data = f.readlines()

a = eval(data[0].strip()[2:])

def add(num_a, num_b):
    x = num_a[0] + num_b[0]
    y = num_a[1] + num_b[1]
    return (x, y)

def mul(num_a, num_b):
    x = num_a[0] * num_b[0] - num_a[1] * num_b[1]
    y = num_a[0] * num_b[1] + num_a[1] * num_b[0]
    return (x, y)

def div(num_a, num_b):
    if num_a[0] > 0:
        x = num_a[0] // num_b[0]
    else:
        x = (num_a[0] + num_b[0] - 1) // num_b[0]
    if num_a[1] > 0:
        y = num_a[1] // num_b[1]
    else:
        y = (num_a[1] + num_b[1] - 1) // num_b[1]
    return (x, y)


r = (0, 0)
for _ in range(3):
    r = mul(r, r)
    r = div(r, (10, 10))
    r = add(r, a)

res = f"[{r[0]},{r[1]}]"
print(f"Solution to Part I: {res}")


# Solution to Part II.
with open("day02_3_input.txt", "r") as f:
    data = f.readlines()

a = eval(data[0].strip()[2:])

counter = 0
delta = 10
for step_x in range(101):
    for step_y in range(101):
        r = (0, 0)
        p = add(a, (step_x * delta, step_y * delta))

        for _ in range(100):
            r = mul(r, r)
            r = div(r, (100000, 100000))
            r = add(r, p)
            if abs(r[0]) > 1000000 or abs(r[1]) > 1000000:
                counter += 1
                break

final_res = 101*101 - counter
print(f"Solution to Part II: {final_res}")


# Solution to Part III.
with open("day02_3_input.txt", "r") as f:
    data = f.readlines()

a = eval(data[0].strip()[2:])

counter = 0
delta = 1
for step_x in range(1001):
    for step_y in range(1001):
        r = (0, 0)
        p = add(a, (step_x * delta, step_y * delta))

        for _ in range(100):
            r = mul(r, r)
            r = div(r, (100000, 100000))
            r = add(r, p)
            if abs(r[0]) > 1000000 or abs(r[1]) > 1000000:
                counter += 1
                break

final_res = 1001*1001 - counter
print(f"Solution to Part III: {final_res}")

