"""Independent finite tests for pair-comparison shattering of linear extensions.

Run: python3 verify_poset_comparisons.py
The exhaustive theorem is proved separately; finite checks do not prove it.
"""
from itertools import combinations, permutations, product
import random

def poset_closure(n, relations):
    reach = [0]*n
    for i,j in relations:
        reach[i] |= 1<<j
    for k in range(n):
        for i in range(n):
            if reach[i] & (1<<k):
                reach[i] |= reach[k]
    if any(reach[i] & (1<<i) for i in range(n)):
        return None
    return tuple(reach)

def all_posets(n):
    pairs = list(combinations(range(n),2))
    out = set()
    for choices in product(range(3), repeat=len(pairs)):
        rel = []
        for (i,j), choice in zip(pairs, choices):
            if choice==1: rel.append((i,j))
            if choice==2: rel.append((j,i))
        c = poset_closure(n, rel)
        if c is not None: out.add(c)
    return sorted(out)

def criterion(n, p, S):
    par=list(range(n))
    def root(v):
        while par[v]!=v: v=par[v]
        return v
    for i,j in S:
        a,b=root(i),root(j)
        if a==b: return False
        par[a]=b
    comps=sorted(set(root(i) for i in range(n)))
    index={x:k for k,x in enumerate(comps)}
    ci=[index[root(v)] for v in range(n)]
    edges=[]
    for a in range(n):
        for b in range(n):
            if p[a]>>b & 1:
                if ci[a]==ci[b]: return False
                edges.append((ci[a],ci[b]))
    return poset_closure(len(comps), edges) is not None

def direct(n, p, S):
    traces=set()
    for perm in permutations(range(n)):
        loc={v:k for k,v in enumerate(perm)}
        if any(loc[a]>loc[b] for a in range(n) for b in range(n) if p[a]>>b&1):
            continue
        traces.add(sum((loc[a]<loc[b])<<i for i,(a,b) in enumerate(S)))
    return len(traces)==1<<len(S)

def height(n,p):
    d=[1]*n
    for z in range(n):
        for i in range(n):
            d[i]=max([d[i]]+[d[j]+1 for j in range(n) if p[j]>>i&1])
    return max(d,default=0)

def check(n,ps,exhaustive=True,seed=7):
    rng=random.Random(seed+n)
    pairs=list(combinations(range(n),2))
    all_s=[tuple(e for i,e in enumerate(pairs) if mask>>i & 1)
           for mask in range(1<<len(pairs))]
    tested=0
    for p in ps:
        supports=all_s if exhaustive else rng.sample(all_s,min(240,len(all_s)))
        maximal=0
        for s in supports:
            a=criterion(n,p,s); b=direct(n,p,s)
            assert a==b, (n,p,s,a,b)
            tested+=1
            if b: maximal=max(maximal,len(s))
        if exhaustive: assert maximal==n-height(n,p), (n,p,maximal,n-height(n,p))
    return tested

def main():
    total=0
    counts={}
    for n in range(1,5):
        ps=all_posets(n)
        counts[n]=len(ps)
        total+=check(n,ps)
    assert counts=={1:1,2:3,3:19,4:219}, counts
    ps5=all_posets(5)
    assert len(ps5)==4231
    rng=random.Random(3025)
    sample=rng.sample(ps5,75)
    total+=check(5,sample,True)
    assert not criterion(4,poset_closure(4,[(0,1),(3,2)]),[(0,2),(1,3)])
    print(f'POSET_COMPARISON_SHATTER_PASS all_posets_n_le_4={sum(counts.values())} sampled_n5=75 tested_pairs={total} posets_n5={len(ps5)}')

if __name__=='__main__': main()
