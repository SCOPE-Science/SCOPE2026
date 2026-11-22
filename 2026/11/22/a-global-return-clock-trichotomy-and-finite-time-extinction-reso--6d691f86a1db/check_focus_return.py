"""Exact and floating regression for a mixed-trace homogeneous border-collision map.

The mathematical proof in RESULT.md is required for the all-parameter theorem.
"""
from fractions import Fraction as Q
from math import acos, ceil, sqrt, sin, pi, isclose
import random


def map_step(x, y, b, r, d):
    if x <= 0:
        return y - b*x, type(x)(0)
    return y + r*x, -d*x


def orbit(x, y, b, r, d, n):
    for _ in range(n):
        x, y = map_step(x, y, b, r, d)
    return x, y


def exact_case():
    # r=1, d=3 gives f_0=1, f_1=1, f_2=-2; first exit at j=2.
    r, d = Q(1), Q(3)
    for bnum in range(1, 81):
        b=Q(bnum,20)
        a,c=Q(2),Q(3)
        h=4 if b*a<c else 3
        M=b*(c-b*a) if b*a<c else b*a-c
        for unum in range(1,7):
            u=Q(unum,7)
            if b*a==c:
                assert orbit(u,Q(0),b,r,d,3)==(0,0)
            else:
                assert orbit(u,Q(0),b,r,d,h)==(M*u,0)
            for xnum in range(-5,6):
                for ynum in range(-5,6):
                    x,y=Q(xnum,4),Q(ynum,3)
                    # every state reaches either the positive axis or zero by step 5
                    for j in range(6):
                        if (x,y)==(0,0) or (x>0 and y==0):
                            break
                        x,y=map_step(x,y,b,r,d)
                    else:
                        raise AssertionError(('no-axis', b, xnum, ynum))
        if b*a==c:
            for xnum in range(-10,11):
                for ynum in range(-10,11):
                    assert orbit(Q(xnum,3),Q(ynum,5),b,r,d,9)==(0,0)
    assert orbit(Q(1),Q(0),Q(3,2),r,d,3)==(0,0)
    # Exact angular endpoint theta=pi/4: r=2, d=2, k=4, A=0, B=4.
    # Every positive ray has a five-step return multiplier 4*b; no b>0 kills it.
    for b in [Q(1,10), Q(1,4), Q(1), Q(7,5)]:
        for u in [Q(1,3), Q(11,7)]:
            assert orbit(u,Q(0),b,Q(2),Q(2),5)==(Q(4)*b*u,Q(0))
    assert orbit(Q(1),Q(0),Q(1,4),Q(2),Q(2),5)==(Q(1),Q(0))
    for b in [Q(1,2),Q(1),Q(2)]:
        x,y=orbit(Q(1),Q(0),b,r,d,4 if b<Q(3,2) else 3)
        assert (x,y)==(1,0)


def floating_case():
    rng=random.Random(44136)
    for _ in range(1400):
        r=rng.uniform(0.1,4)
        d=r*r/4+rng.uniform(.005,10)
        theta=acos(r/(2*sqrt(d)))
        k=ceil(pi/theta)
        a=-d**((k-1)/2)*sin(k*theta)/sin(theta)
        c=d**(k/2)*sin((k-1)*theta)/sin(theta)
        # avoid near-arithmetic resonance of sin(k*theta)
        if a < 1e-8 or c < 1e-8:continue
        b=rng.uniform(.04, 3*c/a)
        v=b*a-c
        if abs(v)<1e-8:continue
        h=k if v>0 else k+1
        M=v if v>0 else -b*v
        u=rng.uniform(.1,2)
        xf,yf=orbit(u,0.,b,r,d,h)
        assert isclose(xf,u*M,rel_tol=3e-6,abs_tol=2e-6), (k,h,a,c,v,xf,u*M)
        assert abs(yf)<1e-5*max(1,abs(xf))
        x,y=rng.uniform(-4,4),rng.uniform(-4,4)
        for j in range(k+3):
            if (x==0 and y==0) or (x>0 and y==0):break
            x,y=map_step(x,y,b,r,d)
        else:raise AssertionError(('no-axis',k))

if __name__=='__main__':
    exact_case()
    floating_case()
    print('MIXED_TRACE_RETURN_VERIFY_OK')
