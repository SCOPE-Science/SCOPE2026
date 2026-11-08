#!/usr/bin/env python3
"""Exact finite stress tests for integer moment-curve diameter and equality cases.

The unrestricted theorem relies on its written inequalities, not these tests.
Run with: python3 verify.py
"""
from fractions import Fraction
from itertools import combinations


def moment(t, dimension):
    return tuple(t ** j for j in range(1, dimension + 1))


def sqdist(u, v):
    return sum((a-b)**2 for a, b in zip(u, v))


def predicted(d, m):
    if d % 2 or m == 1:
        return 4 * sum(m**(2*j) for j in range(1, d+1, 2)), {(-m, m)}
    return sum(m**(2*j) for j in range(1, d+1)), {(-m, 0), (0, m)}


def run():
    total_pairs = 0
    total_instances = 0
    subset_checks = 0
    for d in range(2, 17):
        for m in range(1, 17):
            pts = {t: moment(t,d) for t in range(-m, m+1)}
            bound, expected_pairs = predicted(d, m)
            actual_pairs = set()
            for a,b in combinations(range(-m, m+1), 2):
                val = sqdist(pts[a],pts[b]); total_pairs += 1
                assert val <= bound, (d,m,a,b,val,bound)
                if val == bound:
                    actual_pairs.add((a,b))
            assert actual_pairs == expected_pairs, (d,m,actual_pairs,expected_pairs)
            total_instances += 1
            # Nontrivial sparse T: vertex-pair equality is necessary/sufficient.
            if m <= 7 and d <= 9:
                for i in range(1, 16):
                    T = [t for t in range(-m,m+1) if ((t*t + 7*t + i*(t+9)) % 11) < 6]
                    if len(T) < 2: continue
                    pairs = {(a,b) for a,b in combinations(T,2)
                             if sqdist(pts[a],pts[b]) == bound}
                    assert pairs == {p for p in expected_pairs if p[0] in T and p[1] in T}
                    subset_checks += 1
    lemma_cases = 0
    for p in range(1, 16, 2):
        for m in range(2, 17):
            base = m**(2*p) + m**(2*p+2)
            for u in range(m+1):
                for v in range(m+1):
                    f = (u**p+v**p)**2 + (u**(p+1)-v**(p+1))**2
                    assert f <= base
                    assert (f == base) == (sorted([u,v]) == [0,m]), (p,m,u,v)
                    lemma_cases += 1
    # Discreteness really matters: for any even d and m>=2, a sufficiently
    # small real perturbation toward positive t makes (gamma(-m),gamma(t))
    # further apart than either endpoint-zero pair.
    for d in range(2, 17, 2):
        for m in range(2, 17):
            delta = Fraction(1,10**(3*d))
            a,b = moment(-m,d),moment(delta,d)
            assert sqdist(a,b) > predicted(d,m)[0], (d,m)
    print('EXACT_PASS instances=',total_instances,'pairs=',total_pairs,
          'sparse_subsets=',subset_checks,'integer_lemma_cases=',lemma_cases,'real_perturbations=',8*15)


if __name__ == '__main__':
    run()
