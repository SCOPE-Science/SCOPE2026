#!/usr/bin/env python3
"""Exact reproducibility checks for the enclosing-sphere classification.
Run: python arbor_sphere_verifier.py
All arithmetic below is rational; numerical optimizers are not needed.
Finite checks support, but do not replace, the proof for all parameters.
"""
from fractions import Fraction as F
from itertools import combinations


def construction(n, k):
    ell = n-k
    if ell == 1:
        c = [F(1,2)]*k + [F(n,2)]
        R2 = F(k+n*n,4)
        contact_count = 2**k+1
        weights = [([1]*k+[0], F(1,2)), ([0]*k+[n], F(1,2))]
    elif ell == 2:
        denom=n*n+2*k
        a=F(k,denom)
        b=F(n,2)*(1-a)
        c = [a]*k+[b,b]
        R2=F(k,1)*(1-a)**2+2*b*b
        contact_count=3
        weights = [([1]*k+[0,0], a)]
        for j in range(ell):
            v=[0]*n;v[k+j]=n
            weights.append((v,(1-a)/2))
    else:
        c = [F(0)]*k+[F(n,ell)]*ell
        R2=F(n*n*(ell-1),ell)
        contact_count=ell
        weights=[]
        for j in range(ell):
            v=[0]*n;v[k+j]=n
            weights.append((v,F(1,ell)))
    return c,R2,contact_count,weights


def verts(n,k):
    ell=n-k
    for j in range(k+1):
        for S in combinations(range(k),j):
            x=[0]*n
            for i in S:x[i]=1
            yield tuple(x)
            for t in range(ell):
                y=x.copy();y[k+t]=n-j
                yield tuple(y)


def sqdist(x,c):return sum((F(a)-b)**2 for a,b in zip(x,c))

def expected(n,k,x):
    ell=n-k
    a=x[:k];b=x[k:]
    if ell==1:return (all(v==0 for v in b) and all(t in (0,1) for t in a)) or (all(v==0 for v in a) and b==(n,))
    if ell==2:return (a==(1,)*k and b==(0,0)) or (a==(0,)*k and sorted(b)==[0,n])
    return a==(0,)*k and sorted(b)==[0]*(ell-1)+[n]

checks=0
cases=0
vertices=0
for n in range(3,12):
    for k in range(1,n):
        cases+=1
        c,R2,expected_count,w=construction(n,k)
        assert sum((wt for _,wt in w),F(0))==1;checks+=1
        for i in range(n):
            assert sum((F(v[i])*wt for v,wt in w),F(0))==c[i];checks+=1
        for v,wt in w:
            assert wt>0;checks+=1
            assert sqdist(v,c)==R2;checks+=1
        cnt=0
        for x in verts(n,k):
            vertices+=1
            d=sqdist(x,c)
            assert d<=R2,(n,k,x,d,R2);checks+=1
            contact=(d==R2)
            assert contact==expected(n,k,x),(n,k,x,d,R2);checks+=1
            cnt+=contact
        assert cnt==expected_count,(n,k,cnt,expected_count);checks+=1
        if n-k==2:
            D=n*n+2*n-4
            assert R2 == F((n-1)**2*(n+2)**2,2*D);checks+=1
        if n-k==1:
            assert R2 == F(n*n+n-1,4);checks+=1

# Larger dimensions: exact orbit-endpoint inequalities without enumerating 2**k vertices.
for n in range(12,151):
    for k in range(1,n):
        ell=n-k;c,R2,_,_=construction(n,k)
        a=c[0];b=c[k]
        for j in range(k+1):
            dc=k*a*a+j*(1-2*a)+ell*b*b
            ds=dc+(n-j)**2-2*b*(n-j)
            assert dc<=R2 and ds<=R2,(n,k,j);checks+=2
            if ell==1:
                assert (dc==R2) and (ds==R2 if j==0 else ds<R2);checks+=1
            elif ell==2:
                assert (dc==R2 if j==k else dc<R2);checks+=1
                assert (ds==R2 if j==0 else ds<R2);checks+=1
            else:
                assert dc<R2;checks+=1
                assert (ds==R2 if j==0 else ds<R2);checks+=1

print('PASS cases',cases,'enumerated_vertices',vertices,'exact_assertions',checks)
