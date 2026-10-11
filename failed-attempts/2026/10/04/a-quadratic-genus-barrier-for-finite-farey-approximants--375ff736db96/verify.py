#!/usr/bin/env python3
from math import ceil

def genus_lb(n):
    assert n >= 6
    return 1 + ceil((n - 6) * (n + 1) / 12)

expected = {
    6: 1,
    7: 2,
    8: 3,
    9: 4,
    10: 5,
    11: 6,
    12: 8,
    13: 10,
    14: 11,
}

for n, g in expected.items():
    assert genus_lb(n) == g, (n, genus_lb(n), g)

# If V>=n+1 and nV<=6V-12+12g, then g cannot be below the claimed bound.
for n in range(6, 101):
    lb = genus_lb(n)
    for V in range(n + 1, n + 80):
        for g in range(lb):
            assert n * V > 6 * V - 12 + 12 * g

print("GENUS_LOWER_BOUNDS", [(n, genus_lb(n)) for n in range(6, 15)])
print("VERIFY_OK")
