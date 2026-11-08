#!/usr/bin/env python3
"""Numerical cross-check of exact single-active-actuator diagonal Gramian theorem.
Uses standard Python only. Analytic infinite-horizon and uniqueness proof is in RESULT.md.
"""
import math
import random

rng = random.Random(341104)
checks = 0

def check(test, detail):
    global checks
    if not test:
        raise AssertionError(detail)
    checks += 1

def mass(lam, lo, hi):
    return (math.exp(-2*lam*lo)-math.exp(-2*lam*hi))/(2*lam)

def schedule(lams, horizon):
    n=len(lams)
    cap=mass(lams[0], 0, horizon)
    def ends_for_level(level):
        cuts=[0.0]
        for lam in lams:
            lhs=math.exp(-2*lam*cuts[-1])-2*lam*level
            if lhs <= math.exp(-2*lam*horizon):
                return False, cuts
            nxt=-math.log(lhs)/(2*lam)
            if nxt >= horizon:
                return False, cuts
            cuts.append(nxt)
        return True,cuts
    lo,hi=0.,cap
    for _ in range(100):
        mid=(lo+hi)/2
        ok,cuts=ends_for_level(mid)
        if ok: lo=mid
        else: hi=mid
    # Last cut will approach T; use boundary exact T.
    ok,cuts=ends_for_level(lo)
    if not ok:
        lo *= (1-1e-12)
        ok,cuts=ends_for_level(lo)
    assert ok
    cuts[-1]=horizon
    p=[1.0]
    for i in range(n-1):
        p.append(p[-1]*math.exp(-2*(lams[i]-lams[i+1])*cuts[i+1]))
    tot=sum(p);p=[x/tot for x in p]
    return cuts,p,min(mass(lams[i],cuts[i],cuts[i+1]) for i in range(n))

for n in range(2,7):
    for rep in range(12):
        lams=sorted([rng.uniform(0.20,4) for i in range(n)], reverse=True)
        horizon = rng.uniform(0.6,3)
        cuts, p, optimal = schedule(lams, horizon)
        check(all(cuts[i] < cuts[i+1] for i in range(n)), ('ordered cuts',n,rep))
        masses=[mass(lams[i],cuts[i],cuts[i+1]) for i in range(n)]
        check(max(masses)-min(masses)<2e-11, ('equal Gramian',n,rep, masses))
        for j in range(401):
            t=horizon*(j+0.5)/401
            i=next(idx for idx in range(n) if cuts[idx]<=t<=cuts[idx+1])
            gains=[p[a]*math.exp(-2*lams[a]*t) for a in range(n)]
            check(gains[i]>=max(gains)-1e-13,('dual envelope',n,rep,t,i,gains))
        # Randomized feasible alternatives, discretized using exact cell masses.
        for a in range(24):
            other=[0.0]*n
            for j in range(75):
                chosen=rng.randrange(n)
                other[chosen] += mass(lams[chosen],horizon*j/75,horizon*(j+1)/75)
            check(min(other)<=optimal+1e-10, ('duality sharp',n,rep,a))
print('VERIFY_OK',checks,'equalized entries, dual-envelope optimality, random alternative schedules')
