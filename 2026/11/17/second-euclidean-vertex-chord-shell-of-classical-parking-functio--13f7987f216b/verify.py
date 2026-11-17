#!/usr/bin/env python3
"""Exact-integer verification of the second vertex-chord Euclidean shell.

Standalone Python 3, standard library only. All square distances integral.
"""
from itertools import permutations
from collections import Counter
from math import factorial

def layer(n,k):
    return (1,)*k + tuple(range(k+1,n+1))

def f(t):
    return (t-1)*t*(2*t-1)//6

def diameter(n):
    m=n//2
    return 2*f(n)-f(m)-f(n-m)

def gap(n):
    if n%2==0: return n-1
    m=n//2
    return min(m*m,4*m)

def second_count(n):
    return factorial(n)*(2 if n in (4,9) else 1)

def second_profiles(n):
    m=n//2
    if n==2: return {(1,2)}
    if n%2==0:
        out={(m-1,m+1)}
        if n==4: out.add((1,2))
        return out
    out=set()
    if m<=4: out|={(m,m),(m+1,m+1)}
    if m>=4: out.add((m-1,m+2))
    return out

def rearrangement_profile(n,k,l):
    x=layer(n,k)
    y=layer(n,l)[::-1]
    return sum((a-b)*(a-b) for a,b in zip(x,y))

def verify_profiles(n):
    vals={(k,l):rearrangement_profile(n,k,l) for k in range(1,n+1) for l in range(1,n+1)}
    ranked=sorted(set(vals.values()),reverse=True)
    assert ranked[0]==diameter(n), (n,ranked[0],diameter(n))
    assert ranked[0]-ranked[1]==gap(n),(n,ranked[:3],gap(n))
    found={tuple(sorted((k,l))) for (k,l),v in vals.items() if v==ranked[1]}
    assert found==second_profiles(n),(n,found,second_profiles(n))

def verify_exhaustive(n):
    vs = {p:k for k in range(1,n+1) for p in set(permutations(layer(n,k)))}
    points=list(vs)
    counts=Counter()
    by_layers=Counter()
    for i,x in enumerate(points):
        for y in points[i+1:]:
            ds=sum((a-b)*(a-b) for a,b in zip(x,y))
            counts[ds]+=1
            by_layers[(ds,tuple(sorted((vs[x],vs[y]))))]+=1
    top=sorted(counts,reverse=True)[:2]
    assert top==[diameter(n),diameter(n)-gap(n)],(n,top)
    assert counts[top[1]]==second_count(n), (n,counts[top[1]],second_count(n))
    assert {v for (d,v),ct in by_layers.items() if d==top[1]}==second_profiles(n)
    return (n,len(vs),top[0],top[1],counts[top[1]])

def main():
    exhaustive=[verify_exhaustive(n) for n in range(2,7)]
    for n in range(2,151): verify_profiles(n)
    print('PARKING_SECOND_SHELL_PASS exhaustive='+repr(exhaustive)+' complete_layer_profiles_n=2..150')

if __name__=='__main__':
    main()
