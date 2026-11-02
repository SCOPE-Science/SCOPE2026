#!/usr/bin/env python3
"""Exact reproducibility checks for subset-GCD parity comparison."""
from math import gcd

def mobius_sieve(n):
    mu=[1]*(n+1)
    for p in range(2,n+1):
        if any(p%d==0 for d in range(2, int(p**.5)+1)):
            continue
        for k in range(p,n+1,p): mu[k]*=-1
        for k in range(p*p,n+1,p*p): mu[k]=0
    return mu

def counts(bound):
    mu=mobius_sieve(bound)
    f=[0]*(bound+1)
    for n in range(1,bound+1):
        f[n]=sum(mu[d]*((1<<(n//d))-1) for d in range(1,n+1))
    D=[0]*(bound+1)
    Phi=[0]*(bound+1)
    for n in range(1,bound+1):
        D[n]=sum(f[n//d] for d in range(1,n+1) if n%d==0)
        Phi[n]=sum(f[n//g] for g in range(1,n+1) if gcd(g,n)==1)
        assert f[n]>=1<<(n-1) and f[n]<= (1<<n)-1
    return f,D,Phi

f,D,Phi=counts(240)
assert [(n,D[n]-Phi[n]) for n in [4,6,8,10,12,14]]==[(4,2),(6,7),(8,10),(10,22),(12,68),(14,103)]
assert [(n,Phi[n]-D[n]) for n in [5,7,9]]==[(5,3),(7,9),(9,10)]
assert all((D[n]-Phi[n])*(1 if n%2==0 else -1)>0 for n in range(4,241))
assert all(D[n]-Phi[n]==sum(((int(n%g==0))-(int(gcd(n,g)==1)))*f[n//g] for g in range(2,n+1)) for n in range(2,241))
# Distinct standalone enumeration for all nonempty subsets of {1,...,16}.
for n in range(1,17):
    bf=bd=bp=0
    for mask in range(1,1<<n):
        g=0
        for i in range(n):
            if mask>>i&1: g=gcd(g,i+1)
        bf+=(g==1)
        bd+=(n%g==0)
        bp+=(gcd(n,g)==1)
    assert (bf,bd,bp)==(f[n],D[n],Phi[n])
print('VERIFY_OK mobius_and_gcd_strata=240 brute_force_subsets_n1to16=131054 parity_cases=237')
