#!/usr/bin/env python3
"""Exact two-method certificate for a cubic in PG(2,64).

No third-party packages. Exhaustive finite-field incidence is a complete
finite proof for this single specified finite field, not for other fields.
"""
from collections import Counter

MOD = 0b1000011               # t^6+t+1
Q = 64

def mul(a, b):
    v = 0
    while b:
        if b & 1:
            v ^= a
        a <<= 1
        if a & 64:
            a ^= MOD
        b >>= 1
    return v

M = [[mul(a, b) for b in range(Q)] for a in range(Q)]
INV = [0] * Q
for a in range(1, Q):
    candidates = [b for b in range(1, Q) if M[a][b] == 1]
    assert len(candidates) == 1
    INV[a] = candidates[0]
assert all(M[a][b] == M[b][a] for a in range(Q) for b in range(Q))

def normalize(v):
    for t in v:
        if t:
            return tuple(M[INV[t]][w] for w in v)
    raise ValueError('zero triple')

def cross(p, q):
    a,b,c = p; d,e,f = q
    return normalize((M[b][f] ^ M[c][e],
                      M[c][d] ^ M[a][f],
                      M[a][e] ^ M[b][d]))

def incidence(p, ell):
    return M[p[0]][ell[0]] ^ M[p[1]][ell[1]] ^ M[p[2]][ell[2]] == 0

# Every projective point has exactly one representative in our chosen charts:
# z=1 for affine points; x=1 for nonvertical directions at infinity.
points = [(a,b,1) for a in range(Q) for b in range(Q)] + \
         [(1,m,0) for m in range(Q)] + [(0,1,0)]
assert len(points) == len(set(normalize(p) for p in points)) == 4161
curve = [p for p in points if M[M[p[1]][p[1]]][p[2]] ^
         M[p[1]][M[p[2]][p[2]]] ^ M[M[p[0]][p[0]]][p[0]] == 0]
assert len(curve) == 81
oncurve = set(curve)

# First certificate: all projective lines; incidence by field dot-products.
# The line array is independent of the particular representation of points.
all_lines = [normalize(p) for p in points]
assert len(set(all_lines)) == 4161
line_hist = Counter()
three_secants = []
for ell in all_lines:
    r = sum(incidence(p, ell) for p in curve)
    line_hist[r] += 1
    if r == 3:
        three_secants.append(ell)
assert line_hist == {0:1080, 1:1953, 2:72, 3:1056}, line_hist
assert len(three_secants) == 1056
m1 = {p: sum(incidence(p, ell) for ell in three_secants) for p in points}
expected_off = {11:72, 14:648, 16:2052, 17:864, 18:432, 26:12}
assert Counter(m1[p] for p in points if p not in oncurve) == expected_off
assert Counter(m1[p] for p in curve) == {39:72,40:9}

# Second certificate: an unrelated affine polynomial-root evaluation method.
# On y=m*x+c, the cubic is x^3+m^2*x^2+m*x+c^2+c=0.
# Build a root-count table independently of projective line incidence.
roots = [[0]*Q for _ in range(Q)]
for m in range(Q):
    m2 = M[m][m]
    for x in range(Q):
        x2 = M[x][x]
        value = M[x2][x] ^ M[m2][x2] ^ M[m][x]
        roots[m][value] += 1
assert all(sum(row) == Q for row in roots)

# For fixed x=a, a vertical line has 3 rational cubic points iff
# y^2+y=a^3 is solvable. Equivalently, a^3 lies in AS(F_64).
as_image = {M[y][y] ^ y for y in range(Q)}
assert len(as_image) == 32

m2 = {}
for p in points:
    a,b,z = p
    if z == 1:
        total = 0
        for m in range(Q):
            c = b ^ M[m][a]
            if roots[m][M[c][c] ^ c] == 3:
                total += 1
        if M[M[a][a]][a] in as_image:
            total += 1
    elif a == 1:
        # P=(1,m,0) is a direction point; enumerate parallel lines.
        total = sum(roots[b][M[c][c] ^ c] == 3 for c in range(Q))
    else:
        # O=(0,1,0) is the shared point at infinity of all verticals.
        total = sum(M[M[x][x]][x] in as_image for x in range(Q))
    m2[p] = total
assert m1 == m2

# The exceptional 26-trisecant locus is precisely PG(2,F4)\C.
four = {a for a in range(Q) if M[M[a][a]][M[a][a]] == a}
assert len(four) == 4
subplane = {p for p in points if all(v in four for v in p)}
assert len(subplane) == 21
assert len(subplane & oncurve) == 9
assert {p for p in curve if m1[p] == 40} == subplane & oncurve
assert {p for p in points if m1[p] == 26} == subplane - oncurve

# Pair-count checks involving elliptic-curve collinear triples.
assert 2*72 + 6*1056 == 81*80
assert 1*1953 + 2*72 + 3*1056 == 81*65
assert sum(k*n for k,n in expected_off.items()) + 72*39 + 9*40 == 1056*65
print('H64_TRISECANT_MULTIPLICITY_PASS')
print('line_intersections:', sorted(line_hist.items()))
print('curve_points:', len(curve), 'full_secants:', len(three_secants))
print('on_curve_multiplicity:', sorted(Counter(m1[p] for p in curve).items()))
print('off_curve_multiplicity:', sorted(expected_off.items()))
print('max_locus: PG(2,F4)\\curve, size',len(subplane-oncurve))
