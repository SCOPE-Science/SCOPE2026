"""Exact finite certificate: ordinary zero forcing vs binary information sets.

Run: python3 clebsch_information_sets.py
Standard library only; all C(16,6)=8008 subsets are evaluated.
"""
from collections import Counter
from itertools import combinations
from functools import reduce

V = range(16)
STEP = (1, 2, 4, 8, 15)
ALL = (1 << 16) - 1
N = [sum(1 << (v ^ d) for d in STEP) for v in V]
COLUMNS = [N[v] | (1 << v) for v in V]


def rank(columns):
    piv = {}
    for col in columns:
        while col:
            leading = col.bit_length() - 1
            if leading not in piv:
                piv[leading] = col
                break
            col ^= piv[leading]
    return len(piv)


def zero_forces(whites):
    # Parallel forcing is equivalent to sequential existence for ultimate success.
    black = ALL ^ whites
    while True:
        new = 0
        for v in V:
            if black & (1 << v):
                w = N[v] & ~black
                if w and w & (w - 1) == 0:
                    new |= w
        new &= ~black
        if not new:
            return black == ALL
        black |= new


def shape(whites):
    return tuple(sorted((N[v] & whites).bit_count()
                        for v in V if whites & (1 << v)))


def act(whites, perm):
    return sum(1 << perm[v] for v in V if whites & (1 << v))


def orbit(seed, generators):
    found = {seed}
    frontier = [seed]
    for whites in frontier:
        for perm in generators:
            u = act(whites, perm)
            if u not in found:
                found.add(u)
                frontier.append(u)
    return found


assert rank(COLUMNS) == 6
assert Counter(x.bit_count() for x in
               reduce(lambda s, c: s | {x ^ c for x in s}, COLUMNS, {0})) == {
    0: 1, 6: 16, 8: 30, 10: 16, 16: 1
}
counts = Counter()
exceptions = set()
forcing = set()
for six in combinations(V, 6):
    whites = sum(1 << v for v in six)
    linear = rank(COLUMNS[v] for v in six) == 6
    forcing_status = zero_forces(whites)
    path_shape = shape(whites) == (0, 0, 0, 1, 1, 2)
    assert forcing_status == (linear and not path_shape), six
    counts[(linear, forcing_status, path_shape)] += 1
    if path_shape:
        exceptions.add(whites)
    if forcing_status:
        forcing.add(whites)
assert counts == Counter({(False, False, False): 3976,
                         (True, True, False): 3872,
                         (True, False, True): 160})
assert len(exceptions) == 160 and len(forcing) == 3872
# Translations and generator swaps generate the affine group F2^4 : S5.
generators = [[v ^ t for v in V] for t in (1, 2, 4, 8)]
for i in range(4):
    directions = list(STEP)
    directions[i], directions[i+1] = directions[i+1], directions[i]
    generators.append([reduce(int.__xor__,
                              (directions[j] for j in range(4) if v & (1 << j)), 0)
                       for v in V])
for perm in generators:
    assert len(set(perm)) == 16
    assert all(bool(N[v] & (1 << u)) == bool(N[perm[v]] & (1 << perm[u]))
               for v in V for u in V)
rep = sum(1 << v for v in (3, 4, 9, 10, 12, 15))
assert rep in exceptions and orbit(rep, generators) == exceptions
# An explicit failure of basis exchange among the *forcing* six-set complements.
a = sum(1 << v for v in (1, 6, 11, 12, 14, 15))
b = sum(1 << v for v in (1, 2, 5, 8, 10, 15))
assert a in forcing and b in forcing
assert all((a ^ (1 << 14) ^ (1 << y)) not in forcing for y in (2, 5, 8, 10))
assert shape(a ^ (1 << 14) ^ (1 << 10)) == (0, 0, 0, 1, 1, 2)
assert rank(COLUMNS[v] for v in V if (a ^ (1 << 14) ^ (1 << 10)) & (1 << v)) == 6
print('PASS: 8008 six-subsets; matrix rank 6; GF(2) code [16,6,6].')
print('PASS: 4032 binary matroid bases; 3872 forceable complements;')
print('      160 rank-six non-forceable P3+3K1 six-sets, one affine orbit.')
print('PASS: explicit matroid basis-exchange obstruction.')
