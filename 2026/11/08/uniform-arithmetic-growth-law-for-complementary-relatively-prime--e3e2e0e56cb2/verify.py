#!/usr/bin/env python3
"""Independent exact-integer check of the complementary subset-ratio sandwich."""
from math import gcd

N=400
mu=[1]*(N+1)
mu[0]=0
for p in range(2,N+1):
    if any(p%d==0 for d in range(2,int(p**0.5)+1)):
        continue
    for k in range(p,N+1,p):mu[k]*=-1
    for k in range(p*p,N+1,p*p):mu[k]=0
f=[0]*(N+1)
for m in range(1,N+1):
    f[m]=sum(mu[d]*((1<<(m//d))-1) for d in range(1,m+1))
    assert 1<<(m-1)<=f[m]<1<<m

# An independent direct subset enumeration for the base counting function.
for m in range(1,14):
    exact=0
    for mask in range(1,1<<m):
        g=0
        for j in range(m):
            if (mask>>j)&1:g=gcd(g,j+1)
        if g==1:exact+=1
    assert exact==f[m],(m,exact,f[m])

for n in range(4,N+1):
    a=next(g for g in range(2,n) if n%g)
    p=next(g for g in range(2,n+1) if n%g==0)
    A=1+sum(f[n//g] for g in range(2,n+1) if n%g!=0)
    B=1+sum(f[n//g] for g in range(2,n+1) if gcd(g,n)>1)
    D=sum(f[d] for d in range(1,n+1) if n%d==0)
    Phi=sum(mu[d]*((1<<(n//d))-1) for d in range(1,n+1) if n%d==0)
    assert A==(1<<n)-D and B==(1<<n)-Phi
    ha, hp=n//a,n//p
    assert 2*(n+1)*A*(1<<hp)>=B*(1<<ha)
    assert A*(1<<hp)<=2*(n+1)*B*(1<<ha)
    if n%2==0:assert a>=3 and p==2
    else:assert a==2 and p>=3
print('VERIFY_OK direct_subset_n=1..13; complement_and_sandwich_n=4..400; exact_integer_only')
