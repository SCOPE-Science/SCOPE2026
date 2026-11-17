#!/usr/bin/env python3
"""Finite exact corroboration of the rung-fault collapse theorem.
No external libraries are required.  This checks the Boolean-fiber
conditions, not a substitute for the all-parameter parity proof.
"""
from itertools import combinations

def graph(n):
    N=2*n
    nbr=[{(i-1)%N,(i+1)%N,(i+n)%N} for i in range(N)]
    nbr[0].remove(n);nbr[n].remove(0)
    return nbr

def pairs(n):
    return [(0,n)]+[(j,j+n)for j in range(2,n-1,2)]

def check(n):
    adj=graph(n); P=pairs(n)
    Z={x for pair in P for x in pair}
    W=sorted(set(range(2*n))-Z)
    all_nonempty=0
    for k in range(1,len(W)+1):
        for T in combinations(W,k):
            T=set(T)
            if any((adj[w]&T) for w in T):continue
            all_nonempty+=1
            blocked=set().union(*(adj[w] for w in T))
            # A one-sided available rung is a cone factor.
            # The deleted 0--n rung is itself a simplex factor
            # whenever one of its endpoints is available.
            cone=any((a in blocked)!=(b in blocked) for a,b in P[1:])
            cone=cone or (0 not in blocked or n not in blocked)
            assert cone,(n,sorted(T),P)
    return all_nonempty,len(Z),len(W)

if __name__=='__main__':
    for n in (3,4,7,8,11,12,15,16):
        a,b,c=check(n)
        print(f'n={n}: checked {a} nonempty exterior independent sets; |Z|={b}; |W|={c}; ALL CONE FIBERS')
    print('PASS')
