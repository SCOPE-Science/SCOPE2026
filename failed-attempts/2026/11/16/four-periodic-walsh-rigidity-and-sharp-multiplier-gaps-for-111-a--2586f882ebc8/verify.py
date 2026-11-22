#!/usr/bin/env python3
"""Exact integer verification of Walsh spectra of binary words avoiding 111.

The infinite-dimensional theorem uses a symbolic transfer-matrix proof;
this script independently checks its finite-range identities.
"""
from math import gcd
from functools import reduce

P = ((1,1,1),(1,0,0),(0,1,0))
N = ((1,1,1),(-1,0,0),(0,-1,0))
B = ((0,0,0),(1,0,0),(0,1,0))
E = (1,0,0)

def mm(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3))
                  for j in range(3)) for i in range(3))

def ident():
    return ((1,0,0),(0,1,0),(0,0,1))

def power(a,k):
    r=ident()
    for _ in range(k): r=mm(r,a)
    return r

def mv(a,v):
    return tuple(sum(a[i][k]*v[k] for k in range(3)) for i in range(3))

def signed_count(mask,n):
    v=E
    for j in range(n):
        t = -1 if (mask >> j)&1 else 1
        v=(sum(v),t*v[0],t*v[1])
    return sum(v)

def valid(x,n):
    return not bool(x & (x>>1) & (x>>2))

def walsh_transform(a):
    n=len(a);h=1
    while h<n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                u=a[j];v=a[j+h]
                a[j]=u+v;a[j+h]=u-v
        h*=2
    return a

assert power(N,4)==ident()
assert all(x%2 == y for row,xrow in zip(power(P,4),ident()) for x,y in zip(row,xrow))
assert all(x%4 == y for row,xrow in zip(power(P,8),ident()) for x,y in zip(row,xrow))
for n in range(2,35,4):
    for i in range(1,n+1):
        v=mv(power(P,i-1),E)
        v=mv(B,v)
        v=mv(power(P,n-i),v)
        assert sum(v)%2==0, (n,i)
assert [signed_count((1<<n)-1,n) for n in range(1,9)]==[0,0,1,1,0,0,1,1]

for n in range(1,17):
    a=[int(valid(x,n)) for x in range(1<<n)]
    legal_count=sum(a)
    fw=walsh_transform(a)
    assert len(fw)==(1<<n)
    for mask,w in enumerate(fw):
        assert w == signed_count(mask,n), (n,mask,w)
    residue=n%4
    gap=({0:1,1:2,2:4,3:1})[residue]
    nonzero=[abs(w) for w in fw if w]
    observed_gcd=reduce(gcd,fw,0)
    assert min(nonzero)==gap and observed_gcd==gap, n
    assert (0 not in fw)==(residue in (0,3)), n
    if residue==1:
        witness=(((1<<n)-1)^1)  # leading +, then a number of negative blocks divisible by 4
    elif residue==2:
        witness=(((1<<n)-1)^3)  # leading ++, then a multiple of four negative signs
    else:
        witness=(1<<n)-1
    assert abs(fw[witness])==gap, n
    print('n=%02d valid=%6d zeros=%6d min_nonzero=%d gcd=%d' %
          (n,legal_count,fw.count(0),gap,observed_gcd))
for n in [17,18,19,20,21,22,23,24,97,98,99,100]:
    residue=n%4
    mask=(1<<n)-1
    if residue==1: mask^=1
    elif residue==2: mask^=3
    gap={0:1,1:2,2:4,3:1}[residue]
    assert abs(signed_count(mask,n))==gap
    if residue in (1,2):
        assert signed_count((1<<n)-1,n)==0
print('TRIBONACCI_CUBE_WALSH_PERIOD_FOUR_PASS')
