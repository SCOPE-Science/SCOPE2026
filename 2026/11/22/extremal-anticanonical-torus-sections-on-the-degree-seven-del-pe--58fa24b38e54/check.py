#!/usr/bin/env python3
"""Exact footprint and finite-field rank checks for a toric surface evaluation code.

Runs on Python 3 standard library. No external files or network access required.
The finite-field loops corroborate, but do not replace, the infinite-field proof.
"""
from itertools import combinations
from collections import Counter

EXPONENTS = tuple((a, b) for a in range(3) for b in range(3) if a + b <= 3)
TARGET = (
    None, (1, -3, 2), (1, -2, 0), (1, -2, 1),
    (1, -1, -1), (1, -1, 0), (1, 0, -2),
    (1, 0, -1), (1, 0, 0)
)


def shadow_poly(S):
    # union of upper rectangles in [0,t-1]^2; inclusion-exclusion
    A = B = C = 0
    for n in range(1, len(S) + 1):
        sign = 1 if n % 2 else -1
        for T in combinations(S, n):
            i = max(a for a, b in T)
            j = max(b for a, b in T)
            A += sign
            B -= sign * (i + j)
            C += sign * i * j
    return (A, B, C)


def footprint_check():
    assert len(EXPONENTS) == 8
    assert EXPONENTS == ((0, 0), (0, 1), (0, 2), (1, 0),
                         (1, 1), (1, 2), (2, 0), (2, 1))
    counts = Counter()
    witnesses = {}
    for k in range(1, 9):
        target = TARGET[k]
        for S in combinations(EXPONENTS, k):
            a, b, c = shadow_poly(S)
            da, db, dc = a-target[0], b-target[1], c-target[2]
            # t=s+4, s>=0. Nonnegative coefficient certificate.
            assert da >= 0 and 8*da+db >= 0 and 16*da+4*db+dc >= 0, (k,S)
            if (a,b,c)==target:
                witnesses[k] = S
            counts[k] += 1
        assert k in witnesses
    print('FOOTPRINT_ALL_255_NONEMPTY_SUBSETS_OK')
    for k in range(1,9):
        print('r=%d subset_count=%d min_shadow_coefficients=%s witness=%s' %
              (k,counts[k],TARGET[k],witnesses[k]))


def reduce_rank(rows, p):
    # Exact Gauss-Jordan elimination, pivots always in canonical ascending order.
    basis = {}
    for vec in rows:
        w = list(vec)
        for j in sorted(basis):
            if w[j]:
                factor = w[j]
                w = [(x - factor*y) % p for x,y in zip(w,basis[j])]
        pivot = next((j for j,x in enumerate(w) if x), None)
        if pivot is None:
            continue
        w = [(x * pow(w[pivot], -1, p)) % p for x in w]
        for j, row in list(basis.items()):
            factor = row[pivot]
            if factor:
                basis[j] = [(x-factor*y)%p for x,y in zip(row,w)]
        basis[pivot] = w
    return [basis[j] for j in sorted(basis)]


def in_span(row, basis, p):
    w = list(row)
    for b in basis:
        j = next(i for i,z in enumerate(b) if z)
        if w[j]:
            factor = w[j]
            w = [(x-factor*y)%p for x,y in zip(w,b)]
    return not any(w)


def finite_field_extremizers(p):
    # Prime-field corroboration. Includes every possible rank-3/rank-4 flat.
    points = [(x,y) for x in range(1,p) for y in range(1,p)]
    rows = [tuple(pow(x,a,p)*pow(y,b,p)%p for a,b in EXPONENTS)
            for x,y in points]
    t = p-1
    assert len(reduce_rank(rows,p)) == 8
    for rank, size, expected in [(3,t,2*t), (4,t+1,2*t*t*(t-1))]:
        flats = set()
        for inds in combinations(range(t*t),rank):
            b = reduce_rank([rows[i] for i in inds], p)
            if len(b)!=rank:
                continue
            flat = tuple(i for i,v in enumerate(rows) if in_span(v,b,p))
            if len(flat)==size:
                flats.add(flat)
            else:
                assert len(flat)<size, (p,rank,inds,len(flat))
        assert len(flats)==expected, (p,rank,len(flats),expected)
        for flat in flats:
            S = {points[i] for i in flat}
            assert any(all(x==a for x,y in S if (x==a or y==0)) and
                       len({(x,y) for (x,y) in S if x==a})==t and
                       len(S)==size for a in range(1,p)) or any(
                len({(x,y) for (x,y) in S if y==b})==t and
                len(S)==size for b in range(1,p)), (p,rank,S)
        print('PRIME_FIELD_%d_RANK_%d_MAX_%d_OPTIMIZERS_%d_OK' %
              (p,rank,size,len(flats)))

if __name__ == '__main__':
    footprint_check()
    for p in (5,7):
        finite_field_extremizers(p)
    print('TORIC_DEGREE_SEVEN_OPTIMAL_SECTIONS_VERIFIED')
