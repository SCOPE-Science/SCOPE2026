#!/usr/bin/env python3
"""Exact finite sanity checks for the Prym-volume profile theorem.
Only standard-library rational arithmetic is used.
These tests do not replace the symbolic all-n proof in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import prod

def signclass(s):
    s=tuple(s)
    return s if s[0]==1 else tuple(-v for v in s)

def cuts(n):
    return [(1,)+v for v in product((1,-1),repeat=n-1)]

def weights(lengths):
    n=len(lengths)
    return {(i,j):prod(lengths[k] for k in range(n) if k!=i and k!=j)
            for i,j in combinations(range(n),2)}

def profile_from_weights(w,n):
    return {s:sum((v for (i,j),v in w.items() if s[i]!=s[j]), F(0))
            for s in cuts(n)}

def fourier(q,index):
    return sum((v*prod(s[k] for k in index) for s,v in q.items()),F(0))/len(q)

def inverse(q,n):
    return {(i,j):-2*fourier(q,(i,j)) for i,j in combinations(range(n),2)}

def subset_cut(q,n,inds):
    s=[1]*n
    for i in inds:s[i]=-1
    return q[signclass(s)]

def check(lengths):
    lengths=tuple(F(v) for v in lengths)
    n=len(lengths)
    w=weights(lengths)
    q=profile_from_weights(w,n)
    assert len(q)==2**(n-1)
    assert q[(1,)*n]==0
    assert all(v>0 for s,v in q.items() if s!=(1,)*n)
    assert inverse(q,n)==w
    for i,j in combinations(range(n),2):
        recovered=(subset_cut(q,n,[i])+subset_cut(q,n,[j])
                   -subset_cut(q,n,[i,j]))/2
        assert recovered==w[i,j]
    # There are no Fourier coefficients above character weight 2.
    for r in range(4,n+1,2):
        for subset in combinations(range(n),r):
            assert fourier(q,subset)==0
    if n>=4:
        for i,j,k,l in combinations(range(n),4):
            assert w[i,j]*w[k,l]==w[i,k]*w[j,l]==w[i,l]*w[j,k]
    K=(n-1)*(n-2)//2
    assert prod(w.values())==prod(lengths)**K
    # Check the reconstructed squared lengths without numerical roots.
    P=prod(lengths)
    for i in range(n):
        others=[v for v in range(n) if v!=i]
        j,k=others[:2]
        assert P*w[min(j,k),max(j,k)]/(w[min(i,j),max(i,j)]*
                 w[min(i,k),max(i,k)])==lengths[i]**2
    print("PASS n=%s covers=%s lengths=%s"%(n,2**(n-1)-1,lengths))

for L in [
    (2,3,5),
    (1,2,4,6),
    (2,3,5,7,11),
    (F(1,2),F(2,3),3,5,7,11),
    (1,1,1,1,1,1,1)
]:
    check(L)

# Genuine non-realizable cut profile: all Fourier weights positive,
# but these weights fail a tetrad relation.
w={(0,1):F(24),(0,2):F(12),(0,3):F(8),
   (1,2):F(6),(1,3):F(4),(2,3):F(3)}
q=profile_from_weights(w,4)
assert inverse(q,4)==w
assert w[0,1]*w[2,3]!=w[0,2]*w[1,3]
print("PASS positive-nonrealizable tetrad obstruction")
print("EXACT_PROFILE_CHECKS_PASS")
