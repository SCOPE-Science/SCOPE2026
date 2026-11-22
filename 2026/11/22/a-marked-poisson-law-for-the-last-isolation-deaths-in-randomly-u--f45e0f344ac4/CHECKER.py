"""Finite exact checks for isolated-vertex death events in cycle powers.
Standard-library-only; run: python checker.py.
"""
from itertools import permutations
from math import factorial
from collections import Counter

def neighbors(n,d,v):
    return [((v+j)%n, j) for j in range(-d,d+1) if j]

def events(n,d,order):
    # order is forward permutation; reverse ranks start at one.
    fpos=[0]*n
    for i,v in enumerate(order):fpos[v]=i+1
    rank=[n+1-x for x in fpos]
    ans=[]
    for v in range(n):
        opts=neighbors(n,d,v)
        t,j=max((rank[u],j) for u,j in opts)
        if t<rank[v]:
            ans.append((t,v,fpos[v],j))
    return sorted(ans)

def slow_intervals(n,d,order):
    fpos=[0]*n
    for i,v in enumerate(order):fpos[v]=i+1
    ranks=[n+1-x for x in fpos]
    intervals=[]
    for v in range(n):
        active=[]
        for k in range(n+1):
            u=set(order[:n-k])
            active.append(v in u and all(w not in u for w,j in neighbors(n,d,v)))
        if any(active):
            s=next(k for k,a in enumerate(active) if a)
            e=max(k for k,a in enumerate(active) if a)
            assert active[s:e+1]==[True]*(e-s+1)
            intervals.append((s,e,v))
            assert s==max(ranks[w] for w,j in neighbors(n,d,v))
            assert e==ranks[v]-1
    return sorted(intervals)

def falling(a,b):
    if a<b:return 0
    z=1
    for i in range(b):z*=a-i
    return z

checks=0
for n,d in ((5,1),(6,1),(7,1),(8,1),(6,2),(7,2)):
    summed=[0]*(n+1)
    count=0
    for o in permutations(range(n)):
        count+=1
        es=events(n,d,o)
        ints=slow_intervals(n,d,o)
        assert sorted((t,v) for t,v,_,_ in es)==sorted((s,v) for s,_,v in ints)
        checks+=1
        for t,v,pos,j in es:
            assert -d<=j<=d and j!=0
            assert (v+j)%n in o[n-t:n]
            assert pos==o.index(v)+1
            checks+=3
        for k in range(n+1):
            val=sum(s<=k<=e for s,e,v in ints)
            summed[k]+=val
            if val != sum(t<=k<n+1-pos for t,v,pos,j in es):
                raise AssertionError((n,d,k,o))
            checks+=1
        kfirst=min((t for t,v,_,_ in es),default=None)
        klast=max((k for k in range(n+1) if any(s<=k<=e for s,e,v in ints)), default=None)
        if kfirst is not None:
            assert kfirst<=klast
        checks+=1
    for k in range(n+1):
        # Each center is absent from reverse k and all its 2d neighbors are present.
        # P = (k)_{2d}/(n)_{2d} * (n-k)/(n-2d).
        left=summed[k]*falling(n,2*d+1)
        right=count*n*falling(k,2*d)*(n-k)
        assert left==right, (n,d,k,left,right)
        checks+=1
    print('exact',n,d,'permutations',count,'verified')
print('PASSED',checks,'exact combinatorial checks')
