#!/usr/bin/env python3
"""Independent finite-field construction for flags and all shattering traces.
Science-only verifier: no external input, dependencies or service access.
"""
from itertools import product,combinations
from math import comb
from functools import lru_cache

def span_add(u,vec,p):
    # Both u and vec are tuples in F_p^n; enum the span U+<vec>.
    return frozenset(tuple((x[j]+a*vec[j])%p for j in range(len(vec)))
        for x in u for a in range(p))

def subspaces(p,n):
    zero=(0,)*n
    vecs=list(product(range(p),repeat=n))
    bydim=[{frozenset([zero])}]
    for d in range(n):
        nxt=set()
        for u in bydim[-1]:
            for vec in vecs:
                if vec not in u:nxt.add(span_add(u,vec,p))
        assert all(len(x)==p**(d+1) for x in nxt)
        bydim.append(nxt)
    assert len(bydim[-1])==1
    return bydim

@lru_cache(None)
def gb(n,k,q):
    if k<0 or k>n:return 0
    if k in (0,n):return 1
    return gb(n-1,k-1,q)+q**k*gb(n-1,k,q)

def comp(n,m):
    if m==1:
        yield (n,); return
    for first in range(1,n-m+2):
        for tail in comp(n-first,m-1):yield (first,)+tail

def expected(n,k,q):
    ans=0
    for parts in comp(n,k+1):
        t=n; ways=1
        for block in parts:
            ways*=gb(t,block,q)
            t-=block
        ans+=ways
    return ans

def test(p,n,max_k):
    layers=subspaces(p,n)
    arr=[u for dim in range(1,n) for u in sorted(layers[dim],key=lambda v:sorted(v))]
    mp={u:i for i,u in enumerate(arr)}
    flags=[]
    def rec(u,d,mask):
        if d==n:
            flags.append(mask);return
        for v in layers[d+1]:
            if u<=v:
                rec(v,d+1,mask | ((1<<mp[v]) if d+1<n else 0))
    rec(next(iter(layers[0])),0,0)
    assert len(flags)==expected(n,n-1,p)
    counts=[]
    for k in range(max_k+1):
        n_shattered=0
        for idx in combinations(range(len(arr)),k):
            traces=set()
            for f in flags:
                t=sum(1<<j for j,i in enumerate(idx) if f>>i&1)
                traces.add(t)
                if len(traces)==1<<k:break
            # Dimension nondecreasing is already forced by sorting, but inclusion must hold.
            chain=all(arr[idx[j]]<arr[idx[j+1]] for j in range(k-1))
            assert (len(traces)==1<<k)==chain, (p,n,k,idx,'trace/chain mismatch')
            if chain:n_shattered+=1
        counts.append(n_shattered)
    expected_values=[expected(n,k,p) for k in range(max_k+1)]
    assert counts==expected_values,(p,n,counts,expected_values)
    print(f'FLAG_TRACES_PASS prime={p} dimension={n} subspaces={sum(len(layer) for layer in layers)} flags={len(flags)} max_support={max_k} support_tests={sum(comb(len(arr),k) for k in range(max_k+1))} counts={counts}',flush=True)

for p,n,k in [(2,2,1),(3,2,1),(2,3,2),(3,3,2),(5,3,2),(2,4,3)]:test(p,n,k)
print('ALL_PROJECTIVE_FLAG_SHATTERING_CHECKS_PASS')
