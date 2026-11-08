#!/usr/bin/env python3
"""Finite checks for the stationary splitting-law convex-order theorem.

Only the analytic argument proves the infinite-depth assertion. This program
independently checks finite-depth distributions and moment identities.
"""
from collections import defaultdict
from fractions import Fraction as F
from functools import lru_cache
from math import exp, isclose

BAL = [(F(1, 2), F(1))]
MID = [(F(1, 2), F(1, 2)), (F(1, 4), F(1, 4)), (F(3, 4), F(1, 4))]
WIDE = [(F(1, 4), F(1, 2)), (F(3, 4), F(1, 2))]
CASES = [('balanced', BAL), ('mixture', MID), ('asymmetric', WIDE)]

def transform(pmf, nu):
    out = defaultdict(F)
    for x, px in pmf.items():
        for y, py in pmf.items():
            out[x+y] += px * py / 3
        for z, pz in nu:
            out[z*x] += F(2, 3) * px * pz
    return {x: p for x, p in out.items() if p}

def moment(pmf, k):
    return sum((p*x**k for x,p in pmf.items()), F(0))

def stoploss(pmf, t):
    return sum((p*(x-t) for x,p in pmf.items() if x>t), F(0))

def second_moment_limit(nu):
    ez2 = sum((p*z*z for z,p in nu), F(0))
    return F(2)/(1-2*ez2)

def third_moment_limit(nu):
    ez3 = sum((p*z*z*z for z,p in nu), F(0))
    return F(6)*second_moment_limit(nu)/(1-2*ez3)

laws = [[{F(1):F(1)}] for _ in CASES]
checks = 0
for d in range(4):
    for i, (_, nu) in enumerate(CASES):
        P = laws[i][-1]
        assert sum(P.values()) == 1
        assert moment(P, 1) == 1
        ez2=sum((p*z*z for z,p in nu), F(0))
        expected=second_moment_limit(nu)+(1-second_moment_limit(nu))*((2+2*ez2)/3)**d
        assert moment(P,2)==expected
        checks+=3
        if d<3:
            laws[i].append(transform(P,nu))
    # For equal means, comparing all support knots proves finite-support convex order.
    for a,b in ((0,1),(1,2),(0,2)):
        Pa, Pb = laws[a][-1], laws[b][-1]
        for t in sorted(set(Pa)|set(Pb)):
            assert stoploss(Pa,t)<=stoploss(Pb,t)
            checks+=1

for name,nu in CASES:
    m2=second_moment_limit(nu)
    m3=third_moment_limit(nu)
    assert m3==2*m2*m2
    checks+=1
assert second_moment_limit(BAL)==4
assert second_moment_limit(WIDE)==F(16,3)
assert second_moment_limit(MID)==F(32,7)
checks+=3

@lru_cache(None)
def approx(n, s, case):
    if n == 0:
        return exp(-s)
    nu = CASES[case][1]
    f = approx(n-1,s,case)
    return (f*f+2*sum((float(p)*approx(n-1,float(z)*s,case) for z,p in nu)))/3

for s in (0.05,0.2,0.7,1.0,2.0,4.0):
    vals=[approx(7,s,i) for i in range(3)]
    assert vals[0] < vals[1] < vals[2]
    for i in range(3):
        P=laws[i][2]
        # independent exact-PMF vs functional iteration at depth two
        direct=sum(float(p)*exp(-s*float(x)) for x,p in P.items())
        assert isclose(direct,approx(2,s,i),abs_tol=1e-13)
    checks+=5
print(f'PASS: {checks} finite exact-rational and numerical checks; analytical proof needed for limits')
for name,nu in CASES:
    print(f'{name:11s} E[Y^2]={float(second_moment_limit(nu)):.9g} E[Y^3]={float(third_moment_limit(nu)):.9g} L_7(1)={approx(7,1.0,CASES.index((name,nu))):.9g}')
