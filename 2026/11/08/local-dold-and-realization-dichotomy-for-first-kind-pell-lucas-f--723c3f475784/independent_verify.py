#!/usr/bin/env python3
"""Independent finite test of the local Lucas Dold dichotomy and correction."""
from math import gcd

def prime_list(M):
    S=[True]*(M+1); S[:2]=[False,False]
    for i in range(2,int(M**0.5)+1):
        if S[i]:
            for j in range(i*i,M+1,i):S[j]=False
    return [i for i in range(M+1) if S[i]]

def mu_all(N):
    mu=[1]*(N+1); mu[0]=0
    for p in prime_list(N):
        for j in range(p,N+1,p):mu[j]*=-1
        for j in range(p*p,N+1,p*p):mu[j]=0
    return mu

M=180; ps=prime_list(71); mu=mu_all(M); count=0
for P in range(2,21):
    U=[0,1]
    for _ in range(2,M+1):U.append(P*U[-1]+U[-2])
    D=P*P+4
    for p in ps:
        v=[0]*(M+1)
        for n in range(1,M+1):
            y=U[n]
            while y%p==0:v[n]+=1;y//=p
        a=[0]+[p**v[n] for n in range(1,M+1)]
        T=[0]*(M+1)
        for d in range(1,M+1):
            for k in range(1,M//d+1):T[d*k]+=mu[k]*a[d]
        assert all(z>=0 for z in T[1:]),(P,p,'negative')
        if p==2:
            repair=3 if P&1 else 2
        else:
            rank=next(n for n in range(1,M+1) if U[n]%p==0)
            repair=rank//gcd(rank,p-1)
            char=0 if D%p==0 else (1 if pow(D%p,(p-1)//2,p)==1 else -1)
            assert (repair==1)==(char==1),(P,p,rank,repair,char)
        assert all(repair*T[n]%n==0 for n in range(1,M+1)),(P,p,repair)
        # independently check minimal multiplier as a finite lcm of reduced denominators
        from math import lcm
        finite=lcm(*(n//gcd(n,T[n]) for n in range(1,M+1)))
        # finite n may not yet contain the rank; only use equality when enough data
        if p==2 or (p%2 and rank*p<=M):assert finite==repair,(P,p,finite,repair)
        count+=1
print('INDEPENDENT_VERIFY_OK parameter_prime_pairs=',count, 'max_n=',M)
