#!/usr/bin/env python3
"""Direct labeled-vertex distance and slide enumeration; standard-library only."""
from itertools import combinations
from collections import Counter, deque
from math import comb

def prediction(n):
    k=n//2
    if n%2: return n*3*(2**(k-1)), sorted([n*3*(2**(k-1))])
    parts=[]
    for p in range(k+1):
        if (2*p-k)%3 == 0:
            if p in (0,k): parts += [1]*6
            else: parts += [3*comb(k,p)]*2
    return 2*(2**k+2*(-1)**k),sorted(parts)

def compatible(a,b,n):
    c,r=divmod(a,3); d,s=divmod(b,3)
    distance=min((c-d)%n,(d-c)%n) + (r!=s)
    return distance>2

def solve(n):
    V=range(3*n); k=n//2
    pair={(a,b):compatible(a,b,n) for a in V for b in range(a+1,3*n)}
    def ok(S):return all(pair[min(a,b),max(a,b)] for a,b in combinations(S,2))
    configs={frozenset(S) for S in combinations(V,k) if ok(S)}
    exp,exp_parts=prediction(n)
    assert len(configs)==exp,(n,len(configs),exp)
    first=next(iter(configs))
    # Directly derive each potential slide from the Cartesian graph's edges.
    neigh={a:{3*((a//3+1)%n)+a%3,3*((a//3-1)%n)+a%3,
              3*(a//3)+(a%3+1)%3,3*(a//3)+(a%3+2)%3} for a in V}
    rem=set(configs); sizes=[]; edges=0
    while rem:
        start=rem.pop(); todo=[start]; size=0
        while todo:
            A=todo.pop();size+=1
            for a in A:
                for b in neigh[a]-A:
                    B=frozenset((A-{a})|{b})
                    if B in configs:
                        edges+=1
                        if B in rem:rem.remove(B);todo.append(B)
        sizes.append(size)
    sizes.sort()
    assert sizes==exp_parts,(n,sizes,exp_parts)
    return f'n={n} optimum={k} states={len(configs)} components={len(sizes)} profile={dict(sorted(Counter(sizes).items()))} directed_arcs={edges}'

if __name__=='__main__':
    for n in range(5,12):print(solve(n))
    print('PASS: direct Cartesian-distance exhaustive tests')
