#!/usr/bin/env python3
"""Exact rational spot checks for a two-disk covering theorem on rectangular flat tori.

The analytic proof supplies the universal covering and optimization arguments.
Finite point tests are corroboration, never an infinite proof.
"""
from fractions import Fraction as F


def circ_dist(x, c, period):
    z = (x-c) % period
    return min(z, period-z)


def dsq(x, y, cx, cy, a, b):
    return circ_dist(x, cx, a)**2 + circ_dist(y, cy, b)**2


def check(a0, b0, N=32):
    a, b = F(a0), F(b0)
    assert a >= b > 0
    R=(a*a+b*b)/(4*a)
    h=(a*a-b*b)/(4*a)
    Rsq=R*R
    assert R>=b/2 and R<=a/2
    assert h>=0 and h+R==a/2
    assert Rsq-h*h==b*b/4
    assert Rsq-b*b/4==h*h
    # Four farthest points of the proposed two-site configuration (two at a=b).
    contacts={(R%a,F(0)),((-R)%a,F(0)),(h%a,b/2),((-h)%a,b/2)}
    assert len(contacts)==(2 if a==b else 4)
    for x,y in contacts:
        assert dsq(x,y,0,0,a,b)==Rsq
        assert dsq(x,y,a/2,b/2,a,b)==Rsq
    checked=0
    # Exhaustive exact rational grid evaluation, not an exhaustive test of the torus.
    for i in range(N+1):
        for j in range(N+1):
            x=a*F(i,N)
            y=b*F(j,N)
            v=min(dsq(x,y,0,0,a,b),dsq(x,y,a/2,b/2,a,b))
            assert v<=Rsq, (a,b,x,y,v,Rsq)
            checked+=1
    return len(contacts),checked,R,Rsq


def main():
    cases=[(1,1),(5,4),(3,2),(2,1),(5,2),(3,1),(10,1),(15,2),(100,1)]
    total=0
    for a,b in cases:
        n,checks,R,Rsq=check(a,b)
        total+=checks
        print(f'a={a}, b={b}: R={R}, R^2={Rsq}, contacts={n}, grid={checks} exact cells')
    # The shape-density derivative has numerator (t^2-3)(t^2+1),
    # hence it has exactly one root t>=1, at sqrt(3).
    for t in [F(1), F(5,4), F(3,2), F(2), F(10)]:
        numer=t**4-2*t**2-3
        assert numer == (t*t-3)*(t*t+1)
    print(f'PASS: {total} exact grid evaluations, contact identities and density factorization')


if __name__=='__main__':
    main()
