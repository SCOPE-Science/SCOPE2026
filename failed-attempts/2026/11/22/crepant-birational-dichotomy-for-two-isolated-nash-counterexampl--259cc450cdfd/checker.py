"""Exact integer verification for two specified toric cyclic quotients.

No external packages or data required. This is a finite check of the lattice
calculations; the all-lattice-point and birational arguments appear in RESULT.md.
"""
from itertools import permutations
from math import gcd

CASES = ((11, (1, 2, 3, 5)), (9, (1, 2, 7, 8)))


def det4(rows):
    total = 0
    for p in permutations(range(4)):
        inv = sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4))
        total += (-1 if inv % 2 else 1) * (
            rows[0][p[0]] * rows[1][p[1]] * rows[2][p[2]] * rows[3][p[3]]
        )
    return total


def age_table(r, weights):
    assert sum(weights) % r == 0
    assert all(gcd(r, w) == 1 for w in weights)
    tab = []
    for k in range(1, r):
        residues = tuple((k * w) % r for w in weights)
        assert all(x > 0 for x in residues)
        assert sum(residues) % r == 0
        tab.append((k, residues, sum(residues) // r))
    return tab


TABLE11 = age_table(*CASES[0])
TABLE9 = age_table(*CASES[1])
assert tuple(age for _, _, age in TABLE11) == (1, 2, 2, 2, 2, 2, 2, 2, 2, 3)
assert tuple(age for _, _, age in TABLE9) == (2,) * 8

# The chosen N-basis is (v,e2,e3,e4), v=(1,2,3,5)/11.
# The original rays in N-coordinates are e1=(11,-2,-3,-5), e2,e3,e4.
v = (1, 0, 0, 0)
original = [(11, -2, -3, -5), (0, 1, 0, 0),
            (0, 0, 1, 0), (0, 0, 0, 1)]
assert abs(det4([[original[j][i] for j in range(4)] for i in range(4)])) == 11

local = {}
for missing in range(4):
    cols = [v] + [original[j] for j in range(4) if j != missing]
    mat = [[cols[j][i] for j in range(4)] for i in range(4)]
    index = abs(det4(mat))
    weight = CASES[0][1][missing]
    assert index == weight
    if index > 1:
        action = tuple(x % index for x in
                       ((11,) + tuple(-CASES[0][1][j] for j in range(4) if j != missing)))
        assert all(gcd(index, x) == 1 for x in action)
        assert all(age == 2 for _, _, age in age_table(index, action))
        local[index] = action
assert local == {2: (1, 1, 1, 1), 3: (2, 2, 1, 1), 5: (1, 4, 3, 2)}

print('order-11 age sequence:', [x[2] for x in TABLE11])
print('order-9 age sequence:', [x[2] for x in TABLE9])
print('star cone indices:', [1, 2, 3, 5])
print('singular terminal quotient charts:', local)
print('All exact integer checks passed.')
