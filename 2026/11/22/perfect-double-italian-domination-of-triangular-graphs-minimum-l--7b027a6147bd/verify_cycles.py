#!/usr/bin/env python3
"""Independently build optimal root-label supports from disjoint cycles / doubled edges.
Cross-check direct neighborhood constraints and coefficients of the EGF.
"""
from itertools import combinations,permutations
from collections import Counter
from math import comb, factorial

def all_labelings(n):
    V=tuple(range(n))
    E=list(combinations(V,2)); ei={e:i for i,e in enumerate(E)}
    f=[0]*len(E)
    count=0; by_double=Counter()
    def rec(U, t):
        nonlocal count
        if not U:
            degrees=[0]*n
            for (u,v),w in zip(E,f):
                degrees[u]+=w;degrees[v]+=w
            assert degrees==[2]*n
            for (u,v),w in zip(E,f):
                if w<=1: assert 3<=degrees[u]+degrees[v]-w<=4
            assert sum(f)==n
            count+=1;by_double[t]+=1
            return
        x=U[0]
        for y in U[1:]:
            key=(x,y)
            f[ei[key]]=2
            rec(tuple(z for z in U if z!=x and z!=y),t+1)
            f[ei[key]]=0
        for k in range(3,len(U)+1):
            for S0 in combinations(U[1:],k-1):
                S=(x,)+S0
                rest=tuple(z for z in U if z not in S)
                # anchor smallest vertex and remove reversal by comparing endpoints
                for path in permutations(S0):
                    if path[0]>path[-1]: continue
                    cycle=(x,)+path
                    chosen=[ei[tuple(sorted((cycle[i],cycle[(i+1)%k])))] for i in range(k)]
                    for j in chosen:f[j]=1
                    rec(rest,t)
                    for j in chosen:f[j]=0
    rec(V,0)
    return count,by_double

def recurrence(N):
    a=[0]*(N+1);a[0]=1
    for n in range(1,N+1):
        for k in range(2,n+1):
            c=1 if k==2 else factorial(k-1)//2
            a[n]+=comb(n-1,k-1)*c*a[n-k]
    return a

if __name__=='__main__':
    a=recurrence(12)
    for n in range(5,10):
        got,hist=all_labelings(n)
        assert got==a[n],(n,got,a[n])
        print(f'n={n}: cycle-support count={got}, double-edge histogram={dict(sorted(hist.items()))}, EGF recurrence={a[n]}')
    print('series n=5..12:',a[5:])
    print('CYCLE_EGF_PASS')
