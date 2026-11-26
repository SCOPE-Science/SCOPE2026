#!/usr/bin/env python3
"""Check joint-rank counts for commuting square-zero maps in even dimension.
Uses direct finite matrix arithmetic and row reduction; no symbolic normal-form count in enumeration.
"""
from itertools import product
from collections import Counter
from math import prod

def ops(q):
    if q in (2,3):
        return lambda a,b:(a+b)%q,lambda a,b:(a*b)%q
    if q==4:  # F2[z]/(z^2+z+1), integers 0,1,z,z+1
        def mul(a,b):
            r=0
            if b&1:r^=a
            if b&2:r^=(a<<1)
            if r&4:r^=0b111   # z^2=z+1
            return r
        return lambda a,b:a^b,mul
    raise ValueError(q)

def mm(A,B,add,mul):
    n=len(A);return [[reduce_add((mul(A[i][k],B[k][j]) for k in range(n)),add) for j in range(n)] for i in range(n)]
def reduce_add(vals,add):
    out=0
    for v in vals:out=add(out,v)
    return out

def rank(M,q,add,mul):
    if not M:return 0
    a=[list(row) for row in M];m=len(a);n=len(a[0]);z=0
    for j in range(n):
        piv=next((i for i in range(z,m) if a[i][j]),None)
        if piv is None:continue
        a[z],a[piv]=a[piv],a[z]
        v=a[z][j]
        inv=next(w for w in range(1,q) if mul(v,w)==1)
        a[z]=[mul(v0,inv) for v0 in a[z]]
        for i in range(m):
            if i==z or not a[i][j]:continue
            fac=a[i][j]
            a[i]=[add(a[i][t],mul((-fac)%q if q==3 else fac,a[z][t])) for t in range(n)]
        z+=1
    return z

def gaussian(n,k,q):
    if k==0:return 1
    return prod(q**n-q**i for i in range(k))//prod(q**k-q**i for i in range(k))
def full_rank(n,q):return prod(q**n-q**i for i in range(n))
def matrix_rank_count(n,k,q):
    if k==0:return 1
    return gaussian(n,k,q)*prod(q**n-q**i for i in range(k))
def formula(q,r):
    out=Counter()
    for k in range(r//2+1):
        s=r-2*k
        P_count=gaussian(r,k,q)*gaussian(r-k,k,q)*full_rank(k,q)
        for h in range(s+1):
            out[(k,2*k+h)]=P_count*q**(2*k*(r-k))*matrix_rank_count(s,h,q)
    return out

def directly_count(q,r):
    add,mul=ops(q);out=Counter();ps=0
    for p in product(range(q),repeat=r*r):
        P=[p[i*r:(i+1)*r] for i in range(r)]
        if any(x for row in mm(P,P,add,mul) for x in row):continue
        ps+=1
        k=rank(P,q,add,mul)
        for y in product(range(q),repeat=r*r):
            Y=[y[i*r:(i+1)*r] for i in range(r)]
            PY=mm(P,Y,add,mul);YP=mm(Y,P,add,mul)
            if any(add(PY[i][j],YP[i][j]) for i in range(r) for j in range(r)):continue
            B=[list(P[i])+list(Y[i]) for i in range(r)]+[[0]*r+list(P[i]) for i in range(r)]
            assert not any(x for row in mm(B,B,add,mul) for x in row)
            A=[[int(j==i+r) for j in range(2*r)] for i in range(2*r)]
            assert mm(A,B,add,mul)==mm(B,A,add,mul)
            assert rank(mm(A,B,add,mul),q,add,mul)==k
            out[(k,rank(B,q,add,mul))]+=1
    return out,ps

if __name__=='__main__':
    for q,r in [(2,1),(2,2),(3,2),(4,2),(2,3)]:
        observed,ps=directly_count(q,r)
        expected=formula(q,r)
        assert observed==expected,(q,r,observed,expected)
        print(f'OK q={q} r={r} squarezero_P={ps} qualifying_B={sum(observed.values())} joint={dict(sorted(observed.items()))}')
    print('VERIFY_OK')
