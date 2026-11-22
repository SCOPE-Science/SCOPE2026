"""Standalone exact and numerical checks for a rational planar iteration.
Run: python3 verify.py (Python standard library only).
All infinite claims are proved in RESULT.md; these are diagnostic checks.
"""
from fractions import Fraction as Q
import math


def step(u, y):
    return u*y*y/(1+y*y), y+u


def exact_checks():
    checks=0
    for yn in range(1,6):
        for un in range(1,6):
            u,y=Q(un,4),Q(yn,3)
            for k in range(4):
                p=u*y
                U,Y=step(u,y)
                P=U*Y
                assert P-1==(p-1)*(1+p/(1+y*y))
                assert U-u==-u/(1+y*y)
                assert Y-y==u
                assert U>0 and Y>y
                assert (P>1)==(p>1) or p==1
                if p==1:
                    assert P==1 and U==1/Y
                u,y=U,Y
                checks+=6
    return checks


def numerical_checks():
    checks=0
    for y0 in (0.25,1.0,3.0):
        for p0 in (0.5,0.8,1.0,1.2,2.0):
            u,y=p0/y0,y0
            last_p=p0
            for _ in range(12000):
                U,Y=step(u,y)
                p=U*Y
                if u<1.e-12: break
                assert Y>y and 0<U<u
                if p0<1: assert 0<p<1 and p<last_p
                if p0==1: assert abs(p-1)<1.e-8
                if p0>1: assert p>1 and p>last_p
                u,y=U,Y
                last_p=p
            if p0<1:
                assert y<1e5 and u<1e-6
            elif p0==1:
                assert abs(y/math.sqrt(24000)-1)<0.03
                assert abs(u*y-1)<1e-8
            else:
                assert u>0 and y>0
            checks+=1
    # Critical logarithmic correction: renormalized square radius converges.
    y=1.0
    errors={}
    for n in range(1,50001):
        y+=1/y
        if n in (10000,20000,50000):
            errors[n]=y*y-2*n-0.5*math.log(n)
    assert abs(errors[50000]-errors[20000])<0.0003, errors
    checks+=1
    return checks

if __name__=='__main__':
    a=exact_checks();b=numerical_checks()
    print(f'PASS: {a} exact rational identities/comparisons; {b} numeric regime/asymptotic checks')
