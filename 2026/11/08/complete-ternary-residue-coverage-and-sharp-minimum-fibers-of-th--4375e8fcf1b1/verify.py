#!/usr/bin/env python3
"""Finite exact checks for Perrin 3-adic residue theorem. Python 3 stdlib."""
from collections import Counter

def multiply(a,b,m):
    c=[0]*5
    for i in range(3):
        for j in range(3): c[i+j]+=a[i]*b[j]
    for i in (4,3):
        c[i-2]+=c[i]; c[i-3]+=c[i]
    return tuple(x%m for x in c[:3])

def perrin_mod(M,N):
    a=[3%M,0,2%M]
    for i in range(3,N): a.append((a[i-2]+a[i-3])%M)
    return a

a=(0,1,0);v=(1,0,0)
for _ in range(13):v=multiply(v,a,81)
assert v==(7,12,9)
assert all((x**3-x-1)%3!=0 for x in range(3))
P=perrin_mod(3**8,50)
r=[P[i]%3 for i in range(13)]
d=[((P[i+13]-P[i])//3)%3 for i in range(13)]
assert r==[0,0,2,0,2,2,2,1,1,0,2,1,2]
assert d==[0,2,1,2,0,0,2,0,2,2,2,1,1]
assert [P[i]%9 for i in (0,4,5,7)]==[3,2,5,7]
checks=0
for k in range(1,7):
    M=3**k;T=13*3**(k-1)
    vals=perrin_mod(M,T+3)
    counts=Counter(vals[:T]); assert len(counts)==M
    # Consecutive triples distinguish any shorter exact period.
    for t in range(1,T):
        if T%t==0:
            assert any(vals[i]!=vals[i+t] for i in range(3))
    assert vals[:3]==vals[T:T+3]
    if k==1:
        assert [counts[i] for i in range(3)]==[4,3,6]
    else:
        for x in range(M):
            floor={0:3,1:2,2:4}[x%3]
            assert counts[x]>=floor
            if x%9 in (0,1,8): assert counts[x]==floor
            checks+=1
print('VERIFY_OK cubic_alpha13=(7,12,9); base_branches=13; periods_k=1..6; residue_targets=',checks)
