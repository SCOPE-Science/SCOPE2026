#!/usr/bin/env python3
"""Exhaustive binary-team classification by maximal functional envelopes."""
from collections import Counter
from itertools import product

ROWS = tuple(product((0, 1), repeat=4))
assert len(ROWS) == 16

envelopes = []
for f0, f1, g0, g1 in product((0, 1), repeat=4):
    mask = 0
    for i, (x, y, u, v) in enumerate(ROWS):
        if y == (f0, f1)[x] or v == (g0, g1)[u]:
            mask |= 1 << i
    envelopes.append(mask)
assert len(set(envelopes)) == 16
assert all(t.bit_count() == 12 for t in envelopes)

def model(team):
    return any(team & ~envelope == 0 for envelope in envelopes)

models = bytearray(model(t) for t in range(1 << 16))
minimal_bad = []
for team in range(1 << 16):
    if models[team]:
        continue
    if all(models[team ^ (1 << i)] for i in range(16) if (team >> i) & 1):
        minimal_bad.append(team)
counts = dict(sorted(Counter(t.bit_count() for t in minimal_bad).items()))
assert sum(models) == 32377
assert len(minimal_bad) == 132
assert counts == {4: 12, 5: 16, 6: 96, 8: 8}

# Bit-value permutations and exchange of the two ordered attribute pairs.
transforms = []
for swap in (False, True):
    for flips in product((0, 1), repeat=4):
        t = []
        for x, y, u, v in ROWS:
            bits = (u, v, x, y) if swap else (x, y, u, v)
            t.append(ROWS.index(tuple(b ^ f for b, f in zip(bits, flips))))
        transforms.append(t)
assert len(set(tuple(p) for p in transforms)) == 32

remaining = set(minimal_bad)
orbits = []
while remaining:
    base = min(remaining)
    orbit = {sum(1 << perm[i] for i in range(16) if base & (1 << i)) for perm in transforms}
    assert orbit <= remaining
    remaining.difference_update(orbit)
    orbits.append((base.bit_count(), len(orbit), f"0x{base:04x}"))
assert len(orbits) == 9
assert sum(orbit_size for _, orbit_size, _ in orbits) == 132
assert sorted(orbits) == sorted([
    (4, 4, '0x0033'), (4, 8, '0x003c'), (5, 16, '0x112c'),
    (6, 16, '0x143a'), (6, 32, '0x14a3'), (6, 16, '0x14aa'),
    (6, 16, '0x1863'), (6, 16, '0x1866'), (8, 8, '0x5a69')])
print('all teams:', len(models))
print('satisfying:', sum(models), 'violating:', len(models) - sum(models))
print('minimal-violation size polynomial:', counts)
print('minimal-violation orbit representatives (size, orbit, hex mask):')
for entry in orbits:
    print(*entry)
print('VERIFIED')
