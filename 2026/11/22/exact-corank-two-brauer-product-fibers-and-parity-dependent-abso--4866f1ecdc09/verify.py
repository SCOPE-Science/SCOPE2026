#!/usr/bin/env python3
"""Independent explicit matching-based checks for a rank-conditioned Brauer product law.
Run: python verify.py
"""
from collections import Counter
from itertools import combinations, permutations
from fractions import Fraction
from math import comb, factorial
from random import Random

def matchings(vertices):
    if not vertices:
        yield ()
        return
    a=vertices[0]
    for i in range(1,len(vertices)):
        b=vertices[i]
        for rest in matchings(vertices[1:i]+vertices[i+1:]):
            yield ((a,b),)+rest

def diagram(n, upper, lower, bij):
    pairs=list(upper)+[(a,n+b) for a,b in zip(sorted(set(range(n))-set(sum((list(p) for p in upper),[]))),bij)]+[(n+a,n+b) for a,b in lower]
    partner=[None]*(2*n)
    for x,y in pairs: partner[x]=y; partner[y]=x
    assert all(x is not None for x in partner)
    return tuple(partner)

def rank(d,n):
    return sum(d[i]>=n for i in range(n))

def rank_class(n,r):
    s=n-r
    for utop in combinations(range(n),r):
        left=tuple(x for x in range(n) if x not in utop)
        for ubot in combinations(range(n),r):
            right=tuple(x for x in range(n) if x not in ubot)
            for up in matchings(left):
                for low in matchings(right):
                    for bij in permutations(ubot):
                        yield diagram(n,up,low,bij)

def prod(x,y,n):
    # Three-row concatenation.  Every middle vertex has degree two.
    adj=[[] for _ in range(3*n)]
    def connect(u,v):adj[u].append(v);adj[v].append(u)
    for a in range(2*n):
        b=x[a]
        if a<b:connect(a,b)
    for a in range(2*n):
        b=y[a]
        if a<b:connect(a+n,b+n)
    exterior=list(range(n))+list(range(2*n,3*n))
    partner=[None]*(2*n)
    for start in exterior:
        ai=start if start<n else start-n
        if partner[ai] is not None:continue
        prev=-1; cur=start
        while True:
            nxt=next((v for v in adj[cur] if v!=prev),None)
            if nxt is None:break
            prev,cur=cur,nxt
        assert cur!=start and cur in exterior
        aj=cur if cur<n else cur-n
        partner[ai]=aj;partner[aj]=ai
    assert all(v is not None for v in partner)
    return tuple(partner)

def dsize(n,r):
    def odddf(t):
        a=1
        for j in range(t,0,-2):a*=j
        return a
    return comb(n,r)**2*odddf(n-r-1)**2*factorial(r)

def law(n,k):
    ranks=list(range(n-2,n%2-1,-2))
    pi={r:Fraction(0) for r in ranks};pi[n-2]=Fraction(1)
    for _ in range(k-1):
        nxt={r:Fraction(0) for r in ranks}
        for r,v in pi.items():
            p=Fraction(r*(r-1),n*(n-1))
            nxt[r]+=v*(1-p)
            if r>n%2:nxt[r-2]+=v*p
        pi=nxt
    return pi

def test(n, k):
    first=list(rank_class(n,n-2))
    print(f'n={n}, first-class-size={len(first)}')
    assert len(first)==dsize(n,n-2)
    distribution={d:1 for d in first}
    for j in range(2,k+1):
        distnew=Counter()
        for a,v in distribution.items():
            for b in first:
                distnew[prod(a,b,n)]+=v
        distribution=distnew
        predicted=law(n,j)
        ranks=Counter()
        for d,v in distribution.items(): ranks[rank(d,n)]+=v
        for r,p in predicted.items():
            assert ranks[r]==p*len(first)**j,(n,j,r,ranks[r],p)
            N=dsize(n,r)
            assert all(distribution.get(d,0)*N==ranks[r] for d in rank_class(n,r))
        print(f' k={j} rank-counts={dict(sorted(ranks.items()))}; distinct targets={len(distribution)}')

if __name__=='__main__':
    for n,k in [(3,4),(4,4),(5,2)]:test(n,k)
    # Exhaustive rank transitions for every hook and sample current diagrams at n=6.
    n=6
    choices=list(combinations(range(n),2))
    representatives={r:list(rank_class(n,r))[::max(1,dsize(n,r)//6)][:6] for r in (0,2,4)}
    # Right factors with any top hook are built by sampling the entire D_{n-2} class.
    hooks={}
    for y in rank_class(n,n-2):
        hook=tuple(i for i in range(n) if y[i]<n)
        # Exactly two upper vertices form the sole horizontal hook.
        hooks.setdefault(hook,y)
        if len(hooks)==len(choices):break
    assert len(hooks)==len(choices)
    for r,reps in representatives.items():
        for x in reps:
            through={i-n for i in range(n,2*n) if x[i]<n}
            for hook,y in hooks.items():
                wanted=r-2 if set(hook)<=through else r
                assert rank(prod(x,y,n),n)==wanted
    print('n=6 exact hook-intersection transition verified for ranks 0,2,4')
    for n in range(3,20):
        for k in (1,2,3,5,10,25):
            p=law(n,k)
            assert sum(p.values())==1
    print('ALL BRAUER PRODUCT AND FINITE MARKOV CHECKS PASS')
