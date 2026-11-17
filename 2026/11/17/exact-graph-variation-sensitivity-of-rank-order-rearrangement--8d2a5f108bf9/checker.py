"""Exact independent enumerations of graph BV sorting sensitivity; standard library only."""
from itertools import combinations, permutations
from fractions import Fraction
from math import floor
import random

def cuts(n, edges):
    out={}
    for k in range(1,n):
        o=[]
        for S in combinations(range(n),k):
            s=set(S)
            b=sum(w for u,v,w in edges if (u in s)!=(v in s))
            o.append((b,frozenset(S)))
        out[k]=o
    return out

def profiles(n,edges):
    d=cuts(n,edges)
    return max((max(q for q,_ in d[k])/min(q for q,_ in d[k]),k) for k in d)

def tv(vec,edges):
    return sum(w*abs(vec[u]-vec[v]) for u,v,w in edges)

def perm_norm(n,edges,pi):
    # Independent formula: output cut image / input cut via binary extreme-ray ratios.
    inv={pi[i]:i for i in range(n)}
    return max(tv([int(inv[i] in S) for i in range(n)],edges) /tv([int(i in S) for i in range(n)],edges)
               for k in range(1,n) for S in map(set,combinations(range(n),k)))

def test(n,edges):
    C,k=profiles(n,edges)
    q=max(perm_norm(n,edges,p) for p in permutations(range(n)))
    assert C==q,(n,edges,C,q)
    d=cuts(n,edges)
    src=min(d[k],key=lambda x:x[0])[1]
    tgt=max(d[k],key=lambda x:x[0])[1]
    perm=[None]*n
    vin=iter(sorted(src)); vout=iter(sorted(set(range(n))-src))
    for j in range(n): perm[j]=next(vin) if j in tgt else next(vout)
    h=[int(i in src) for i in range(n)]
    f=[0]*n
    for j,i in enumerate(perm): f[i]=4*j
    g=[f[i]+h[i] for i in range(n)]
    A=sorted(f); B=sorted(g)
    assert tv([B[i]-A[i] for i in range(n)],edges)/tv(h,edges)==C
    return C

def connected(n,edges):
    sets=[{i} for i in range(n)]
    roots=list(range(n))
    for u,v,_ in edges:
        a,b=roots[u],roots[v]
        if a!=b:
            for j in range(n):
                if roots[j]==b:roots[j]=a
    return len(set(roots))==1

count=0
for n in range(2,5):
    possible=list(combinations(range(n),2))
    for mask in range(1,1<<len(possible)):
        e=[(u,v,Fraction(1)) for i,(u,v) in enumerate(possible) if mask>>i&1]
        if connected(n,e): test(n,e);count+=1
print('ALL_CONNECTED_SIMPLE_GRAPHS_EXACTLY_CHECKED',count)

rng=random.Random(916)
for n in (3,4,5):
    for repeat in range(8):
        possible=list(combinations(range(n),2))
        while True:
            e=[(u,v,Fraction(rng.randint(1,9),rng.randint(1,8))) for u,v in possible if rng.getrandbits(1)]
            if connected(n,e):break
        test(n,e)
print('EXACT_WEIGHTED_GRAPHS_CHECKED',24)

for n in range(2,13):
    path=[(i,i+1,Fraction(1)) for i in range(n-1)]
    star=[(0,i,Fraction(1)) for i in range(1,n)]
    assert profiles(n,path)[0]==n-1
    assert profiles(n,star)[0]==n-1
    if n>=3:
        cycle=path+[(n-1,0,Fraction(1))]
        assert profiles(n,cycle)[0]==n//2
print('PATH_STAR_CYCLE_FORMULAS_PASSED',11)

for q in range(2,7):
    e=[(i,j,Fraction(1)) for s in (0,q) for i,j in combinations(range(s,s+q),2)] + [(0,q,Fraction(1))]
    C,k=profiles(2*q,e)
    assert C==q*q//2+1,(q,C,k)
print('BARBELL_EXACT_QUADRATIC_GROWTH_PASSED',5)
print('ALL_SORTING_GRAPH_BV_TESTS_PASSED')
