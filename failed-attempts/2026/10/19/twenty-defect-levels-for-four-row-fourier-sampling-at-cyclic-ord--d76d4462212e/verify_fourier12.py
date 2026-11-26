#!/usr/bin/env python3
"""Exact certificate for the four-by-four minor-incidence of F_12.

Requires only Python's standard library. All determinants are computed in
Z[zeta_12] and independently through four embeddings into F_61.
"""
from itertools import combinations, permutations
from collections import Counter

N = 12
ROWS = list(combinations(range(N), 4))
UNITS = (1, 5, 7, 11)
ROOTS = (21, 29, 32, 40)
P = 61
EXPECTED = (
    ((0, 1, 2, 3), 24, 0),
    ((0, 1, 2, 5), 48, 3),
    ((0, 1, 2, 4), 48, 15),
    ((0, 1, 3, 5), 24, 27),
    ((0, 1, 2, 6), 48, 39),
    ((0, 1, 3, 4), 24, 51),
    ((0, 1, 3, 7), 48, 63),
    ((0, 1, 2, 7), 12, 66),
    ((0, 1, 5, 6), 12, 69),
    ((0, 1, 3, 10), 12, 72),
    ((0, 1, 3, 6), 24, 90),
    ((0, 1, 3, 9), 48, 99),
    ((0, 1, 4, 5), 24, 99),
    ((0, 1, 4, 7), 24, 105),
    ((0, 1, 4, 9), 12, 171),
    ((0, 1, 4, 8), 24, 207),
    ((0, 2, 4, 6), 12, 255),
    ((0, 1, 6, 7), 6, 270),
    ((0, 2, 4, 8), 12, 303),
    ((0, 2, 6, 8), 6, 351),
    ((0, 3, 6, 9), 3, 414),
)
EXPECTED_DISTRIBUTION = {
    0:24, 3:48, 15:48, 27:24, 39:48, 51:24, 63:48, 66:12,
    69:12, 72:12, 90:24, 99:72, 105:24, 171:12, 207:24,
    255:12, 270:6, 303:12, 351:6, 414:3,
}


def orbit(a):
    return {tuple(sorted((u*x+b) % N for x in a))
            for u in UNITS for b in range(N)}


def finite_field_det(entries):
    """Gaussian elimination determinant in F_61: no tolerance or approximation."""
    m = [list(row) for row in entries]
    n = len(m)
    det = 1
    for i in range(n):
        pivot = next((j for j in range(i, n) if m[j][i] % P), None)
        if pivot is None:
            return 0
        if pivot != i:
            m[i], m[pivot] = m[pivot], m[i]
            det = -det
        t = m[i][i] % P
        det = det*t % P
        inv = pow(t, P - 2, P)
        for j in range(i + 1, n):
            fac = (m[j][i]*inv) % P
            for k in range(i + 1, n):
                m[j][k] = (m[j][k] - fac*m[i][k]) % P
            m[j][i] = 0
    return det % P


# zeta^4 = zeta^2 - 1, hence zeta^j is represented by four integers.
ZETA_POWERS = (
    (1,0,0,0), (0,1,0,0), (0,0,1,0), (0,0,0,1),
    (-1,0,1,0), (0,-1,0,1), (-1,0,0,0), (0,-1,0,0),
    (0,0,-1,0), (0,0,0,-1), (1,0,-1,0), (0,1,0,-1)
)
PERMS = [(s,(-1)**sum(s[i] > s[j] for i in range(4)
                                      for j in range(i+1,4)))
         for s in permutations(range(4))]


def cyclotomic_det(rowset, colset):
    """Return the 4 exact integer coordinates of the Fourier determinant."""
    v = [0,0,0,0]
    for perm, sign in PERMS:
        expo = sum(rowset[j] * colset[perm[j]] for j in range(4)) % N
        basis = ZETA_POWERS[expo]
        for k in range(4):
            v[k] += sign*basis[k]
    assert all(abs(x) <= 24 for x in v)
    return tuple(v)


def main():
    assert len(ROWS) == 495
    assert len(ROOTS) == 4 and len(set(ROOTS)) == 4
    assert all(pow(g, 12, P)==1 and pow(g, 6, P)!=1 and
               pow(g, 4, P)!=1 for g in ROOTS)
    assert all(pow(g,4,P)-pow(g,2,P)+1 == 0 or
               (pow(g,4,P)-pow(g,2,P)+1) % P == 0 for g in ROOTS)

    representatives = {}
    for R in ROWS:
        orb = orbit(R)
        rep = min(orb)
        representatives.setdefault(rep, orb)
    assert len(representatives) == 21
    assert sum(len(o) for o in representatives.values()) == len(ROWS)
    assert len(set().union(*representatives.values())) == len(ROWS)

    stats = []
    for rep, orb in representatives.items():
        d = 0
        for C in ROWS:
            # Independent proof of the zero decision: four finite-field
            # eigenvalues of the primitive 12th root and modular elimination.
            mod_values = []
            for primitive_root in ROOTS:
                f = [[pow(primitive_root, r*c, P) for c in C] for r in rep]
                mod_values.append(finite_field_det(f))
            is_zero = not any(mod_values)
            # Independently, use the 24 Leibniz terms in Z[zeta]/Phi_12.
            assert is_zero == (cyclotomic_det(rep,C) == (0,0,0,0)), (rep,C)
            d += is_zero
        stats.append((rep,len(orb),d))
    assert sorted(stats,key=lambda x:(x[2],x[0])) == list(EXPECTED)
    distribution = Counter()
    for rep, size, d in stats:
        distribution[d] += size
    assert dict(distribution) == EXPECTED_DISTRIBUTION
    assert sum(distribution.values())==495
    assert sum(d * size for d,size in distribution.items()) == 40608
    assert 495**2 == 245025
    assert sum(d * size for d,size in distribution.items()) * 9075 == 245025 * 1504
    # Distinct row orbits with same divisor occupancy distributions, but
    # different singularity incidence.
    for modulus in (2,3,4,6):
        def occupancies(R):
            return sorted(sum(int(x%modulus==r) for x in R) for r in range(modulus))
        assert occupancies((0,1,2,4)) == occupancies((0,1,3,5))
    assert {rep:d for rep,_,d in stats}[(0,1,2,4)] == 15
    assert {rep:d for rep,_,d in stats}[(0,1,3,5)] == 27
    for rep,size,d in sorted(stats,key=lambda x:(x[2],x[0])):
        print(f'R={rep} affine_orbit_size={size} singular_columns={d}')
    print('distribution:', sorted(distribution.items()))
    print('VERIFY_OK orbit_count=21 levels=20 singular_pairs=40608 total_pairs=245025 fraction=1504/9075')

if __name__ == '__main__':
    main()
