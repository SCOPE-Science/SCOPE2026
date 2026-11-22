#!/usr/bin/env python3
"""Finite consistency checks for the weighted Fermat--Ceva incidence argument.

This checks incidence and arithmetic only; the uniform proof uses Bezout.
"""
from fractions import Fraction


def check_incidence(m):
    triples = [(i, j) for i in range(m) for j in range(m)]
    # Grid point [zeta^i : zeta^j : 1]. Each family has m lines.
    families = [
        [set((i, j) for i, j in triples if (i-j-k) % m == 0) for k in range(m)],
        [set((i, j) for i, j in triples if (j-k) % m == 0) for k in range(m)],
        [set((i, j) for i, j in triples if (i+k) % m == 0) for k in range(m)],
    ]
    assert len(triples) == m*m
    assert all(len(line) == m for family in families for line in family)
    for point in triples:
        assert all(sum(point in line for line in family) == 1 for family in families)
    for a in range(3):
        for b in range(a+1, 3):
            assert all(len(x & y) == 1 for x in families[a] for y in families[b])
    for family in families:
        for x in range(m):
            for y in range(x+1, m):
                assert not (family[x] & family[y])
    # At each coordinate vertex, m lines of exactly one family are concurrent;
    # each coordinate side meets exactly two vertices, no grid point.
    assert 3*m == sum(len(f) for f in families)


def check_bounds(m, alpha, beta):
    u = m*alpha
    boundary = max(u+beta, 2*beta)
    # For curves not among the 3m pencil lines or three coordinate sides,
    # A + m B/3 <= m*d and B<=3*d/2, with d normalized to one.
    candidates = [u, u/2 + Fraction(3, 2)*beta]
    upper = max(candidates)
    assert upper <= boundary
    assert (u+beta if beta<=u else 2*beta) == boundary
    volume_sq = m*m*alpha*alpha + 3*beta*beta
    assert boundary*boundary >= volume_sq
    assert (boundary*boundary == volume_sq) == (beta == u)


def main():
    for m in range(2, 41):
        check_incidence(m)
        for a in (Fraction(1), Fraction(2, 3), Fraction(5, 4)):
            for b in (a/5, a*m/4, a*m/3, a*m/2, a, a*m, a*m*2, a*m*3):
                check_bounds(m, a, b)
        # The base-point-free pencil has 3 degree-2m special divisors;
        # its fiber has self-intersection zero and adjunction genus.
        assert (2*m)**2-m*m-3*m*m == 0
        assert 1 + (m*m-3*m)//2 == (m-1)*(m-2)//2
        # Each grid exceptional has fiber degree 1; each vertex exceptional degree m.
        assert 2*m - m - m == 0 # pencil lines
        assert 2*m - 2*m == 0   # coordinate sides
    print('PASS: exact grid incidences, two-weight bounds, isotropic class, genus for m=2..40')
    print('LIMIT: finite tests are not the Bezout proof or a classification of all pencil singular fibers')


if __name__ == '__main__':
    main()
