#!/usr/bin/env python3
"""Independent exact-integer checks for a rank-four root-lattice packet theorem.
Run with Python 3.10+: python verify_a4.py
No third-party modules or external data are needed.
"""
from itertools import combinations, permutations, product
from math import comb

N = 5

def sq(v):
    return sum(a*a for a in v)

def add(v, w):
    return tuple(a+b for a,b in zip(v,w))

def determinant(A):
    # Leibniz formula; 4x4 only, exact integer arithmetic.
    out = 0
    for perm in permutations(range(4)):
        inversions = sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
        term = (-1 if inversions%2 else 1)
        for i in range(4):
            term *= A[i][perm[i]]
        out += term
    return out

# Every possible nonzero A4 vector of norm squared at most 4.
short = set()
for first in product(range(-2, 3), repeat=4):
    v = first + (-sum(first),)
    if sq(v) in (2, 4):
        short.add(v)
short = sorted(short)
assert len(short) == 50
assert sum(sq(v)==2 for v in short) == 20
assert sum(sq(v)==4 for v in short) == 30

# A fitted packet of radius sqrt(6/5) forces every nonempty subset sum
# to have norm squared at most 24/5, hence at most 4 in A4.
expected = set()
for perm in permutations(range(N)):
    frame = []
    for i in range(N-1):
        v = tuple(int(j==perm[i])-int(j==perm[i+1]) for j in range(N))
        frame.append(v)
    expected.add(tuple(sorted(frame)))
assert len(expected) == 120

survivors = set()
searched = 0
for frame in combinations(short, 4):
    searched += 1
    sums = [tuple([0]*N)]
    possible = True
    for v in frame:
        shifted = [add(s, v) for s in sums]
        if any(sq(s) > 4 for s in shifted):
            possible = False
            break
        sums += shifted
    if not possible:
        continue
    if determinant([v[:4] for v in frame]) == 0:
        continue
    survivors.add(frame)
assert searched == comb(50,4) == 230300
assert survivors == expected, (len(survivors),len(expected),len(survivors^expected))
assert all(abs(determinant([v[:4] for v in frame])) == 1 for frame in survivors)

# Every oriented path's entire Kuhn packet admits explicit Euclidean balls;
# for a prefix chain the translated coordinate values are binary.
counts = {1:0, 2:0, 3:0, 4:0}
for frame in survivors:
    for order in permutations(frame):
        vertices = [tuple([0]*N)]
        for v in order:
            vertices.append(add(vertices[-1],v))
        a = tuple(-min(v[i] for v in vertices) for i in range(N))
        assert all(t in (0,1) for t in a)
        k = sum(a)
        assert 1 <= k <= 4
        for v in vertices:
            y = add(v,a)
            assert all(q in (0,1) for q in y)
            assert sum(y) == k
            # The center is c=(k/5)1-a. Squared distance is k(5-k)/5.
            assert sum((5*q-k)**2 for q in y) == 5*k*(5-k)
            assert k*(5-k) <= 6
        counts[k] += 1
assert sum(counts.values()) == 120*24 == 2880
assert counts == {1:120, 2:1320, 3:1320, 4:120}, counts
print('A4_PACKET_EXACT_OK; 50 short vectors; 230300 unordered tests;')
print('120 and only 120 candidate frames, all unimodular directed paths;')
print('2880 exact packet enclosing-sphere certificates; counts',counts)
