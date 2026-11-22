#!/usr/bin/env python3
"""Exact-arithmetic checks for a uniform two-unit-fraction underapproximation theorem.

Uses the standard-library Fraction type, integer floors, and full finite searches.
The proof of the unbounded case is in RESULT.md, not inferred from sampling.
"""
from fractions import Fraction


def candidate(u, s):
    q = 5*u - 4
    a = u + s
    d = 5*a - q
    b = max(a, q*a//d + 1)
    assert Fraction(1,a) + Fraction(1,b) < Fraction(5,q)
    return a,b


def exact_maximizers(u):
    q = 5*u - 4
    target = Fraction(5,q)
    best = Fraction(-1,1)
    winners = []
    for s in range(u):
        pair = candidate(u,s)
        a,b = pair
        value = Fraction(1,a) + Fraction(1,b)
        assert value < target
        if value > best:
            best,winners = value,[pair]
        elif value == best:
            winners.append(pair)
    return winners


def theorem_maximizers(u):
    m = u-1
    if m == 5:
        return [candidate(u,0),candidate(u,2)]
    if m in (6,16):
        return [candidate(u,2)]
    if m%9 in (2,3):
        return [candidate(u,1)]
    return [candidate(u,0)]


def check_algebra():
    # Independent direct evaluations of polynomial identities quoted in proof.
    for u in range(2,101):
        q = 5*u-4
        X0 = q*u
        X1 = q*(u+1)
        X2 = q*(u+2)
        assert 36*X0*(X0+4)-16*X1*(X1+9) == 4*q*(25*u**3-60*u**2+12*u-20)
        assert 12*X1*(X1+1)-9*X0*(X0+3) == 3*q*q*(u*u+8*u+3)
        assert 16*X1*(X1+1)-9*X0*(X0+4) == q*q*(7*u*u+32*u+12)
        assert 28*X0*(X0+4)-16*X2*(X2+2) == 4*(u-6)*(3*u+2)*q*q
        assert 14*X0*(X0+3)-12*X2*(X2+1) == 2*q*q*(u*u-24*u-21)
        t = 9 - (X1 % 9)
        assert (t==1) == (u%9 in (3,4))
        assert t in (1,4,7,9)
        for s in range(3,u):
            d=4+5*s
            Xs=q*(u+s)
            D = d*u*(q*u+4)-16*(u+s)*(q*(u+s)+d)
            rhs = (-(80*u+16)*s*s +
                   (25*u**3-180*u*u+68*u-64)*s -
                   60*u**3+48*u*u-48*u)
            assert D==rhs
            if u>=34:
                assert D>0
        if u>=34:
            assert 3*(5*u**3-164*u*u-188*u-112)>0
            assert 25*u**4-345*u**3+440*u*u-228*u+48>0


def main():
    check_algebra()
    n=500
    total=0
    for u in range(2,n+1):
        actual=exact_maximizers(u)
        expected=theorem_maximizers(u)
        assert actual==expected,(u,actual,expected)
        total += u
    exceptional={u-1:exact_maximizers(u) for u in range(2,34)
                 if (u-1 in (5,6,16) or (u-1)%9 in (2,3))}
    assert exceptional[5]==[(6,40),(8,15)]
    assert exceptional[6]==[(9,20)]
    assert exceptional[16]==[(19,110)]
    print('PASS: exact global two-term maximizers for 2<=u<=500')
    print('PASS: complete finite boundary 2<=u<=33')
    print('PASS: polynomial comparison identities and residue tables')
    print('PASS: exceptional optimizer cases',exceptional)
    print('Finite candidate evaluations:',sum(u for u in range(2,n+1)))

if __name__=='__main__':
    main()
