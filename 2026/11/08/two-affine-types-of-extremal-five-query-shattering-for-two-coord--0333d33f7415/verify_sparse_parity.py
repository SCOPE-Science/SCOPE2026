#!/usr/bin/env python3
"""Exact finite certificate for extremal five-query two-coordinate parities.

Run: python3 verify_sparse_parity.py
All finite searches are exhaustive, with affine normalization justified in RESULT.md.
No external packages or files required.
"""
from itertools import combinations, permutations
from collections import Counter

D = 5
V = set(range(1 << D))
FRAME = (0, 1, 2, 4, 8, 16)
OUTSIDE = tuple(sorted(V - set(FRAME)))
CANON = (0, 1, 2, 3, 4, 5, 6, 8, 16, 31)

def sums(A):
    return {a ^ b for a, b in combinations(A, 2)}

def image_basis(z, pr):
    """Image of the canonical ordered affine frame under a candidate map."""
    cols = tuple(x ^ z for x in pr)
    img = [0] * 32
    for mask in range(1, 32):
        bit = mask & -mask
        img[mask] = img[mask ^ bit] ^ cols[bit.bit_length() - 1]
    return img

def full_affine_frames(A):
    """Every ordered affine-independent frame of six points in A."""
    for z in A:
        rest = tuple(x for x in A if x != z)
        for five in combinations(rest, 5):
            for pr in permutations(five):
                img = image_basis(z, pr)
                if len(set(img)) == 32:
                    yield z, img

# Exhaust all affine-normalized nine- and ten-point sets.
cover_10 = set()
max_9 = 0
count_9 = count_10 = 0
for extra in combinations(OUTSIDE, 3):
    A = FRAME + extra
    count_9 += 1
    max_9 = max(max_9, len(sums(A)))
assert count_9 == 2600 and max_9 == 28
for extra in combinations(OUTSIDE, 4):
    A = FRAME + extra
    count_10 += 1
    if sums(A) == V - {0}:
        cover_10.add(frozenset(A))
assert count_10 == 14950 and len(cover_10) == 80
assert sums(CANON) == V - {0}

# Independent affine-orbit enumeration from one representative.
seen = set()
auto = 0
point_images = {x: {x} for x in CANON}
num_frames = 0
for z, img in full_affine_frames(CANON):
    num_frames += 1
    inv = {v: i for i, v in enumerate(img)}
    B = frozenset(inv[x ^ z] for x in CANON)
    seen.add(B)
    if frozenset(z ^ img[x] for x in CANON) == frozenset(CANON):
        auto += 1
        for x in CANON:
            point_images[x].add(z ^ img[x])
assert seen == cover_10
assert num_frames == 80640
assert auto == 1008
point_orbits = {tuple(sorted(v)) for v in point_images.values()}
assert point_orbits == {(0,1,2,3,4,5,6), (8,16,31)}

# A complete direct trace certificate: d coordinate profiles, k query rows.
def trace_count(profiles):
    return len(sums(profiles))
assert trace_count(CANON + (0,)) == 32
assert trace_count((0,1,2,4,8,15,0)) == 16

# 7 affine planes in CANON; a duplicated profile in either orbit differs
# by the affine-invariant number of affine planes containing it.
planes = [C for C in combinations(CANON, 4) if C[0] ^ C[1] ^ C[2] ^ C[3] == 0]
assert len(planes) == 7
assert {x: sum(x in q for q in planes) for x in CANON} == {x: (4 if x < 7 else 0) for x in CANON}

AGL5 = 32 * 9999360
orbit_size = AGL5 // auto
assert AGL5 % auto == 0 and orbit_size == 317440
# Independent double count of all bases containing a specified ordered frame.
assert orbit_size * num_frames == AGL5 * len(cover_10)

print('SPARSE_PARITY_FIVE_SHATTERING_PASS')
print('nine_normalized',count_9,'max_nonzero_sums',max_9)
print('ten_normalized',count_10,'covering',len(cover_10))
print('ordered_affine_frames',num_frames,'stabilizer',auto,'orbit',orbit_size)
print('duplicate_point_orbits',list(sorted(point_orbits)))
print('affine_planes',len(planes),'trace_patterns',trace_count(CANON + (0,)))
