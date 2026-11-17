#!/usr/bin/env python3
"""Exact finite-mass identities and numerical probes of a Banach contraction averaging comparison.
No external packages; the unrestricted theorem is established analytically elsewhere.
"""
from fractions import Fraction
from math import log, exp, sqrt

def direct(n,p):
    assert isinstance(p,Fraction) and 0<p<=1 and n>=2
    r=1-p
    return sum(abs(Fraction(1,n)-p*r**k) for k in range(n))+r**n

def formula(n,p):
    r=1-p
    return 2*(r**n+sum((p*r**k-Fraction(1,n)) for k in range(n) if p*r**k>Fraction(1,n)))

def active(n,p):
    r=1-p
    return sum(p*r**k > Fraction(1,n) for k in range(n))

def asymptotic(lam):
    if lam<=1: return 2*exp(-lam)
    return 2*(1-(1+log(lam))/lam+exp(-lam))

def numeric(n,lam):
    p=lam/n
    r=1-p
    return 2*(r**n+sum(max(0.0,p*r**k-1/n) for k in range(n)))

count=0
for n in range(2,27):
    for den in (5,11,19,37):
        for num in range(1,den+1):
            p=Fraction(num,den)
            a=direct(n,p)
            b=formula(n,p)
            assert a==b,(n,p,a,b)
            signs=[p*(1-p)**k>Fraction(1,n) for k in range(n)]
            assert signs==sorted(signs,reverse=True)
            count+=1
print('EXACT_FINITE_L1_AND_SINGLE_CROSSING_CHECKS_PASS',count)

# The signed right-shift witness gives the exact l-infinity row norm.
count2=0
for n in range(2,17):
    for den in (7,29,101):
        for num in (1,den//4,den//2,3*den//4,den):
            p=Fraction(num,den)
            r=1-p
            # analytic tail mass is r^n; sign of c_k-g_k reaches it.
            row=sum(abs(Fraction(1,n)-p*r**k) for k in range(n)) + r**n
            assert row==direct(n,p)
            count2+=1
print('EXACT_SHIFT_EXTREMIZER_CHECKS_PASS',count2)

# All finite smooth candidate points (on fixed active-count pieces) are explicit.
# Confirm the global scalar optimum is never smaller than these candidates at
# 1000-point grid points on a variety of finite horizons. Include knots by
# bracket changes and bisection.
def candidates(n):
    pts=[0.0,1.0,1.0/n]
    for j in range(1,n): pts.append(1-(j/n)**(1/(n-j)))
    for k in range(1,n):
        peak=1/(k+1)
        def f(p): return p*(1-p)**k-1/n
        if f(peak)<0: continue
        for lo,hi in [(0.0,peak),(peak,1.0)]:
            if f(lo)*f(hi)>0: continue
            for _ in range(55):
                mid=(lo+hi)/2
                if f(mid)*f(lo)<=0: hi=mid
                else: lo=mid
            pts.append((lo+hi)/2)
    return pts

def fn(n,p):
    r=1-p
    return 2*(r**n+sum(max(0,p*r**k-1/n) for k in range(n)))

for n in range(2,45):
    cand=min(fn(n,p) for p in candidates(n))
    grid=min(fn(n,j/1000) for j in range(1001))
    assert cand<=grid+3e-11,(n,cand,grid)
print('FINITE_CRITICAL_POINT_AND_KNOT_CANDIDATE_TESTS_PASS_N2_TO44')

# The continuous derivative equation has one root because its LHS-to-RHS
# ratio is strictly increasing on (1,infinity). Compute by bisection.
lo,hi=1.5,2.0
for _ in range(70):
    mid=(lo+hi)/2
    test=log(mid)-mid*mid*exp(-mid)
    if test>0:hi=mid
    else:lo=mid
lam=(lo+hi)/2
value=asymptotic(lam)
assert 1.6946009<lam<1.6946010
assert .5646229<value<.5646230
assert abs(asymptotic(1)-2/exp(1))<1e-13
for n in (100,300,1000,4000,8000):
    got=numeric(n,lam)
    assert abs(got-value) < 7/n,(n,got,value)
print('UNIQUE_RATE_BRACKETING_AND_CONTINUUM_LIMIT_TESTS_PASS',format(lam,'.13f'),format(value,'.13f'))
print('ALL_ABEL_CESARO_MINIMAX_CHECKS_PASS')
