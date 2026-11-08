#!/usr/bin/env python3
"""Reproducible certificates for priced diagonal pinning on complete graphs.

Requires Python 3.10+ standard library only. The theorem is proved in RESULT.md;
these tests check formulas and global-optimality certificates on finite inputs.
"""
from fractions import Fraction as F
from itertools import permutations
from math import sqrt, exp, fsum
from random import Random


def exact_case(prices, lam):
    """Exact construction when each listed price is a perfect-square integer."""
    n = len(prices)
    w = [int(sqrt(p)) for p in prices]
    assert all(x*x == p for x, p in zip(w, prices))
    bounds = [F(q) - F(sum(w[:q]), w[q]) for q in range(1, n)]
    q = 1 + sum(lam > x for x in bounds)
    t = sum(w[:q])
    s = F(n) - lam
    if q < n:
        assert 0 < lam < q
        d = [s * F(t, q - lam) / v if i < q else s for i, v in enumerate(w)]
    else:
        d = [F(t, v) for v in w]
    u = [di - s for di in d]
    eta = (s * F(t, q-lam))**2 if q < n else F(t*t)
    assert all(ui >= 0 for ui in u)
    assert sum(F(1, di) for di in d) == 1
    assert all(F(p) == eta/(di*di) for p, di in zip(prices[:q], d[:q]))
    if q < n:
        assert all(F(p) >= eta/(s*s) for p in prices[q:])
    b = sum(F(p)*ui for p, ui in zip(prices, u))
    if q < n:
        assert b == s*(F(t*t, q-lam)-sum(prices[:q]))
    else:
        assert b == t*t-s*sum(prices)
    return b, u, q, bounds


def numeric_design(prices, budget):
    n = len(prices)
    sorted_prices = sorted(float(p) for p in prices)
    roots = [sqrt(p) for p in sorted_prices]
    bounds = [q - fsum(roots[:q])/roots[q] for q in range(1, n)]

    def cost(lam, produce=False):
        q = 1 + sum(lam > bound for bound in bounds)
        T = fsum(roots[:q])
        s = n-lam
        if q < n:
            d = [s*T/((q-lam)*r) if i<q else s for i,r in enumerate(roots)]
            value = s*(T*T/(q-lam)-fsum(sorted_prices[:q]))
        else:
            d = [T/r for r in roots]
            value = T*T-s*fsum(sorted_prices)
        if produce:
            gains_sorted = [max(0.0, z-s) for z in d]
            pool = list(zip(sorted_prices, gains_sorted))
            # Preserve original ordering, including repeated prices.
            used=[False]*n
            gains=[]
            for p in prices:
                j=next(j for j,(v,g) in enumerate(pool) if not used[j] and abs(v-p)<1e-9*max(1,abs(p)))
                used[j]=True
                gains.append(pool[j][1])
            return value, gains, q
        return value
    lo=0.0; hi=n+budget/min(prices)+1
    for _ in range(90):
        mid=(lo+hi)/2
        if cost(mid)<budget:lo=mid
        else:hi=mid
    lam=(lo+hi)/2
    val,u,q=cost(lam, True)
    return lam,u,q,bounds


def smallest_eig_secular(gains):
    n=len(gains)
    # The smallest eigenvalue of diag(n+u_i)-11^T is the unique root
    # sum 1/(n+u_i-lambda)=1 below its smallest diagonal entry.
    hi=min(n+x for x in gains)
    lo=0.0
    for _ in range(85):
        mid=(lo+hi)/2
        val=fsum(1/(n+x-mid) for x in gains)
        if val<1:lo=mid
        else:hi=mid
    return (hi+lo)/2


def run():
    ncert=0; cb=0; trial=0
    rng=Random(7192015)
    for n in range(2,9):
        for t in range(1,11):
            w=sorted(rng.randint(1,9) for _ in range(n))
            p=[x*x for x in w]
            bounds=[F(q)-F(sum(w[:q]),w[q]) for q in range(1,n)]
            intervals=[F(0)]+bounds+[F(n+1)]
            for q in range(1,n+1):
                a,b=intervals[q-1:q+1]
                if a==b:continue
                lam=(a+b)/2
                B,u,selected,_=exact_case(p,lam)
                assert selected == q
                v,uu,qq,_=numeric_design(p,float(B))
                assert abs(v-float(lam))<1e-8
                assert abs(sum(x*y for x,y in zip(p,uu))-float(B))<2e-7*max(1.,float(B))
                ncert+=1
            # Exact continuity of optimal value and first derivative at each threshold.
            for q in range(1,n):
                lam=bounds[q-1]
                s=F(n)-lam
                T=sum(w[:q]); P=sum(p[:q]); Tnext=T+w[q]; Pnext=P+p[q]
                bq=s*(F(T*T,q-lam)-P)
                bnext=s*(F(Tnext*Tnext,q+1-lam)-Pnext)
                assert bq==bnext
                before=P+F((n-q)*T*T,(q-lam)**2)
                after=Pnext+F((n-q-1)*Tnext*Tnext,(q+1-lam)**2)
                assert before==after
                cb+=1
    for _ in range(240):
        n=rng.randint(2,9)
        prices=[exp(rng.uniform(-2.5,2.5)) for _ in range(n)]
        B=exp(rng.uniform(-3,4))
        lam, gains, _, _=numeric_design(prices,B)
        assert all(x >= -1e-10 for x in gains)
        assert abs(fsum(x*y for x,y in zip(prices,gains))-B)<2e-7*max(1,B)
        assert abs(smallest_eig_secular(gains)-lam)<1e-8
        for _ in range(65):
            masses=[rng.expovariate(1) for _ in range(n)]
            scale=B/fsum(masses)
            other=[scale*m/p for m,p in zip(masses, prices)]
            val=smallest_eig_secular(other)
            assert val<=lam+1e-8,(n,B,prices,lam,val)
            trial+=1
    print('PASS: exact active-set and rank-one certificates:',ncert)
    print('PASS: exact continuity and first-derivative transitions:',cb)
    print('PASS: independently evaluated feasible-budget comparisons:',trial)
    print('TOTAL_CHECKS:',ncert+cb+trial)

if __name__=='__main__':
    run()
