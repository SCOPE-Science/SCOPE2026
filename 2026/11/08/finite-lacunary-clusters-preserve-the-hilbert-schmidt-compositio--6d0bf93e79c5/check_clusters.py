#!/usr/bin/env python3
"""Exact finite corroboration of the cluster Toeplitz-block identities."""
from fractions import Fraction as F
from collections import defaultdict
from math import prod

def convol(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def power(a,k):
    h=[F(1)]
    for _ in range(k):h=convol(h,a)
    return h

checks=0
for q in (2,3,4):
    for Fset in ((0,1),(0,2,4),(0,1,2,3),(0,3,5)):
        L=max(Fset)
        N=[q**j for j in range(8,18)]
        if min(N[1]-N[0],N[0])<=L+2:continue
        for coeff in ((F(2,7),F(1,5),F(1,9)),(F(1,3),F(-1,4),F(2,9),F(1,6))):
            a=[F(0)]+list(coeff[1:]);d=next(i for i,v in enumerate(a) if v)
            k=L//d+1
            ell=k*d
            h=power(a,k)
            for m in range(ell):
                assert (h[m] if m<len(h) else 0)==0
                checks+=1
            assert h[ell]==a[d]**k;checks+=1
            # Output sites are outside the exceptional clusters for the chosen tail.
            exc={n+v for n in N for v in Fset}
            for n in N[1:-1]:
                for s in Fset:
                    assert n+ell+s not in exc
                    checks+=1
            # Each diagonal block is lower triangular with one constant nonzero diagonal.
            for s in Fset:
                for r in Fset:
                    t=ell+s-r
                    val=h[t] if 0<=t<len(h) else F(0)
                    if s<r: assert val==0
                    if s==r:assert val==h[ell]
                    checks+=1
            # An exact sparse-coefficient witness: block transfer for each cluster.
            for n in N[1:-1]:
                u={n+r:F((r+1)*(r+2),17) for r in Fset}
                for s in Fset:
                    out=sum((v*(h[n+ell+s-j] if 0<=n+ell+s-j<len(h) else F(0)) for j,v in u.items()),F(0))
                    diag=sum((u[n+r]*(h[ell+s-r] if 0<=ell+s-r<len(h) else F(0)) for r in Fset),F(0))
                    assert out==diag
                    checks+=1
        # Bounded difference multiplicities; this checks a finite sample, not the infinite proof.
        counts=defaultdict(int)
        for j in range(len(N)):
            for i in range(j):counts[N[j]-N[i]]+=1
        bound=1+__import__('math').ceil(__import__('math').log(q/(q-1),q))
        assert max(counts.values())<=bound;checks+=1
print('LACUNARY_CLUSTER_EXACT_BLOCK_CHECK_OK',checks)
