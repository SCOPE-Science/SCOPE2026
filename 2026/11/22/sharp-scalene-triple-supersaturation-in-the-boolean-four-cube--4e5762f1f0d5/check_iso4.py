#!/usr/bin/env python3
"""Finite exact certificate for the scalene-triple profile of a 4-cube.
No third-party modules, file inputs, or floating-point arithmetic.
"""
from itertools import combinations
from math import comb

N = 16
U = (1 << N) - 1
PARITY = tuple(sum(1 << v for v in range(N) if v.bit_count() % 2 == p) for p in (0, 1))

def d(u, v):
    return (u ^ v).bit_count()

triples = []
for a, b, c in combinations(range(N), 3):
    sides = {d(a, b), d(a, c), d(b, c)}
    if len(sides) == 3:
        triples.append((a, b, c))
assert len(triples) == 256
assert sum(tuple(sorted((d(a,b),d(a,c),d(b,c)))) == (1,2,3) for a,b,c in triples) == 192
assert sum(tuple(sorted((d(a,b),d(a,c),d(b,c)))) == (1,3,4) for a,b,c in triples) == 64

# Method A: exact dynamic recurrence. If h is highest included vertex,
# every newly created scalene triple has h as one of its vertices.
pairs_at = [[] for _ in range(N)]
for a,b,c in triples:
    pairs_at[c].append((1 << a) | (1 << b))
scalene = [0] * (1 << N)
for mask in range(1, 1 << N):
    h = mask.bit_length() - 1
    prior = mask ^ (1 << h)
    scalene[mask] = scalene[prior] + sum((prior & p) == p for p in pairs_at[h])

# Independent method B: direct membership scan over ALL 256 triples on
# every subset; this has 65,536 x 256 fixed integer-membership tests.
triple_masks = [(1<<a)|(1<<b)|(1<<c) for a,b,c in triples]
for mask in range(1 << N):
    direct = sum((mask & t) == t for t in triple_masks)
    assert scalene[mask] == direct, (mask, scalene[mask], direct)

mins = [10**9] * (N + 1)
counts = [0] * (N + 1)
for mask, value in enumerate(scalene):
    k = mask.bit_count()
    if value < mins[k]:
        mins[k] = value
        counts[k] = 1
    elif value == mins[k]:
        counts[k] += 1

EXPECTED_MIN = [0,0,0,0,0,0,0,0,0,16,36,60,88,124,164,208,256]
EXPECTED_COUNT = [1,16,120,304,316,144,56,16,2,16,48,64,32,64,48,16,1]
assert mins == EXPECTED_MIN, (mins, EXPECTED_MIN)
assert counts == EXPECTED_COUNT, (counts, EXPECTED_COUNT)

# Exact characterization of all equality cases for sizes at least six.
def is_described_extremizer(mask):
    k = mask.bit_count()
    if k < 6:
        raise ValueError('Only requested for k>=6')
    if k == 16:
        return True
    if 6 <= k <= 8:
        return any(mask & ~part == 0 for part in PARITY)
    r = k - 8
    for full in PARITY:
        if mask & full != full:
            continue
        residual = mask & (U ^ full)
        a = sum(((residual >> v) & 1) and ((residual >> (v ^ 15)) & 1)
                for v in range(8))
        # v<8 ensures each antipodal pair occurs once, since v xor 15 >=8.
        if a == max(0, r - 4):
            return True
    return False

for mask in range(1 << N):
    k = mask.bit_count()
    if k >= 6:
        assert (scalene[mask] == mins[k]) == is_described_extremizer(mask), mask

for k in range(8, 17):
    r = k-8
    assert mins[k] == 16*r + 4*comb(r,2) + 4*max(0,r-4)

# A conceptual local identity, checked independently for every B within
# the opposite parity class: scalene(E union B) = 16r+4*C(r,2)+4a(B).
for fixed in PARITY:
    other = U ^ fixed
    vs = [v for v in range(N) if other >> v & 1]
    for maskbits in range(1<<8):
        residual = sum(1<<vs[i] for i in range(8) if maskbits >> i & 1)
        r = maskbits.bit_count()
        antipodal = sum((residual>>v&1) and (residual>>(v^15)&1) for v in range(8))
        assert scalene[fixed | residual] == 16*r+4*comb(r,2)+4*antipodal
print('PASS: all 65,536 subsets, 256 scalene triples, exact minima, extremizers, and parity identity')
for k in range(6,17):
    print(f'k={k:2d} min={mins[k]:3d} extremizers={counts[k]}')
