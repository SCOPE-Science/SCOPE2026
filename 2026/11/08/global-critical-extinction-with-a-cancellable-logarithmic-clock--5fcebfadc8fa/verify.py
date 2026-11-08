#!/usr/bin/env python3
"""Finite reproducibility checks for a two-population critical map.
Uses Python 3 standard library; no external dependencies.
Computations do not prove universal limits.
"""
import math
from fractions import Fraction as F

def coefficients(a,p,q,al):
    c=q+al*a
    d=a*q+a*a*(al-1-p)
    k=al*d+al*q*a+al*al*a*a/2
    return c,d,k

def exact_algebra():
    cases=[(F(2),F(3,2),F(1),F(1)),(F(2),F(4),F(1),F(1)),
           (F(2),F(1),F(1),F(3,2)),(F(13,10),F(1,2),F(2,5),F(4,5))]
    for a,p,q,al in cases:
        c,d,k=coefficients(a,p,q,al)
        # Expansion z' = z - c z^2 + t z^3 + O(z^4)
        t=q*q+al*q*a+al*al*a*a/2-al*d
        assert c*c-t==k
        # Expansion y' = a z - a^2(1+p) z^2 + O(z^3)
        assert -a*a*(1+p) == d-a*c
        assert k==al*a*(2*q+a*(F(3,2)*al-1-p))
    assert coefficients(F(2),F(3,2),F(1),F(1))[2]==0
    return len(cases)

def integrate_case(a,p,q,al,y,z):
    c,d,k=[float(v) for v in coefficients(F(str(a)),F(str(p)),F(str(q)),F(str(al)))]
    out=[]
    for n in range(1,400001):
        yy=a*z*math.exp(-y)/(1+p*y)
        zz=z*math.exp(-al*y)/(1+q*z)
        y,z=yy,zz
        if n in (100000,400000):
            assert y>0 and z>0
            out.append((n,n*z,(y-a*z)/z**2,1/z-c*n-(k/c)*math.log(n)))
    assert abs(out[-1][1]-1/c)<0.0003
    assert abs(out[-1][2]-d)<0.005
    # The finite-part difference shrinks with additional steps.
    assert abs(out[-1][-1]-out[0][-1])<0.005
    return (c,d,k,out)

def main():
    count=exact_algebra()
    configs=[(2.,1.5,1.,1.,.3,.4),(2.,4.,1.,1.,.3,.4),
             (2.,1.,1.,1.5,.3,.4)]
    for params in configs:
        c,d,k,out=integrate_case(*params)
        print('CASE c=%g d=%g k=%g last=%s'%(c,d,k,out[-1]))
    print('VERIFY_OK exact_coefficient_cases=%d positive_zero_negative_log_signs=3 numerical_cases=3 horizons=2'%count)
if __name__=='__main__': main()
