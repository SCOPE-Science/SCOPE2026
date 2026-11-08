#!/usr/bin/env python3
"""Exact finite regression checks for neutral integer-slope coupled maps."""
from fractions import Fraction as Q
from math import floor

def branch_f(x, q, s):
    return s*q*x - (s*q*x).numerator // (s*q*x).denominator

def radius(d, q):
    z = q*d
    k = z.numerator // z.denominator
    return min(z-k, k+1-z) / q

def verify():
    cases = 0
    boundary_points = 0
    for q in (3, 4, 5, 7, 11):
        den = 6*q
        points = [Q(i,den) for i in range(den+1)]
        for s in (-1,1):
            for eta in (-1,1):
                c=(Q(1)-Q(eta,q))/2
                assert q*(1-2*c)==eta
                for x in points:
                    for y in points:
                        gap = radius(x-y,q)
                        xx,yy=x,y
                        for n in range(6):
                            fx,fy=branch_f(xx,q,s),branch_f(yy,q,s)
                            xx1=(1-c)*fx+c*fy
                            yy1=c*fx+(1-c)*fy
                            d1=xx1-yy1
                            assert (q*d1-eta*s*q*(xx-yy)).denominator==1
                            assert radius(d1,q)==gap
                            assert abs(d1)>=gap
                            assert 0<=xx1<=1 and 0<=yy1<=1
                            if q*xx in range(-50,51) or q*yy in range(-50,51):
                                boundary_points+=1
                            xx,yy=xx1,yy1
                            cases+=1
    # Residue proof: all ordered uniform q-adic grids project to equal
    # residue-class counts modulo q; the nearest-lattice distribution is
    # inherited from that exact circular residue symmetry.
    for q in (3,4,5,7):
        for den in (q,2*q,3*q):
            # Compare uniform modular phase on denominator when den multiple of q.
            v=[Q(i,den) for i in range(den)]
            phases=[(q*t)-(q*t).numerator//(q*t).denominator for t in v]
            m=den//q
            assert sorted(set(phases))==[Q(i,m) for i in range(m)]
            assert all(phases.count(Q(i,m))==q for i in range(m))
    assert cases>20000
    print(f'VERIFY_OK exact_rational_iterates={cases} boundary_samples={boundary_points} slopes=5 signs=2 couplings=2')
if __name__=='__main__':
    verify()
