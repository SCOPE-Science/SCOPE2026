#!/usr/bin/env python3
from functools import lru_cache
from itertools import combinations
from math import comb, factorial

def catalan(n):
    return comb(2*n,n)//(n+1)

def odd_df(m):
    if m <= 0:
        return 1
    r=1
    for j in range(m,0,-2): r*=j
    return r

def key(t):
    return repr(t)

@lru_cache(None)
def rooted_nonplane(labels):
    labels=tuple(labels)
    if len(labels)==1: return frozenset({labels[0]})
    S=set(labels); m=min(labels); out=set()
    rest=sorted(S-{m})
    # one side must contain the least label: unique representative of each unordered root split
    for r in range(0,len(rest)+1):
        for extra in combinations(rest,r):
            A={m,*extra}
            if A==S: continue
            B=S-A
            for x in rooted_nonplane(tuple(sorted(A))):
                for y in rooted_nonplane(tuple(sorted(B))):
                    a,b=sorted((x,y), key=key)
                    out.add((a,b))
    return frozenset(out)

@lru_cache(None)
def rooted_plane(labels):
    labels=tuple(labels)
    if len(labels)==1: return frozenset({labels[0]})
    S=set(labels); out=set(); arr=sorted(S)
    # ordered split: choose the left leaf set A, any nonempty proper subset
    for r in range(1,len(arr)):
        for aa in combinations(arr,r):
            A=set(aa); B=S-A
            for x in rooted_plane(tuple(sorted(A))):
                for y in rooted_plane(tuple(sorted(B))):
                    out.add((x,y))
    return frozenset(out)

def leaves(t):
    if isinstance(t,int): return frozenset({t})
    return leaves(t[0])|leaves(t[1])

def unrooted_split_signature(t):
    """Suppress the degree-2 root; canonical edge-split set determines the unrooted labeled tree."""
    allL=leaves(t)
    sig=set()
    def visit(u,is_root=False):
        if isinstance(u,int): return
        for child in u:
            A=leaves(child); B=allL-A
            # edge at a root child occurs twice as complementary splits; set() merges them,
            # exactly modeling root suppression and replacement by one edge.
            ca=tuple(sorted(A)); cb=tuple(sorted(B))
            sig.add(min(ca,cb))
            visit(child)
    visit(t,True)
    return tuple(sorted(sig,key=lambda z:(len(z),z)))

def S2(n,k):
    dp=[[0]*(k+1) for _ in range(n+1)]; dp[0][0]=1
    for i in range(1,n+1):
        for j in range(1,min(i,k)+1):
            dp[i][j]=dp[i-1][j-1]+j*dp[i-1][j]
    return dp[n][k]

def a3(n): return factorial(n)*catalan(n-1)
def a4(n): return odd_df(2*n-3)
def a6(n): return 1 if n<=2 else odd_df(2*n-5)

# Direct tree generation: rooted nonplane through 7, plane through 6.
for n in range(1,8):
    rn=rooted_nonplane(tuple(range(n)))
    assert len(rn)==a4(n),(n,len(rn),a4(n))
    if n<=6:
        rp=rooted_plane(tuple(range(n)))
        assert len(rp)==a3(n),(n,len(rp),a3(n))
        # Forgetting all left/right choices has the claimed uniform fiber.
        def forget(u):
            if isinstance(u,int): return u
            x,y=forget(u[0]),forget(u[1]); return tuple(sorted((x,y),key=key))
        fibers={r:0 for r in rn}
        for p in rp: fibers[forget(p)]+=1
        assert set(fibers.values())=={2**(n-1)},(n,set(fibers.values()))

# Forgetting the root: directly canonicalize by unrooted edge splits through n=7.
for n in range(3,8):
    rn=rooted_nonplane(tuple(range(n)))
    fibers={}
    for t in rn:
        s=unrooted_split_signature(t)
        fibers[s]=fibers.get(s,0)+1
    assert len(fibers)==a6(n),(n,len(fibers),a6(n))
    assert set(fibers.values())=={2*n-3},(n,set(fibers.values()),2*n-3)

# Formula and collapse checks, plus full ordered-tuple Stirling transforms.
expected_injective={
    'M3':[1,2,12,120,1680,30240,665280],
    'M4':[1,1,3,15,105,945,10395],
    'M6':[1,1,1,3,15,105,945],
}
for name,f in [('M3',a3),('M4',a4),('M6',a6)]:
    got=[f(n) for n in range(1,8)]
    assert got==expected_injective[name],(name,got)
for n in range(1,8):
    assert a3(n)==(2**(n-1))*a4(n)
for n in range(3,8):
    assert a4(n)==(2*n-3)*a6(n)

expected_full={
    'M3':[1,3,19,207,3211,64383,1581259],
    'M4':[1,2,7,41,346,3797,51157],
    'M6':[1,2,5,17,86,647,6665],
}
for name,f in [('M3',a3),('M4',a4),('M6',a6)]:
    got=[sum(S2(n,k)*f(k) for k in range(1,n+1)) for n in range(1,8)]
    assert got==expected_full[name],(name,got)

print('VERIFY_OK')
