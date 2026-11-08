#!/usr/bin/env python3
"""Independent literal matrix-product check of rank-one square-zero commutators."""
from itertools import product
from collections import Counter

def check(n,q):
    def plus(a,b):return (a+b)%q
    def mul(a,b):return (a*b)%q
    vlist=list(product(range(q),repeat=n))
    candidates=[]
    # Form matrices directly and deduplicate without relying on normalized outer products.
    for u in vlist:
        for phi in vlist:
            if not any(u) or not any(phi) or sum(u[i]*phi[i] for i in range(n))%q:continue
            candidates.append(tuple(u[i]*phi[j]%q for i in range(n) for j in range(n)))
    factors=sorted(set(candidates))
    def matrix_mult(A,B):
        return tuple(sum(A[n*i+k]*B[n*k+j] for k in range(n))%q for i in range(n) for j in range(n))
    zero=(0,)*(n*n)
    for A in factors:assert matrix_mult(A,A)==zero
    fibers=Counter()
    for A in factors:
        for B in factors:
            AB=matrix_mult(A,B)
            BA=matrix_mult(B,A)
            C=tuple((AB[k]-BA[k])%q for k in range(n*n))
            fibers[C]+=1
    N=(q**n-1)//(q-1)*(q**(n-1)-1)
    pred0=N*((q**(n-1)-1)+(((q**(n-1)-1)//(q-1))-1)*(q**(n-2)-1))
    pred1=2*q**(n-1)*(q**(n-2)-1)
    pred2=(2*(q-1) if q%2 else q*(q*q-1))
    assert len(factors)==N
    assert fibers[zero]==pred0
    for C,c in fibers.items():
        if C==zero:continue
        if matrix_mult(C,C)==zero: assert c==pred1
        else: assert c==pred2
    assert sum(fibers.values())==N*N
    print('LITERAL_PASS',n,q,'factors',N,'targets',len(fibers),'ordered_pairs',N*N)

if __name__=='__main__':
    for n,q in [(2,3),(2,5),(3,2),(3,3),(4,2)]:check(n,q)
    print('LITERAL_MATRIX_BRACKET_CHECKS_PASS')
