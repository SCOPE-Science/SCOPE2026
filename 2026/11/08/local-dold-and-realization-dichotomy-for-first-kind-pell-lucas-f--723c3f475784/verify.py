#!/usr/bin/env python3
"""Exact finite checks for local Dold status of U(P,-1)."""
from math import gcd

def primes(n):
    r=[]
    for k in range(2,n+1):
        if all(k%d for d in range(2,int(k**.5)+1)):
            r.append(k)
    return r

def vals(P,N):
    out=[0,1]
    for i in range(2,N+1):out.append(P*out[-1]+out[-2])
    return out

def vp(n,p):
    a=0
    while n and n%p==0:n//=p;a+=1
    return a

def mobius(n):
    m=n;k=0;d=2
    while d*d<=m:
        if m%d==0:
            m//=d;k+=1
            if m%d==0:return 0
        d+=1
    if m>1:k+=1
    return (-1)**k

def trans(a,n):
    return sum(mobius(n//d)*a[d] for d in range(1,n+1) if n%d==0)

def leg(a,p):
    if a%p==0:return 0
    return 1 if pow(a,(p-1)//2,p)==1 else -1

N=240; ps=primes(79); total=0; diffs=[]; reps=[]
for P in range(1,17):
    U=vals(P,N); a2=[0]+[2**vp(U[n],2) for n in range(1,N+1)]
    v=trans(a2,2)
    expected=3 if P%2 else 2
    # finite-repair, all n
    assert all(expected*trans(a2,n)%n==0 and trans(a2,n)>=0 for n in range(1,N+1))
    assert v%2!=0 if P%2==0 else trans(a2,3)%3!=0
    for p in ps[1:]:
        # odd p
        a=[0]+[p**vp(U[n],p) for n in range(1,N+1)]
        r=next((i for i in range(1,N+1) if U[i]%p==0),None)
        assert r is not None
        repair=r//gcd(r,p-1)
        for n in range(1,N+1):
            t=trans(a,n)
            assert t>=0,(P,p,n,t)
            assert repair*t%n==0,(P,p,r,repair,n,t)
            if t%n!=0 and repair==1:raise AssertionError((P,p,n,t))
        expectedgood=(leg(P*P+4,p)==1)
        assert (repair==1)==expectedgood,(P,p,r,repair,expectedgood)
        total+=1
        if (P,p) in [(1,5),(2,3),(2,5),(3,13),(4,5),(8,13)]:reps.append((P,p,r,repair,leg(P*P+4,p)))
print('VERIFY_OK odd_prime_pairs=',total,'length=',N,'even_parameters=',16)
print('SELECTED=',reps)
print('exact_mobius_transforms=yes minimal_repair_by_rank=yes signs_nonnegative=yes')
