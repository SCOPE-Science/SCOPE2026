#!/usr/bin/env python3
"""Exact affine-orbit certificate for six-subsets of F_3^3."""
import itertools
import json
from collections import Counter
from pathlib import Path

P = list(itertools.product(range(3), repeat=3))
IDX = {x: i for i, x in enumerate(P)}

def add_basis(p, i):
    return tuple((p[j] + (i == j)) % 3 for j in range(3))

def swap01(p): return (p[1], p[0], p[2])
def swap12(p): return (p[0], p[2], p[1])
def shear(p): return ((p[0] + p[1]) % 3, p[1], p[2])
def scale(p): return ((2*p[0]) % 3, p[1], p[2])

MAPS = [
    [IDX[f(p)] for p in P]
    for f in [lambda p: add_basis(p, 0), lambda p: add_basis(p, 1),
              lambda p: add_basis(p, 2), swap01, swap12, shear, scale]
]
IMAGES = [[1 << t for t in transform] for transform in MAPS]

def transform(mask, images):
    result = 0
    while mask:
        b = mask & -mask
        result |= images[b.bit_length() - 1]
        mask -= b
    return result

def affine_dimension(indices):
    base = P[indices[0]]
    mat = [[(P[i][j] - base[j]) % 3 for j in range(3)] for i in indices[1:]]
    rank = 0
    for col in range(3):
        pivot = next((i for i in range(rank, len(mat)) if mat[i][col] != 0), None)
        if pivot is None:
            continue
        mat[rank], mat[pivot] = mat[pivot], mat[rank]
        inv = pow(mat[rank][col], -1, 3)
        mat[rank] = [(v * inv) % 3 for v in mat[rank]]
        for i in range(len(mat)):
            if i != rank:
                coef = mat[i][col]
                mat[i] = [(u - coef * v) % 3 for u, v in zip(mat[i], mat[rank])]
        rank += 1
    return rank

DIRECTIONS = [v for v in P if v != (0,0,0) and v[next(i for i in range(3) if v[i])] == 1]
assert len(DIRECTIONS) == 13

def zero_pairs(indices):
    total = 0
    for v in DIRECTIONS:
        counts = [0, 0, 0]
        for idx in indices:
            counts[sum(v[i] * P[idx][i] for i in range(3)) % 3] += 1
        total += (counts == [2, 2, 2])
    return total

remaining = {sum(1 << i for i in indices) for indices in itertools.combinations(range(27), 6)}
expected = json.loads((Path(__file__).resolve().parent / 'orbit_certificate.json').read_text())
assert len(remaining) == 296010
rows = []
while remaining:
    root = min(remaining)
    remaining.remove(root)
    stack = [root]
    size = 0
    while stack:
        mask = stack.pop()
        size += 1
        for im in IMAGES:
            other = transform(mask, im)
            if other in remaining:
                remaining.remove(other)
                stack.append(other)
    indices = [i for i in range(27) if (root >> i) & 1]
    j = zero_pairs(indices)
    rows.append({'representative': indices, 'size': size, 'j': j,
                 'rank': 27 - 2*j, 'dimension': affine_dimension(indices)})
assert rows == expected, (rows, expected)
assert sum(o['size'] for o in rows) == 296010
assert Counter({r: sum(o['size'] for o in rows if o['rank'] == r)
                for r in {o['rank'] for o in rows}}) == {
    9: 468, 15: 10530, 21: 78624, 23: 113724, 25: 75816, 27: 16848}
print('PASS: 10 full affine orbits, exhaustive partition of 296010 masks; exact ranks.')
