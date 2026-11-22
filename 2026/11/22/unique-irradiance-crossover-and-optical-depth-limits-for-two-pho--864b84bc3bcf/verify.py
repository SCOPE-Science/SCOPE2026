#!/usr/bin/env python3
"""Independent numerical and rational corroboration for a two-stratum photosynthetic sorting theorem.

Only Python standard-library dependencies. The mathematical proof is in RESULT.md;
tests are finite corroboration, not an infinite certificate.
"""
import math
import random
from fractions import Fraction

TOTAL = 0

def check(condition, message):
    global TOTAL
    TOTAL += 1
    if not condition:
        raise AssertionError(f"assertion {TOTAL}: {message}")


def g(t, a, b):
    return math.exp(-b*t) * (-math.expm1(-(a-b)*t))


def interval_g(s, left, right, a, b):
    # ∫_{s*left}^{s*right} (e^{-bt}-e^{-at}) dt
    return ((math.exp(-b*s*left)-math.exp(-b*s*right))/b
           -(math.exp(-a*s*left)-math.exp(-a*s*right))/a)


def difference(s, q, a, b):
    return interval_g(s,q*q,q,a,b)-interval_g(s,q,1.,a,b)


def ratio(s,q,a,b):
    upper=interval_g(s,q,1.,a,b)
    lower=interval_g(s,q*q,q,a,b)
    return lower/upper


def production(s,q,a,b,a_on_top):
    # P=∫ response(s exp(-z)) dz, exact primitive; q=exp(-stratum thickness)
    top=a if a_on_top else b
    bottom=b if a_on_top else a
    return ((math.exp(-top*q*s)-math.exp(-top*s))/top
            +(math.exp(-bottom*q*q*s)-math.exp(-bottom*q*s))/bottom)


def crossing(q,a,b):
    left=0.05/max(a,b)
    while difference(left,q,a,b)>=0:
        left/=2
    right=1/max(b*q*q,1.e-12)
    while difference(right,q,a,b)<=0:
        right*=1.25
    for _ in range(100):
        mid=(left+right)/2
        if difference(mid,q,a,b)>0: right=mid
        else:left=mid
    return (left+right)/2


def elasticity(s,a,b):
    c=a-b
    y=c*s
    return -b*s+y/math.expm1(y)


def median(a,b):
    total=1/b-1/a
    def partial(t):
        return (1-math.exp(-b*t))/b-(1-math.exp(-a*t))/a
    lo,hi=0.,10./b
    for _ in range(80):
        mi=(lo+hi)/2
        if partial(mi)<total/2:lo=mi
        else:hi=mi
    return (lo+hi)/2


def thin_root(a,b):
    l,r=1e-8,10./b
    for _ in range(85):
        m=(l+r)/2
        if elasticity(m,a,b)>-1: l=m
        else:r=m
    return (l+r)/2

# Exact-rational boundary witness (at a=2, b=1, q=1/2).
def rational_gap(z):
    return z-Fraction(5,2)*z*z+2*z**4-Fraction(1,2)*z**8
check(rational_gap(Fraction(1,2)) == -Fraction(1,512), 'exact low-light witness')
check(rational_gap(Fraction(1,3)) == Fraction(526,6561), 'exact high-light witness')

root=crossing(.5,2.,1.)
check(abs(root-2.8020540391874182)<1e-8,'reference critical irradiance')
check(difference(4*math.log(2),.5,2,1)<0,'low-light reversal sign')
check(difference(4*math.log(3),.5,2,1)>0,'high-light reversal sign')
check(abs(production(5,.5,2,1,True)-.2077660717709528)<1e-12,'high light productivity AB')
check(abs(production(5,.5,2,1,False)-.11302057743722)<1e-12,'high light productivity BA')

rng=random.Random(173104)
# Different parameter scales and optical depths; independent sign checks around each numerical crossover.
for trial in range(600):
    b=10**rng.uniform(-.6,.5)
    a=b*(1+rng.uniform(.15,3.0))
    q=rng.uniform(.22,.85)
    s_star=crossing(q,a,b)
    check(s_star>0 and math.isfinite(s_star), f'finite crossover {trial}')
    check(difference(.72*s_star,q,a,b)<0, f'before crossing {trial}')
    check(difference(1.35*s_star,q,a,b)>0, f'after crossing {trial}')
    check(abs(difference(s_star,q,a,b))<1e-9/b,f'at crossover {trial}')
    # Exact independent P-AB difference from separately integrated responses.
    for factor in [.55,.9,1.,1.2,1.8]:
        s=factor*s_star
        d=difference(s,q,a,b)
        p=production(s,q,a,b,True)-production(s,q,a,b,False)
        check(abs(d-p)<3e-10/b, f'production identity {trial} {factor}')
    # R(s) increasing over the tested finite bracket.
    probes=[.60*s_star,.85*s_star,s_star,1.2*s_star,1.6*s_star]
    rvals=[ratio(s,q,a,b) for s in probes]
    for one,two in zip(rvals,rvals[1:]):
        check(two>one, f'strict integrated ratio {trial}')

# Qualitative thin-canopy asymptotic with independent elasticity-root calculation.
s0=thin_root(2.,1.)
errors=[]
for L in [.2,.1,.05,.025]:
    s=crossing(math.exp(-L),2.,1.)
    errors.append(abs(s-s0))
check(all(errors[i+1]<errors[i] for i in range(len(errors)-1)), 'thin-layer limiting convergence')
check(errors[-1]<.05,'thin-layer terminal accuracy')

# Thick-canopy asymptotic: q*s_c -> unique g-median, independent primitive.
m=median(2.,1.)
errors=[]
for L in [2.,3.,4.,5.]:
    q=math.exp(-L)
    sc=crossing(q,2.,1.)
    errors.append(abs(q*sc-m))
check(all(errors[i+1]<errors[i] for i in range(len(errors)-1)), 'thick-layer limiting convergence')
check(errors[-1]<.05,'thick-layer terminal accuracy')

# Check critical elasticity is strictly decreasing on broad positive ranges.
for a,b in [(2,1), (5,1), (1.5,.25),(7,3)]:
    vals=[elasticity(s,a,b) for s in [.01,.1,.2,.5,1.,2.,4.,8.]]
    for x,y in zip(vals,vals[1:]):
        check(x>y, 'elasticity monotonic')

print(f'PASS: {TOTAL:,} deterministic assertions; one exact rational witness on both sides;')
print(f'  example critical surface light: {root:.15f};')
print(f'  thin-limit light: {s0:.12f}; thick-limit normalized surface light: {m:.12f};')
print('  finite numerical tests corroborate, but do not certify, the analytic theorem.')
