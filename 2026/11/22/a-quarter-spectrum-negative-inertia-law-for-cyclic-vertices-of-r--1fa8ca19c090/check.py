#!/usr/bin/env python3
"""Standalone exact-arithmetic checks for cyclic-set Walsh sign theorem."""
from math import comb, factorial
from itertools import product

def signed_poly(n, s):
    # Coefficients of (1-z)^s(1+z)^(n-s).
    return [sum((-1)**j*comb(s,j)*comb(n-s,k-j)
                for j in range(max(0,k-(n-s)),min(s,k)+1)) for k in range(n+1)]

def multiplier(n, s):
    a=signed_poly(n,s)
    return sum(a[k]*factorial(k)*k*n**(n-k)//n for k in range(1,n+1))

def cyclic_mask(mapping):
    n=len(mapping); cyclic=0; visited=[False]*n
    for start in range(n):
        if visited[start]: continue
        here={}; path=[]; v=start
        while v not in here and not visited[v]:
            here[v]=len(path); path.append(v); v=mapping[v]
        if v in here:
            for u in path[here[v]:]: cyclic|=1<<u
        for u in path:visited[u]=True
    return cyclic

def direct_histogram(n):
    counts=[0]*(1<<n)
    for f in product(range(n),repeat=n):
        counts[cyclic_mask(f)]+=1
    return counts

def polynomial_mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def polynomial_pow(a,n):
    v=[1]
    for _ in range(n):v=polynomial_mul(v,a)
    return v

def execute():
    count=0
    for n in range(2,7):
        hist=direct_histogram(n)
        assert sum(hist)==n**n;count+=1
        for k in range(1,n+1):
            predicted=factorial(k)*k*n**(n-k)//n
            assert all(hist[mask]==predicted for mask in range(1,1<<n) if mask.bit_count()==k)
            count+=1
        assert hist[0]==0;count+=1
        for s in range(n+1):
            mask=(1<<s)-1
            brute=sum(c*(-1 if (r&mask).bit_count()%2 else 1) for r,c in enumerate(hist))
            assert brute==multiplier(n,s),(n,s,brute,multiplier(n,s))
            count+=1
    for n in range(2,50):
        for s in range(1,n+1):
            if s%2 and 2*s>=n:
                assert multiplier(n,s)<0,(n,s)
                count+=1
    for n in range(2,26):
        for s in range(1,n+1):
            g=signed_poly(n,s)
            d=[(k+1)*g[k+1] for k in range(n)]
            if s<n:
                p=polynomial_mul(polynomial_mul(polynomial_pow([1,-1],s-1),polynomial_pow([1,1],n-s-1)),[n-2*s,-n])
            else:
                p=[-n*x for x in polynomial_pow([1,-1],n-1)]
            assert d==p,(n,s)
            count+=1
    print('PASS',count,'exact assertions; independent maps through n=6; integral derivative and signs through n=49')
if __name__=='__main__': execute()
