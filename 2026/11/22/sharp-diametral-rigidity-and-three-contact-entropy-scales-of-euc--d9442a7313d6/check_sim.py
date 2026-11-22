#!/usr/bin/env python3
"""Reproduce exact metric identities for standard-coordinate SIM polytopes.
Run: python3 check_sim.py; only Python standard library is required.
Finite checks complement the separate all-dimensional proofs.
"""
from fractions import Fraction as F
from itertools import permutations
from math import factorial, comb, exp, log
from random import Random


def spectral(alpha):
    n = len(alpha)
    S, Q = [0], [0]
    for a in alpha:
        S.append(S[-1] + a)
        Q.append(Q[-1] + a*a)
    return S, Q


def enclosing_ball(alpha):
    n = len(alpha)
    S, Q = spectral(alpha)
    # Univariate strongly convex objective; its minimizer is either a
    # quadratic stationary point or a breakpoint between two ranks.
    candidates = {S[k]/n for k in range(n+1)}
    candidates.update(a/2 for a in alpha)
    def radius(c):
        return n*c*c + max(Q[k]-2*c*S[k] for k in range(n+1))
    c = min(candidates, key=radius)
    R2 = radius(c)
    active = tuple(k for k in range(n+1) if n*c*c+Q[k]-2*c*S[k] == R2)
    assert 1 <= len(active) <= 2
    if len(active) == 1:
        assert n*c == S[active[0]]
    else:
        j = active[1]
        assert active[0] == j-1
        assert c == alpha[j-1]/2
        assert S[j-1]/n <= c <= S[j]/n
    return c, R2, active


def all_vertices(alpha):
    n = len(alpha)
    return set(tuple(p) for k in range(n+1) for p in permutations(alpha[:k]+(0,)*(n-k)))


def diameter_sq(alpha):
    n = len(alpha)
    _, Q = spectral(alpha)
    return Q[n//2]+Q[(n+1)//2]


def run():
    # Brute pairs of actual distinct polytope vertices; exact rationals.
    cases=0; pairs=0
    for n in range(2,6):
        for t in (F(1,5), F(1,2), F(4,5)):
            a=tuple(t**j for j in range(n))
            verts=sorted(all_vertices(a))
            c,R2,active=enclosing_ball(a)
            assert all(sum((x-c)**2 for x in v) <= R2 for v in verts)
            touched = {v for v in verts if sum((x-c)**2 for x in v) == R2}
            assert len(touched) == sum(factorial(n)//factorial(n-k) for k in active)
            d2=diameter_sq(a)
            num=0
            for i,v in enumerate(verts):
                for w in verts[i+1:]:
                    pairs+=1
                    d=sum((x-y)**2 for x,y in zip(v,w))
                    assert d <= d2
                    if d == d2:
                        num+=1
                        assert set(i for i,x in enumerate(v) if x) .isdisjoint(set(i for i,y in enumerate(w) if y))
            assert num == factorial(n)//(2 if n%2==0 else 1),(n,t,num)
            cases+=1
    # Rank-pair rearrangement, independent of explicit vertex lists.
    rank_cases=0
    for n in range(2,31):
        for t in (F(1,3),F(2,5),F(3,4),F(9,10)):
            a=[t**j for j in range(n)]
            S,Q=spectral(a)
            d2=diameter_sq(a)
            for k in range(n+1):
                for l in range(n+1):
                    dot=sum(a[i-1]*a[n-i] for i in range(n-l+1,k+1)) if k+l>n else F(0)
                    assert Q[k]+Q[l]-2*dot <= d2
                    rank_cases+=1
            c,R2,active=enclosing_ball(a)
            assert all(Q[k]-2*c*S[k]+n*c*c<=R2 for k in range(n+1))
    # Strictly decreasing nongeometric weights: general diameter theorem.
    rng=Random(16433); generic_cases=0
    for n in range(2,13):
        for _ in range(45):
            vals=rng.sample(range(1,300),n)
            a=sorted((F(v,300) for v in vals),reverse=True)
            S,Q=spectral(a); d2=diameter_sq(a)
            for k in range(n+1):
                for l in range(n+1):
                    dot=sum(a[i-1]*a[n-i] for i in range(n-l+1,k+1)) if k+l>n else F(0)
                    assert Q[k]+Q[l]-2*dot<=d2
            generic_cases+=1
    # Large-scale checks: accelerated float candidate selection.
    def large_case(n, t):
        a=[t**j for j in range(n)]
        S,Q=spectral(a)
        best=(float('inf'),None)
        for k in range(n+1):
            lo=a[k]/2 if k<n else 0.0
            hi=a[k-1]/2 if k>0 else float('inf')
            c=max(lo,min(S[k]/n,hi))
            val=n*c*c+Q[k]-2*c*S[k]
            if val < best[0]: best=val,c
        c=best[1]
        vals=[Q[k]-2*c*S[k] for k in range(n+1)]
        idx=max(range(n+1),key=lambda k: vals[k])
        assert abs(n*c*c+vals[idx]-best[0]) < 1e-6
        return c,best[0],idx,diameter_sq(a)
    for lam in (0.4,1.5,4):
        for n in (2000,8000):
            c,R2,k,d2=large_case(n,exp(-lam/n))
            x=log(1+lam/2)/lam
            assert abs(c-1/(lam+2))<.005
            assert abs(k/n-x)<.004
            assert abs(R2/n-1/(2*(lam+2)))<.002
            assert abs(d2/n-(1-exp(-lam))/lam)<.002
    for n in (2500,8000):
        t=0.8
        c,R2,k,d2=large_case(n,t)
        assert abs(k-log(n*(1-t)/2)/(-log(t)))<3
        assert abs(R2-(1/(1-t*t)-1/(n*(1-t)**2)))<0.0001
    print('SIM_METRIC_PASS exact_vertex_cases=%d pairs=%d exact_rank_cases=%d generic_weight_cases=%d asymptotic_cases=8' % (cases,pairs,rank_cases,generic_cases))

if __name__=='__main__':run()
