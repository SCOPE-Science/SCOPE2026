"""Exact full regular-representation witness replay for three-tap A4 convolution.
Only the Python standard library is needed. Run: python3 verify_regular.py
"""
from fractions import Fraction
from itertools import permutations, combinations
from collections import Counter

S4 = list(permutations(range(4)))
identity = (0, 1, 2, 3)

def compose(p, q):
    return tuple(p[q[i]] for i in range(4))

def inverse(p):
    return tuple(p.index(i) for i in range(4))

def parity(p):
    return sum(p[i] > p[j] for i in range(4) for j in range(i+1, 4)) % 2

G = sorted(p for p in S4 if parity(p) == 0)
index = {p:i for i,p in enumerate(G)}

def order(p):
    z = identity
    for k in range(1, 13):
        z = compose(z, p)
        if z == identity:
            return k
    raise AssertionError('not an A4 element')

V = frozenset(p for p in G if order(p) in (1,2))
reps = [
    (identity,(0,2,3,1),(0,3,1,2)),            # C3 coset
    (identity,(0,2,3,1),(1,0,3,2)),            # 2+1 V4 cosets
    (identity,(0,2,3,1),(1,2,0,3)),            # transversal not a C3 coset
    (identity,(1,0,3,2),(2,3,0,1)),            # V4 coset
]
# Expected attainable ranks and one exact integer tap triple for each.
witnesses = [
    {4:(1,1,1), 8:(2,-1,-1), 12:(1,1,2)},
    {9:(9,-8,-7), 11:(2,-1,-1), 12:(1,1,1)},
    {9:(1,1,-1), 10:(1,1,1), 11:(2,-1,-1), 12:(1,1,2)},
    {9:(2,1,1), 12:(1,1,1)},
]

def rk(M):
    a = [[Fraction(t) for t in row] for row in M]
    nrows, ncols = len(a), len(a[0]); row = 0
    for col in range(ncols):
        k = next((i for i in range(row, nrows) if a[i][col]), None)
        if k is None:
            continue
        a[row], a[k] = a[k], a[row]
        pivot = a[row][col]
        for i in range(row+1, nrows):
            if a[i][col]:
                factor = a[i][col] / pivot
                for j in range(col+1, ncols):
                    a[i][j] -= factor*a[row][j]
                a[i][col] = 0
        row += 1
        if row == nrows:
            break
    return row

def convolution_rank(support, coeffs):
    M = [[0]*12 for _ in range(12)]
    for tap, coeff in zip(support,coeffs):
        for j,g in enumerate(G):
            M[index[compose(tap,g)]][j] += coeff
    return rk(M)

orbits = []
covered = {}
for representative in reps:
    maps = {}
    for left in G:
        for h in S4:
            h_inv = inverse(h)
            transported = tuple(compose(left,compose(h,compose(x,h_inv))) for x in representative)
            maps[frozenset(transported)] = transported
    orbits.append(maps)

assert tuple(len(z) for z in orbits) == (16,144,48,12)
for j, orb in enumerate(orbits):
    for support in orb:
        assert support not in covered, (j,support)
        covered[support] = j
assert len(covered) == 220 == len(list(combinations(G,3)))
assert set(covered) == set(map(frozenset, combinations(G,3)))

count = Counter()
for j, orb in enumerate(orbits):
    for permuted in orb.values():
        for target, coeffs in witnesses[j].items():
            actual = convolution_rank(permuted, coeffs)
            assert actual == target, (j, permuted, coeffs, target, actual)
            count[(j,target)] += 1
for j in range(4):
    for target in witnesses[j]:
        assert count[(j,target)] == len(orbits[j])
print('PASS group=A4 support_sets=220 orbit_sizes=16,144,48,12 exact_rank_witness_tests='+str(sum(count.values())))
for j in range(4):
    print('class',j,'attainable',sorted(witnesses[j]),'witness_supports',len(orbits[j]))
