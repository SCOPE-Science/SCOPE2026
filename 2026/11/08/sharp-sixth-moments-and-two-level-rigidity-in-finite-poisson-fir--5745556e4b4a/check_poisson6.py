#!/usr/bin/env python3
"""Exact and numerical checks of sixth moments for finite Poisson first chaos."""
from fractions import Fraction as Q
from math import sqrt
from random import Random
from sympy import symbols, diff, factor, simplify, together


def normalized_sixth(a, lam):
    z2 = sum(x*x for x in a)
    z3 = sum(x**3 for x in a)
    z4 = sum(x**4 for x in a)
    z6 = sum(x**6 for x in a)
    return 15 + 15*z4/(lam*z2*z2) + 10*z3*z3/(lam*z2**3) + z6/(lam*lam*z2**3)


def independent_cumulant_recurrence(a, lam):
    # Centered compound Poisson linear statistic; E X^r from the Bell recursion.
    kap = [0, 0] + [lam*sum(x**j for x in a) for j in range(2,7)]
    m = [Q(1)]
    from math import comb
    for n in range(1, 7):
        m.append(sum(comb(n-1, k-1)*kap[k]*m[n-k]
                     for k in range(1, n+1)))
    return m[6] / m[2]**3


def root_bisect(k, ell, lam):
    def p(t):
        return (1+20*lam*k)*t**3-(1+10*lam*k)*t*t+(1+10*lam*ell)*t-(1+20*lam*ell)
    a,b=1.,2.
    while p(b)<0:
        b*=2
    for _ in range(90):
        c=(a+b)/2
        if p(c)<0: a=c
        else: b=c
    return (a+b)/2


def exact_lower(n, lam):
    if n%2==0:
        return 15+15/(lam*n)+1/(lam*lam*n*n), None
    candidates=[]
    for k in range(1, n//2+1):
        ell=n-k
        t=root_bisect(k,ell,lam)
        a=[t]*k+[-1.]*ell
        candidates.append((normalized_sixth(a,lam),k,t))
    val,k,t=min(candidates)
    return val,(k,t)


def checks():
    k,ell,t,L=symbols('k ell t L',positive=True)
    d=k*t*t+ell
    F=(15*L*(k*t**4+ell)*d+10*L*(k*t**3-ell)**2+(k*t**6+ell))/d**3
    P=(1+20*L*k)*t**3-(1+10*L*k)*t**2+(1+10*L*ell)*t-(1+20*L*ell)
    assert simplify(together(diff(F,t)*d**4 - 6*k*ell*t*(t+1)*P))==0
    print('EXACT_ALL_PARAMETER_CUBIC_DERIVATIVE_IDENTITY_OK')

    cases=0
    for n in range(2,7):
        for lam in [Q(1,5),Q(2,3),Q(1),Q(7,2)]:
            rng=Random(100*n+int(10*lam))
            for _ in range(30):
                a=[Q(rng.randint(-5,5)) for i in range(n)]
                if not any(a):continue
                assert normalized_sixth(a,lam)==independent_cumulant_recurrence(a,lam)
                cases+=1
    print('INDEPENDENT_EXACT_BELL_RECURSION_AND_SIXTH_CUMULANTS_OK',cases)

    rng=Random(12425); diagnostics=0
    for n in range(2,15):
        for lam in [0.03,0.2,1.0,2.5,20.0]:
            low,_=exact_lower(n,lam)
            high=15+25/lam+1/lam**2
            # Witnesses for both bounds.
            assert abs(normalized_sixth([1]+[0]*(n-1),lam)-high)<1e-6
            if n%2==0:
                a=[1]*(n//2)+[-1]*(n//2)
            else:
                _,(kk,tt)=exact_lower(n,lam)
                a=[tt]*kk+[-1.]*(n-kk)
            assert abs(normalized_sixth(a,lam)-low)<1e-6*max(1,low)
            for _ in range(100):
                a=[rng.uniform(-1,1) for i in range(n)]
                val=normalized_sixth(a,lam)
                assert val>=low-1e-7*max(1,low)
                assert val<=high+1e-7*max(1,high)
                diagnostics+=1
    print('ENDPOINT_WITNESSES_AND_UNCERTIFIED_RANDOM_DIAGNOSTICS_OK', diagnostics)
    for n in [3,5,7,9]:
        for lam in [0.01,0.1,1,10,100]:
            low,opt=exact_lower(n,lam)
            base=15+15/(n*lam)+1/(lam*lam*n*n)
            assert low>base
            assert opt[1]>1
    print('ODD_DIMENSION_NONFLAT_EXTREMIZER_DIAGNOSTICS_OK')
    print('ALL_POISSON_SIXTH_MOMENT_CHECKS_PASSED')

if __name__=='__main__': checks()
