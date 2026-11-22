#!/usr/bin/env python3
"""Exact finite verification of the four-variable bent shattering theorem.

Point x is the integer with its four binary coordinates. A function mask has
bit x equal to f(x). For quadratic monomials use (01,02,03,12,13,23).
No third-party packages or external data are required.
"""
from collections import Counter, deque
from itertools import combinations
import json
from pathlib import Path

ALL = (1 << 16) - 1
PAIRS = list(combinations(range(4), 2))


def rank_four(polar):
    rows = [0] * 4
    for j, (a, b) in enumerate(PAIRS):
        if polar >> j & 1:
            rows[a] ^= 1 << b
            rows[b] ^= 1 << a
    rank = 0
    for column in range(4):
        pivot = next((i for i in range(rank, 4) if rows[i] >> column & 1), None)
        if pivot is not None:
            rows[rank], rows[pivot] = rows[pivot], rows[rank]
            for i in range(4):
                if i != rank and (rows[i] >> column) & 1:
                    rows[i] ^= rows[rank]
            rank += 1
    return rank


def function_mask(q, linear, constant):
    mask = 0
    for x in range(16):
        bit = constant ^ ((x & linear).bit_count() & 1)
        bit ^= sum(((q >> j) & 1) * ((x >> a) & 1) * ((x >> b) & 1)
                   for j, (a, b) in enumerate(PAIRS)) & 1
        mask |= bit << x
    return mask


functions = sorted({function_mask(q, l, c)
                    for q in range(64) if rank_four(q) == 4
                    for l in range(16) for c in (0, 1)})
assert sum(rank_four(q) == 4 for q in range(64)) == 28
assert len(functions) == 896
assert Counter(f.bit_count() for f in functions) == {6: 448, 10: 448}
blocks = [f for f in functions if f.bit_count() == 10]
proper = bytearray(1 << 16)
nine = set()
for block in blocks:
    for x in range(16):
        if (block >> x) & 1:
            nine.add(block ^ (1 << x))
    s = (block - 1) & block
    while True:
        proper[s] = 1
        if s == 0:
            break
        s = (s - 1) & block
assert len(nine) == 4480
assert all(proper[s] for s in range(1 << 16) if s.bit_count() <= 6)
assert Counter(s.bit_count() for s in range(1 << 16) if proper[s]) == {
    0: 1, 1: 16, 2: 120, 3: 560, 4: 1820, 5: 4368,
    6: 8008, 7: 11200, 8: 10080, 9: 4480}

# Generators of AGL(4,2): four translations, three adjacent coordinate
# transpositions, three elementary coordinate additions.
generators = [tuple(x ^ (1 << i) for x in range(16)) for i in range(4)]
for i in range(3):
    generators.append(tuple((x & ~((1 << i) | (1 << (i + 1))))
                            | (((x >> i) & 1) << (i + 1))
                            | (((x >> (i + 1)) & 1) << i)
                            for x in range(16)))
for i in range(3):
    generators.append(tuple(x ^ (((x >> i) & 1) << (i + 1))
                            for x in range(16)))


def transport(s, perm):
    out = 0
    while s:
        low = s & -s
        out |= 1 << perm[low.bit_length() - 1]
        s -= low
    return out


rep = 0x0777
assert rep in nine
orb = {rep}
queue = deque([rep])
while queue:
    s = queue.popleft()
    for perm in generators:
        t = transport(s, perm)
        if t not in orb:
            orb.add(t)
            queue.append(t)
assert orb == nine

# The trace certificate verifies all 512 Boolean patterns on one nine-set.
xs = [x for x in range(16) if (rep >> x) & 1]
cert = json.loads((Path(__file__).parent / 'nine_trace_witnesses.json').read_text('utf8'))
assert cert['support_hex'] == '0x0777'
assert cert['points'] == xs
assert len(cert['truth_table_masks_hex']) == 512
function_set = set(functions)
for trace, raw in enumerate(cert['truth_table_masks_hex']):
    f = int(raw, 16)
    assert f in function_set
    assert sum(((f >> x) & 1) << j for j, x in enumerate(xs)) == trace

# Natural geometric descriptions of missing 7- and 8-sets.
hyperplanes = set()
for normal in range(1, 16):
    for c in range(2):
        hyperplanes.add(sum(1 << x for x in range(16)
                            if ((x & normal).bit_count() & 1) == c))
assert len(hyperplanes) == 30
bad7 = {s for s in range(1 << 16) if s.bit_count() == 7 and not proper[s]}
assert bad7 == {h ^ (1 << x) for h in hyperplanes for x in range(16) if (h >> x) & 1}

# For eight points, failure is exactly the existence of a nonzero
# complementing translation. (The three failure orbits have sizes 30,840,1920.)
def translate(s, t):
    return sum(1 << (x ^ t) for x in range(16) if (s >> x) & 1)

bad8 = {s for s in range(1 << 16) if s.bit_count() == 8 and not proper[s]}
assert len(bad8) == 2790
assert bad8 == {s for s in range(1 << 16) if s.bit_count() == 8
                and any(translate(s, t) == (ALL ^ s) for t in range(1, 16))}
# These 2790 failures split into exactly three affine-group orbits.
unseen = set(bad8)
missing_orbit_sizes = []
while unseen:
    start = next(iter(unseen))
    unseen.remove(start)
    orbit_queue = deque([start])
    orbit_size = 0
    while orbit_queue:
        s = orbit_queue.popleft()
        orbit_size += 1
        for perm in generators:
            t = transport(s, perm)
            if t in unseen:
                unseen.remove(t)
                orbit_queue.append(t)
    missing_orbit_sizes.append(orbit_size)
assert sorted(missing_orbit_sizes) == [30, 840, 1920]

# Distinct size-10 supports meet in at most eight points.
assert max((a & b).bit_count() for j, a in enumerate(blocks)
           for b in blocks[j + 1:]) == 8
print('QUADRATIC_BENT_FACE_CERTIFICATE_PASS')
