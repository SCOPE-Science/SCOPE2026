#!/usr/bin/env python3
"""Independent literal-string checks for a sharp greedy-superstring witness."""
from itertools import permutations

inputs = ('0000', '0001', '0010', '0011', '0100', '0101', '1000', '1010')
steps = [
    ('1010', '0101', 3),
    ('1000', '0001', 3),
    ('10001', '0010', 3),
    ('100010', '0100', 3),
    ('1000100', '0011', 2),
    ('10101', '100010011', 1),
    ('1010100010011', '0000', 0),
]

def overlap(x, y):
    return max((t for t in range(1, min(len(x), len(y)) + 1)
                if x[-t:] == y[:t]), default=0)

active = list(inputs)
for x, y, k in steps:
    assert x != y and x in active and y in active
    m = max(overlap(a, b) for a in active for b in active if a != b)
    assert overlap(x, y) == k == m, (x, y, k, m)
    active.remove(x)
    active.remove(y)
    active.append(x + y[k:])
assert active == ['10101000100110000'], active

optimum = min(4 + sum(4 - overlap(x, y) for x, y in zip(order, order[1:]))
              for order in permutations(inputs))
assert optimum == 11
assert all(x in '00101000011' for x in inputs)
assert len(active[0]) == 17
print('WITNESS PASS n=8 optimum=11 greedy=17 ratio=17/11 steps=7')
