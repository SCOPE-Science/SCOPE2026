#!/usr/bin/env python3
"""Exact checks for Fourier-sparse affine-orbit matrix recovery over F_13.

Uses only the Python standard library. All calculations are integer or finite-field.
"""
from itertools import combinations

P = 13
U = tuple(range(1, P))
D = frozenset((0, 1, 3, 9))


def differences(s):
    return {(x - y) % P for x in s for y in s if x != y}


def ratios(s):
    return {(y * pow(x, -1, P)) % P for x in s for y in s if x != y}


def bareiss_det(M):
    """Division-exact integer determinant with deterministic pivoting."""
    a = [row[:] for row in M]
    n = len(a)
    if n == 0:
        return 1
    assert all(len(r) == n for r in a)
    prev = 1
    sign = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot = next((i for i in range(k + 1, n) if a[i][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                z = a[i][j] * pivot - a[i][k] * a[k][j]
                assert z % prev == 0
                a[i][j] = z // prev
        for i in range(k + 1, n):
            a[i][k] = 0
        prev = pivot
    return sign * a[-1][-1]


# Classification of the planar difference sets: testing 55 normalizations
# of four-sets containing 0,1 yields exactly these four patterns.
normal = []
for a, b in combinations(range(2, P), 2):
    s = (0, 1, a, b)
    if len(differences(s)) == P - 1:
        normal.append((a, b))
assert normal == [(3, 9), (4, 6), (5, 11), (8, 10)]

# Independent whole-space enumeration: exactly 52 four-sets are perfect
# additive difference sets, all affine images of the displayed Singer set.
perfect = {frozenset(s) for s in combinations(range(P), 4)
           if len(differences(s)) == P - 1}
affine = {frozenset((a*x+b) % P for x in D)
          for a in U for b in range(P)}
assert len(perfect) == len(affine) == 52 and perfect == affine

# Scaling does not change the quotient set. Test every admissible translation.
ratio_counts = {}
for b in range(P):
    s = frozenset((x + b) % P for x in D)
    if 0 not in s:
        ratio_counts[b] = len(ratios(s))
assert ratio_counts == {1: 8, 2: 9, 3: 8, 5: 9, 6: 9,
                        7: 7, 8: 7, 9: 8, 11: 7}

# Independent 495-case check: no four-subset of F_13^* has simultaneously
# all nonzero additive differences and at least 11 multiplicative ratios.
for s in combinations(U, 4):
    assert not (len(differences(s)) == 12 and len(ratios(s)) >= 11)

# Five-sparse witness; row index m=1,...,12, column n=2,...,12.
S = (1, 2, 3, 4, 11)
weights = (1, 2, 4, 8, 16)
f = dict(zip(S, weights))
assert 16*16 > 1*1 + 2*2 + 4*4 + 8*8  # all multiplicative Fourier coefficients nonzero
B = []
for m in U:
    row = []
    for n in range(2, P):
        x = (m * pow((1-n) % P, -1, P)) % P
        y = (n * x) % P
        row.append(f.get(x, 0) * f.get(y, 0))
    B.append(row)
minor = [B[m-1] for m in U if m != 4]
assert len(minor) == 11 and bareiss_det(minor) == -(2**43)
print('AFFINE13_SPARSE_RECOVERY_PASS normalizations=55 perfect_four_sets=52 '
      'nonzero_support_four_sets=495 translations=9 rank_minor=11 det=-2^43')

# Independent exact matrix-span certificate over F_53. The element 10 has
# order 13. Sending the complex cyclotomic integer zeta_13 to 10 (mod 53)
# is a ring map, so full rank after reduction certifies full rank over C.
Q = 53
OMEGA = 10
assert pow(OMEGA, 13, Q) == 1 and OMEGA != 1
assert sum(pow(OMEGA, j, Q) for j in range(13)) % Q == 0
orbit_rows = []
for k in range(P):
    for ell in U:
        orbit_rows.append([
            (f.get((ell*t) % P, 0) * f.get((ell*s) % P, 0)
             * pow(OMEGA, (-k*(t-s)) % P, Q)) % Q
            for t in U for s in U
        ])
assert len(orbit_rows) == 156 and len(orbit_rows[0]) == 144
r = 0
for j in range(144):
    piv = next((i for i in range(r, 156) if orbit_rows[i][j]), None)
    if piv is None:
        continue
    orbit_rows[r], orbit_rows[piv] = orbit_rows[piv], orbit_rows[r]
    inv = pow(orbit_rows[r][j], -1, Q)
    orbit_rows[r] = [(v * inv) % Q for v in orbit_rows[r]]
    for i in range(r + 1, 156):
        c = orbit_rows[i][j]
        if c:
            pi = orbit_rows[i]
            pr = orbit_rows[r]
            for z in range(j, 144):
                pi[z] = (pi[z] - c * pr[z]) % Q
    r += 1
    if r == 144:
        break
assert r == 144
print('AFFINE13_DIRECT_ORBIT_SPAN_PASS rows=156 cols=144 rank_mod_53=144 omega=10')
