#!/usr/bin/env python3
"""Finite reproducibility checks for a three-amplitude signed-permutation cubature family.

This script uses only the Python standard library. It checks representative
instances, exact endpoint inequalities, and independent mixed-moment formulas.
Analytical arguments for every admissible dimension are in RESULT.md.
"""
from decimal import Decimal, localcontext
from fractions import Fraction
from math import isqrt

LO = Fraction(67, 125)
HI = Fraction(27, 50)


def terms(n, a):
    one = Fraction(1)
    two = Fraction(2)
    M2 = Fraction(3*n, n+2)
    M3 = Fraction(15*n*n, (n+2)*(n+4))
    S = 20 - 18*a
    Q = 20*M2 - 18*a*a
    P = (S*S - Q)/two
    Delta = 2*Q - S*S
    F = S**3 - 3*S*P - 20*M3 + 18*a**3
    return S, P, Delta, F


def check_n(n):
    assert n >= 100 and n % 20 == 0
    S0,P0,D0,F0=terms(n,LO)
    S1,P1,D1,F1=terms(n,HI)
    assert F0 < 0 < F1
    assert 0 < D0 < D1 < 4
    assert 0 < P1 < P0 and S1 > 10
    assert D0 == Fraction(16*(487*n-45901),3125*(n+2))
    assert P1 == Fraction(63659*n+277318,2500*(n+2))
    assert F0 == Fraction(-16*(12913*n*n+1624353*n+123478304),390625*(n+2)*(n+4))
    assert F1 == Fraction(24443*n*n-168342*n-31064456,6250*(n+2)*(n+4))
    with localcontext() as ctx:
        ctx.prec = 90
        two=Decimal(2)
        lo=Decimal(LO.numerator)/Decimal(LO.denominator)
        hi=Decimal(HI.numerator)/Decimal(HI.denominator)
        N=Decimal(n)
        M2=3*N/(N+2)
        M3=15*N*N/((N+2)*(N+4))
        def f(a):
            S=20-18*a
            Q=20*M2-18*a*a
            P=(S*S-Q)/2
            return S**3-3*S*P-20*M3+18*a**3
        for _ in range(290):
            mid=(lo+hi)/2
            if f(mid)>0:hi=mid
            else:lo=mid
        a=(lo+hi)/2
        S=20-18*a
        Q=20*M2-18*a*a
        D=2*Q-S*S
        b=(S-D.sqrt())/2
        c=(S+D.sqrt())/2
        assert Decimal(0)<a<b<c
        def close(x,y):return abs(x-y)<Decimal('1e-65')
        assert close((18*a+b+c)/20,1)
        assert close((18*a*a+b*b+c*c)/20,M2)
        assert close((18*a**3+b**3+c**3)/20,M3)
        # Independent coordinate-moment identities of orbit quadrature.
        p4=(18*a*a+b*b+c*c)/(20*N)
        p6=(18*a**3+b**3+c**3)/(20*N*N)
        assert close(p4,3/(N+2))
        assert close(p6,15/((N+2)*(N+4)))
        e6=p6/N
        e42=(p4-p6)/(N*(N-1))
        e222=(1-3*p4+2*p6)/(N*(N-1)*(N-2))
        target=N*(N+2)*(N+4)
        assert close(e6,15/target)
        assert close(e42,3/target)
        assert close(e222,1/target)
        return str(a)[:18],str(b)[:18],str(c)[:18]


def check_two_level_obstruction():
    # The proof reduces a hypothetical two-level orbit to n+1 | 18.
    eligible = [n for n in range(3,100000) if 18 % (n+1)==0]
    assert eligible==[5,8,17]
    for n in eligible:
        q2=Fraction(6*(n+2),n+1)
        assert isqrt(q2.numerator)**2 != q2.numerator or isqrt(q2.denominator)**2 != q2.denominator

if __name__=='__main__':
    check_two_level_obstruction()
    for n in [100,120,140,160,200,300,500,1000,2000]:
        print('n=',n,'a,b,c=',*check_n(n))
    print('ALL_CHECKS_PASS')
