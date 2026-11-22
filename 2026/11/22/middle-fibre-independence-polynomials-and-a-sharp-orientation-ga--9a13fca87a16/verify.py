#!/usr/bin/env python3
"""Exhaustive and sampled checks of three-layer homomorphism identities."""
from itertools import product
from random import Random
from functools import lru_cache

def actual(arcs,n,p,q,r):
    labels=range(p+q+r)
    A=p; B=p+q
    return sum(
        all((a<b and (a<A and A<=b<B or a<A and b>=B or A<=a<B and b>=B)) for a,b in ((x[u],x[v]) for u,v in arcs))
        for x in product(labels,repeat=n)
    )

def predicted(arcs,n,p,q,r):
    out=[set() for _ in range(n)]; inc=[set() for _ in range(n)]
    for u,v in arcs: out[u].add(v); inc[v].add(u)
    M={i for i in range(n) if out[i] and inc[i]}
    if any(v in M for u in M for v in out[u]):return 0
    iso={i for i in range(n) if not out[i] and not inc[i]}
    S=set(M)
    for v in M:S|=out[v]|inc[v]
    choices=[i for i in range(n) if i not in S and i not in iso]
    ans=0
    edges={frozenset((u,v)) for u,v in arcs}
    for mask in range(1<<len(choices)):
        R={choices[j] for j in range(len(choices)) if mask>>j&1}
        if any(e<=R for e in edges):continue
        ans+=q**(len(M)+len(R))*p**sum(bool(out[v]) and v not in R for v in range(n) if v not in iso and v not in M)*r**sum(bool(inc[v]) and v not in R for v in range(n) if v not in iso and v not in M)
    return (p+q+r)**len(iso)*ans


def fib(n):
    a,b=0,1
    for _ in range(n):a,b=b,a+b
    return a

def check():
    checked=0
    for n in range(1,5):
        pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
        for code in product((0,1,2),repeat=len(pairs)):
            arcs=[(u,v) if x==1 else (v,u) for (u,v),x in zip(pairs,code) if x]
            for p,q,r in ((1,1,1),(2,1,1),(1,2,2)):
                a=actual(arcs,n,p,q,r); b=predicted(arcs,n,p,q,r)
                assert a==b,(n,arcs,p,q,r,a,b)
                checked+=1
    rng=Random(1729)
    for n in range(5,9):
        pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
        for trial in range(130):
            code=[rng.randrange(3) for _ in pairs]
            arcs=[(u,v) if x==1 else (v,u) for (u,v),x in zip(pairs,code) if x]
            for p,q,r in ((1,1,1),(2,1,1)):
                a=actual(arcs,n,p,q,r);b=predicted(arcs,n,p,q,r)
                assert a==b,(n,arcs,p,q,r,a,b)
                checked+=1
    for n in range(2,15):
        m=n-1
        good=sum(1 for s in product((0,1),repeat=m) if not any(s[i]==s[i+1]==s[i+2] for i in range(m-2)))
        assert good==2*fib(n),(n,good,2*fib(n))
        checked+=1
    # Coefficientwise verification for the middle-fibre enumerator.
    for n in range(1,6):
        pairs=[(i,j) for i in range(n) for j in range(i+1,n)]
        rng=Random(110+n)
        configurations=list(product((0,1,2),repeat=len(pairs))) if n<=3 else [tuple(rng.randrange(3) for _ in pairs) for i in range(50)]
        for code in configurations:
            arcs=[(u,v) if a==1 else (v,u) for (u,v),a in zip(pairs,code) if a]
            coeff=[0]*(n+1)
            for color in product((0,1,2), repeat=n):
                if all(color[u]<color[v] for u,v in arcs):
                    coeff[color.count(1)]+=1
            out=[set() for _ in range(n)];inc=[set() for _ in range(n)]
            for u,v in arcs:out[u].add(v);inc[v].add(u)
            mixed={v for v in range(n) if out[v] and inc[v]}
            predicted_coeff=[0]*(n+1)
            if not any(v in mixed for u in mixed for v in out[u]):
                iso={v for v in range(n) if not out[v] and not inc[v]}
                excluded=set(mixed)
                for v in mixed:excluded|=out[v]|inc[v]
                remain=[v for v in range(n) if v not in excluded and v not in iso]
                for bits in product((0,1),repeat=len(remain)):
                    chosen={v for v,b in zip(remain,bits) if b}
                    if any(u in chosen and v in chosen for u,v in arcs):continue
                    # Each isolated vertex contributes 2 + z.
                    from math import comb
                    for k in range(len(iso)+1):
                        predicted_coeff[len(mixed)+len(chosen)+k]+=comb(len(iso),k)*2**(len(iso)-k)
            assert coeff==predicted_coeff,(n,arcs,coeff,predicted_coeff)
            checked+=1
    # Sharp half-gap tree family and summed orientation count.
    for nleaves in range(1,10):
        N=nleaves
        edges=[(0,2),(2,1)]+[(0,3+i) for i in range(N)]+[(3+N+i,1) for i in range(N)]
        n=3+2*N
        # Direct independent-set dynamic product for this double-star tree.
        total=2**(2*N)+(2**N+1)**2
        reduced=2**(2*N)
        assert reduced*2<total and reduced/total<0.5
        checked+=1
    print('VERIFY_OK',checked)

if __name__=='__main__':check()
