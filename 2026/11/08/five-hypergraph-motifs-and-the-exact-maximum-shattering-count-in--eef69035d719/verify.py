#!/usr/bin/env python3
"""Exhaustive combinatorial certificate for four-query Johnson rank-three shattering.
Requires only the Python standard library.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial

EXPECTED = {
    (5, 1): (12, Fraction(1, 2)),
    (6, 0): (12, Fraction(1, 2)),
    (6, 1): (13, Fraction(25, 48)),
    (7, 0): (3, Fraction(1, 8)),
}
# Each listed row is a three-subset of the coordinate labels 1,...,u.
MOTIFS = [
    (5, 1, ((2,3,4), (1,2,4), (1,2,5), (3,4,5))),
    (6, 0, ((1,5,6), (1,3,6), (2,3,6), (4,5,6))),
    (6, 1, ((3,5,6), (1,3,6), (2,3,6), (4,5,6))),
    (6, 1, ((1,5,6), (2,5,6), (3,5,6), (4,5,6))),
    (7, 0, ((1,6,7), (2,4,7), (3,4,7), (5,6,7))),
]


def all_traces(cols, outsider_count):
    universe = cols + [0] * outsider_count
    masks = set()
    for xyz in combinations(universe, 3):
        mask = 0
        for j in range(4):
            intersection = sum((cell >> j) & 1 for cell in xyz)
            if intersection == 2:
                mask |= (1 << j)
        masks.add(mask)
    return masks


def row_distinct(cols):
    return all(any(((v >> i) & 1) != ((v >> j) & 1) for v in cols)
               for i in range(4) for j in range(i+1, 4))


def permute_rows(m, p):
    b = [0] * 16
    for v in range(1, 16):
        newmask = sum(((v >> i) & 1) << p[i] for i in range(4))
        b[newmask] = m[v]
    return tuple(b)


def canonical(m):
    return min(permute_rows(m, p) for p in permutations(range(4)))


def multiplicity_vector(motifs):
    u = max(max(row) for row in motifs)
    a = [0] * 16
    for v in range(1, u + 1):
        mask = sum((v in row) << j for j, row in enumerate(motifs))
        assert mask
        a[mask] += 1
    return tuple(a)


def enumerate_certificates():
    vectors = []
    all_vectors = 0
    def visit(t, rem, m):
        nonlocal all_vectors
        if t == 16:
            if rem != (0,0,0,0):
                return
            all_vectors += 1
            cols = [v for v in range(1,16) for _ in range(m[v])]
            if not row_distinct(cols):
                return
            for outsiders in range(4):
                if len(all_traces(cols, outsiders)) == 16:
                    vectors.append((tuple(m), sum(m), outsiders))
                    break
            return
        touched = [j for j in range(4) if (t >> j) & 1]
        for count in range(1 + min(rem[j] for j in touched)):
            newrem = list(rem)
            for j in touched:
                newrem[j] -= count
            m[t] = count
            visit(t+1, tuple(newrem), m)
        m[t] = 0
    visit(1, (3,3,3,3), [0] * 16)
    assert all_vectors == 862, all_vectors
    assert len(vectors) == 40, len(vectors)
    grouped = defaultdict(list)
    for m, u, t in vectors:
        grouped[(u,t)].append(m)
    result = {}
    for key, v in grouped.items():
        weight = Fraction(0)
        for m in v:
            denom = 24
            for count in m[1:]:
                denom *= factorial(count)
            weight += Fraction(1, denom)
        result[key] = (len(v),weight)
    assert result == EXPECTED, (result, EXPECTED)
    motif_keys = {canonical(multiplicity_vector(m)): (u,t) for u,t,m in MOTIFS}
    assert len(motif_keys) == 5
    observed_keys = {canonical(m): (u,t) for m,u,t in vectors}
    assert observed_keys == motif_keys
    # Partition every accepted vector by one of the five exact motif orbits.
    orbits = Counter((u,t,canonical(m)) for m,u,t in vectors)
    assert sorted(orbits.values()) == [1,3,12,12,12], orbits
    print('EXACT_FINITE_CERTIFICATE_PASS vectors=862 accepted=40 motifs=5')
    for (u,t), (num,coef) in sorted(result.items()):
        print('UNION',u,'MIN_OUTSIDERS',t,'ORDERED_VECTORS',num,'COEFFICIENT',coef)
    return vectors


def closed_form(n):
    if n <= 5: return 0
    if n == 6: return 720
    falling5 = factorial(n)//factorial(n-5)
    assert falling5*(6*n*n - 17*n - 41)%48 == 0
    return falling5*(6*n*n - 17*n - 41)//48


def motif_count(n, vectors):
    result = Fraction(0)
    for m,u,t in vectors:
        if n < u+t:continue
        denominator = 24
        for c in m[1:]: denominator *= factorial(c)
        result += Fraction(factorial(n)//factorial(n-u), denominator)
    assert result.denominator == 1
    return int(result)

if __name__=='__main__':
    vv = enumerate_certificates()
    for n in range(3,19):
        got = motif_count(n,vv)
        expected = closed_form(n)
        assert got == expected,(n,got,expected)
        print('FORMULA',n,got)
    print('ALL_JOHNSON_RANK3_FOUR_CERTIFICATES_PASS')
