#!/usr/bin/env python3
"""Reproduce the rank-one Boolean-relation commuting clique counts.
Requires Python 3 standard library only. Run: python3 verify.py.
"""
from functools import lru_cache
from math import comb, factorial
from collections import defaultdict

@lru_cache(None)
def first_stirling(n, h):
    if n == h == 0: return 1
    if n == 0 or h == 0 or h > n: return 0
    return first_stirling(n-1, h-1) - (n-1)*first_stirling(n-1, h)

@lru_cache(None)
def second_stirling(n, k):
    if n == k == 0: return 1
    if n == 0 or k == 0 or k > n: return 0
    return second_stirling(n-1, k-1)+k*second_stirling(n-1,k)

@lru_cache(None)
def labeled(n, k, h):
    return sum((-1)**(a+b+c)*comb(h,a)*comb(h,b)*comb(k,c)
               *(2**(k+h-a)+2**(k+h-b)+k-c-1)**n
               for a in range(h+1) for b in range(h+1) for c in range(k+1))

def clique_coefficient(n,k,j):
    numerator=sum(first_stirling(j,h)*labeled(n,k,h) for h in range(j+1))
    divisor=factorial(k)*factorial(j)
    assert numerator%divisor==0
    return numerator//divisor

def maximal_formula(n):
    out=defaultdict(int)
    for l in range(n+1):
        for r in range(n-l+1):
            p=n-l-r
            multin=factorial(n)//(factorial(l)*factorial(r)*factorial(p))
            for k in range(p+1):
                if not second_stirling(p,k): continue
                if l and r:
                    decoration=2**(k*(l+r))
                    j=(2**l-1)*(2**r-1)
                elif k:
                    decoration=(2**k-1)**(l+r)
                    j=0
                else:
                    continue
                out[k+j]+=multin*second_stirling(p,k)*decoration
    return dict(out)

def matrix(A,B,n):
    return tuple(B if A & (1<<i) else 0 for i in range(n))

def product(X,Y,n):
    rows=[]
    for i in range(n):
        t=X[i]; z=0
        for j in range(n):
            if (t>>j)&1: z |= Y[j]
        rows.append(z)
    return tuple(rows)

def direct_cliques(n):
    V=[(A,B) for A in range(1,1<<n) for B in range(1,1<<n)]
    N=len(V)
    matrices=[matrix(A,B,n) for A,B in V]
    adj=[0]*N
    for i in range(N):
        for j in range(i+1,N):
            if product(matrices[i],matrices[j],n)==product(matrices[j],matrices[i],n):
                adj[i]|=1<<j
                adj[j]|=1<<i
    counts=defaultdict(int)
    max_counts=defaultdict(int)
    counts[(0,0)]=1
    def visit(candidates,common,k,j):
        while candidates:
            bit=candidates & -candidates
            candidates-=bit
            v=bit.bit_length()-1
            is_idem=product(matrices[v],matrices[v],n)==matrices[v]
            nk=k+int(is_idem)
            nj=j+int(not is_idem)
            counts[(nk,nj)]+=1
            new_common=common & adj[v]
            if not new_common: max_counts[nk+nj]+=1
            visit(candidates & adj[v],new_common,nk,nj)
    visit((1<<N)-1,(1<<N)-1,0,0)
    return dict(counts),dict(max_counts)

def main():
    # Direct Boolean multiplication, not the coordinate-alphabet commutation test.
    expected={
       1:({(0,0):1,(1,0):1},{1:1}),
       2:({(0,0):1,(0,1):2,(1,0):7,(2,0):1},{1:7,2:1}),
       3:({(0,0):1,(0,1):12,(0,2):18,(0,3):6,(1,0):37,(1,1):24,(2,0):24,(3,0):1},{1:13,2:45,3:7}),
    }
    for n in range(1,5):
        observed,max_observed=direct_cliques(n)
        if n in expected:
            assert (observed,max_observed)==expected[n],(n,'direct known checks')
        full={key:clique_coefficient(n,*key) for key in observed}
        assert full==observed,(n,'clique formula',full,observed)
        assert maximal_formula(n)==max_observed,(n,'maximal',maximal_formula(n),max_observed)
        assert sum(count for (k,j),count in observed.items() if k+j==1)==(2**n-1)**2
        print('n=',n,'vertices=',(2**n-1)**2,'cliques=',sum(observed.values()),
              'maximal=',sum(max_observed.values()),'clique_max=',max(max_observed),
              'max_spectrum=',sorted(max_observed.items()))
    print('VERIFY_OK')
if __name__=='__main__':main()
