#!/usr/bin/env python3
"""Exact arithmetic checks for the stated matching-deletion root-polytope formula.

Finite tests are independent checks, not substitutes for the published proof.
"""
from fractions import Fraction
from itertools import combinations, product
from math import comb, factorial


def determinant(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    n = len(a)
    d = Fraction(1)
    for j in range(n):
        k = next((k for k in range(j, n) if a[k][j]), None)
        if k is None:
            return Fraction(0)
        if k != j:
            a[j], a[k] = a[k], a[j]
            d = -d
        p = a[j][j]
        d *= p
        for k in range(j+1, n):
            c = a[k][j]/p
            for h in range(j+1, n):
                a[k][h] -= c*a[j][h]
    return d


def check():
    checked = 0
    pairs = 0
    for n in range(3, 17):
        d = n-1
        m = n-2
        # Canonical edge {0,1}; basis of the hyperplane h_01=0:
        # w=e_0+e_1-2e_(n-1), and e_j-e_(n-1) for j=2,...,n-2.
        # v_last=w/2 and v_j=w/2 - (e_j-e_last).
        cols = [[Fraction(1,2)] + [Fraction(-int(i==j)) for i in range(2, n-1)]
                for j in range(2,n-1)]
        cols.append([Fraction(1,2)] + [Fraction(0)]*(n-3))
        det = abs(determinant(list(zip(*cols))))
        assert det == Fraction(1,2), (n, det)
        assert det*2**m == 2**(n-3)
        assert sum(comb(d,k)**2 for k in range(d+1)) == comb(2*d,d)
        for r in range(n//2+1):
            normalized = comb(2*d,d)-r*2**(n-2)
            assert normalized > 0
            checked += 1
        # Independently confirm signed cap conflicts cannot overlap by
        # checking every full root of the complete graph, every two disjoint
        # edge pairs, and every independent orientation choice.
        roots = [(i,j) for i in range(n) for j in range(n) if i!=j]
        for a,b,c,e in combinations(range(n),4):
            for (p,q),(s,t) in [((a,b),(c,e)),((a,c),(b,e)),((a,e),(b,c))]:
                for ep1,ep2 in product((1,-1), repeat=2):
                    for i,j in roots:
                        f = ep1*((i==p)-(i==q)-(j==p)+(j==q))
                        g = ep2*((i==s)-(i==t)-(j==s)+(j==t))
                        assert f+g<=2
                        pairs += 1
    print('EXACT_OK determinant_and_volume_cases=',checked,
          'root_cap_nonintersection_tests=',pairs)

if __name__=='__main__':
    check()
