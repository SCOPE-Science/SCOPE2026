#!/usr/bin/env python3
"""Exact finite checks of lattice discrepancy thresholds in box-slice Fano polytopes.

The unrestricted theorem uses the lattice-height argument, not these finite tests.
"""
from fractions import Fraction
from itertools import product
from math import gcd


def gauge(point, A, B):
    return max(Fraction(max(point), B), Fraction(-min(point), A))


def lattice_points(n, A, B):
    for head in product(range(-A, B + 1), repeat=n):
        tail=-sum(head)
        if -A<=tail<=B:
            yield head+(tail,)


def vertex(p, n, A, B):
    # An n-dimensional box section has a vertex only where >=n
    # independent coordinate inequalities become equalities.
    return sum(x in (-A,B) for x in p)>=n


def check():
    cases=0
    for n in range(2,5):
        for B in range(1,4):
            for A in range(B,n*B+1):
                if gcd(A,B)!=1: continue
                pts=list(lattice_points(n,A,B))
                nz=[p for p in pts if any(p)]
                md=min(gauge(p,A,B) for p in nz)
                canonical=all(gauge(p,A,B)>=1 for p in nz)
                terminal=all(vertex(p,n,A,B) for p in nz if gauge(p,A,B)<=1)
                assert md==Fraction(1,B),(n,A,B,md)
                assert canonical==(B==1),(n,A,B,'canonical')
                assert terminal==(n==2 and A==1 and B==1),(n,A,B,'terminal')
                cases+=1
                if (n,A,B) in [(2,1,1),(2,2,1),(2,3,2),(3,2,1),(3,3,2),(4,3,2)]:
                    print('n=%d A=%d B=%d mld=%s canonical=%s terminal=%s PASS' %
                          (n,A,B,str(md),canonical,terminal))
    for B in range(2,9):
        A=B+1
        n=2
        assert A<=n*B and gcd(A,B)==1
        alpha=Fraction(B,A+B)
        assert alpha<Fraction(1,2) and alpha>Fraction(1,3)
        assert gauge((1,-1,0),A,B)==Fraction(1,B)
    print('EXACT_TORIC_DISCREPANCY_CHECKS_PASS cases=%d boundary_sequence=7' % cases)

if __name__=='__main__':check()
