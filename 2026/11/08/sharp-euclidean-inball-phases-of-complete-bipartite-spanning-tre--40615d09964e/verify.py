#!/usr/bin/env python3
"""Exact finite checks for Euclidean radii of biclique spanning-tree polytopes.

No mathematical infinity claim is inferred from the test grid. Run python3 verify.py.
"""
from fractions import Fraction
from math import isclose


def check(p, q):
    assert 2 <= p <= q
    m = p*q
    t = p+q-1
    d0_squared = Fraction(t*t, m*(m-1))
    db_squared = Fraction((p-1)**2, m*(q-1))
    rank_dists = {}
    for r in range(1, p+1):
        for s in range(1, q+1):
            z = r*s
            if z == m:
                continue
            slack = Fraction((r+s-1)*m - t*z, m)
            assert slack > 0
            normal_squared = Fraction(z*(m-z), m)
            rank_dists[r,s] = slack*slack/normal_squared
    min_rank = min(rank_dists.values())
    nearest = {key for key, value in rank_dists.items() if value == min_rank}
    if (p,q) == (2,2):
        assert min_rank == Fraction(1, 12)
        assert nearest == {(1,1)}
    else:
        assert min_rank == db_squared, (p,q,min_rank,db_squared)
        expected = {(p,q-1)}
        if p == q:
            expected.add((p-1,q))
        if (p,q) == (3,3):
            expected.add((1,1))
        assert nearest == expected, (p,q,nearest,expected)
    predicted = Fraction(1,12) if (p,q)==(2,2) else min(d0_squared, db_squared)
    assert predicted == min(min_rank,d0_squared)
    outer_squared = Fraction(t*(m-t),m)
    assert outer_squared >= 0
    return len(rank_dists)


def main():
    profiles = cuts = 0
    for p in range(2, 13):
        for q in range(p, 71):
            cuts += check(p,q)
            profiles += 1
    # These are checks at finite parameters, not a proof of asymptotics.
    for p in (40,80,160,320):
        for c,expected in ((0.6,'coordinate'),(1.4,'degree')):
            q = max(p,round(c*p**1.5))
            m=p*q;t=p+q-1
            d0_sq=Fraction(t*t,m*(m-1))
            d1_sq=Fraction((p-1)**2,m*(q-1))
            if expected=='coordinate':
                assert d0_sq < d1_sq
            else:
                assert d1_sq < d0_sq
    print('BICLIQUE_TREE_INBALL_CHECKS_PASSED profiles=', profiles,
          'rank_orbit_distances=',cuts,'scaling_checks=',8)


if __name__ == '__main__':
    main()
