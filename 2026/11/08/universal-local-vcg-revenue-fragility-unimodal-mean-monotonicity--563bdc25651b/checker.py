#!/usr/bin/env python3
"""Reproduce the 2-by-2 VCG sensitivity identities.

Dependencies: Python 3.10+, SymPy (symbolic integration). No network access.
"""
from fractions import Fraction
from itertools import product
import random
import sympy as sp


def vcg_revenue(a, b, c, d):
    """Independent assignment-and-externality implementation; nonnegative values."""
    vals = ((a,b),(c,d))
    # 0, 1 = object labels; -1 = bidder receives no item.
    options = ((-1,-1),(-1,0),(-1,1),(0,-1),(1,-1),(0,1),(1,0))
    def val(i,j): return 0 if j == -1 else vals[i][j]
    choice = max(options, key=lambda p: (val(0,p[0])+val(1,p[1]),p[0]!=-1,p[1]!=-1))
    value0, value1 = val(0,choice[0]), val(1,choice[1])
    W = value0 + value1
    pay0 = max(c,d) - value1
    pay1 = max(a,b) - value0
    if any(isinstance(x,float) for x in (a,b,c,d)):
        assert pay0 > -1e-10 and pay1 > -1e-10
        assert abs(pay0 + pay1 - (max(a,b)+max(c,d)-W)) < 1e-10
    else:
        assert pay0 >= 0 and pay1 >= 0
        assert pay0 + pay1 == max(a,b)+max(c,d)-W
    return pay0+pay1


def difference_formula(a,b,c,d):
    S=a-b; T=c-d
    if S*T <= 0:
        return 0
    return min(abs(S),abs(T))


def exact_grid_checks():
    # Exhaustive finite-grid check for all 2-by-2 valuation matrices with
    # entries in {0,1,2,3,4,5}, plus fractional shocks to fourth entry.
    shifts = [Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(1),Fraction(2),Fraction(5)]
    cases = 0
    for v in product(range(6), repeat=4):
        a,b,c,d = map(Fraction,v)
        r0 = vcg_revenue(a,b,c,d)
        assert r0 == difference_formula(a,b,c,d)
        S, T = a-b,c-d
        for t in shifts:
            r1 = vcg_revenue(a,b,c,d+t)
            assert r1 == difference_formula(a,b,c,d+t)
            # For t>0, revenue can decrease only in the same-item-1 quadrant.
            if r1 < r0:
                assert t > 0 and S>0 and T>0 and T-S < t
            # If S>0 and T>0, the strict inequality exactly characterizes loss.
            if S>0 and T>0 and t>0:
                assert (r1 < r0) == (T-S < t)
            cases += 1
    return cases


def symbolic_checks():
    t,s,u=sp.symbols('t s u', real=True)
    Q = sp.Rational(1,4)-sp.integrate((1-s)*sp.integrate(1-u,(u,s+t,1)),(s,0,1-t))
    Qexpected=(t**4-6*t**2+8*t+3)/24
    assert sp.simplify(Q-Qexpected)==0

    Lprime=sp.integrate((1-u)*sp.integrate(1-s,(s,u-t,1)),(u,t,1))
    Lexpr=t*(t**4-10*t+15)/120
    assert sp.simplify(Lprime-sp.diff(Lexpr,t))==0
    assert sp.simplify(Lexpr.subs(t,1)-sp.Rational(1,20))==0

    Fpos=lambda z:sp.Rational(1,2)+z-z*z/2
    Fneg=lambda z:sp.Rational(1,2)+z+z*z/2
    Gprime0=sp.integrate((1-u)*(Fpos(t)-Fpos(t-u)),(u,0,t)) + sp.integrate((1-u)*(Fpos(t)-Fneg(t-u)),(u,t,1))
    Gexpr=t*(-2*t**4+10*t**3-20*t**2+10*t+15)/120
    assert sp.simplify(Gprime0-sp.diff(Gexpr,t))==0
    assert sp.simplify(Gexpr.subs(t,1)-sp.Rational(13,120))==0
    Gprime1=sp.integrate((1-u)*(1-Fpos(t-u)),(u,t-1,1))
    Gexpr1=(14-(2-t)**5)/120
    assert sp.simplify(Gprime1-sp.diff(Gexpr1,t))==0
    assert sp.simplify(Gexpr1.subs(t,1)-sp.Rational(13,120))==0
    assert sp.simplify(Gexpr1.subs(t,2)-sp.Rational(7,60))==0
    N0=t*t*(20-20*t+10*t*t-3*t**3)/120
    N1=(8-(2-t)**5)/120
    assert sp.simplify(Gexpr-Lexpr-N0)==0
    assert sp.simplify(Gexpr1-sp.Rational(1,20)-N1)==0
    assert sp.simplify(N0.subs(t,1)-N1.subs(t,1))==0
    return 9


def numerical_sanity():
    rng=random.Random(431031)
    shifts=(0.25,0.5,1.0,1.5,2.5)
    n=140000
    counts=[0]*len(shifts); totals=[0.0]*len(shifts)
    for _ in range(n):
        a,b,c,d=(rng.random() for j in range(4))
        r0=difference_formula(a,b,c,d)
        for i,delta in enumerate(shifts):
            r1=difference_formula(a,b,c,d+delta)
            counts[i]+=(r1<r0)
            totals[i]+=(r1-r0)
    for i,delta in enumerate(shifts):
        q=(delta**4-6*delta*delta+8*delta+3)/24 if delta <=1 else 0.25
        net=(delta**2*(20-20*delta+10*delta**2-3*delta**3)/120 if delta <=1 else ((8-(2-delta)**5)/120 if delta<=2 else 1/15))
        assert abs(counts[i]/n-q)<0.009, (delta,counts[i]/n,q)
        assert abs(totals[i]/n-net)<0.008, (delta,totals[i]/n,net)
    return n*len(shifts)


def bimodal_boundary_check():
    # Exact ideal two-peak model plus bounded perturbation argument.
    exact0 = sum((Fraction(difference_formula(S,0,T,0)) for S,T in product((-1,1),repeat=2)),Fraction(0))/4
    exact1 = sum((Fraction(difference_formula(S,0,T-1,0)) for S,T in product((-1,1),repeat=2)),Fraction(0))/4
    assert exact0 == Fraction(1,2) and exact1 == Fraction(1,4)
    assert exact1-exact0+4*Fraction(1,100) == -Fraction(21,100)
    # Independent full-payoff check with smooth atomless gap noise.
    rng=random.Random(431032)
    n=120000; z=0.0
    for _ in range(n):
        S=rng.choice((-1,1))+rng.uniform(-.01,.01)
        T=rng.choice((-1,1))+rng.uniform(-.01,.01)
        a,b,c,d=1+S/2,1-S/2,1+T/2,1-T/2
        z+=vcg_revenue(a,b,c,d+1)-vcg_revenue(a,b,c,d)
    assert z/n < -0.21, z/n
    return n


if __name__ == '__main__':
    g=exact_grid_checks()
    symbolic_checks()
    m=numerical_sanity()
    k=bimodal_boundary_check()
    print('PASS exact externality/formula grid:',g,'(6^4 valuation grids times 6 shocks)')
    print('PASS 9 symbolic identities (integration and polynomial checks)')
    print('PASS Monte Carlo sanity comparisons:',m,'(5 shock sizes, 140000 markets)')
    print('PASS atomless bimodal expectation-reversal check:',k,'markets and exact ideal comparison')
