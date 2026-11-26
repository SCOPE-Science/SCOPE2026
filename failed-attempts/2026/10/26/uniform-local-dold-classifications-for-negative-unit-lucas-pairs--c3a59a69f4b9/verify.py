#!/usr/bin/env python3
"""Exact consistency checks for a parameter-uniform Lucas local-Dold theorem.

The program does not establish the infinite statements or bibliographic novelty.
"""
from math import gcd


def primes_le(n):
    return [k for k in range(2,n+1) if all(k%d for d in range(2,int(k**0.5)+1))]


def val(x,p):
    if x==0:
        raise ValueError('zero has no finite p-adic order')
    v=0
    while x%p==0:
        x//=p
        v+=1
    return v


def sequences(P,N):
    u=[0,1];v=[2,P]
    for _ in range(2,N+1):
        u.append(P*u[-1]+u[-2])
        v.append(P*v[-1]+v[-2])
    return u,v


def rank_mod(P,p):
    a,b=0,1
    for n in range(1,2*p+3):
        a,b=b,(P*b+a)%p
        if a==0:
            return n
    raise AssertionError(('missing rank',P,p))


def forecast(P,p,n,U,V):
    D=P*P+4
    if p==2:
        if P%2:
            a=1 if n%3 else (2 if n%2 else 2**(val(n,2)+2))
            b=1 if n%3 else (4 if n%2 else 2)
            return a,b
        e=val(P,2)
        return (1 if n%2 else 2**(e+val(n,2)-1)), (2**e if n%2 else 2)
    if D%p==0:
        return p**val(n,p),1
    r=rank_mod(P,p)
    a=p**(val(U[r],p)+val(n//r,p)) if n%r==0 else 1
    if r%2==0:
        t=r//2
        b=p**(val(V[t],p)+val(n//t,p)) if (n%t==0 and (n//t)%2==1) else 1
    else:
        b=1
    return a,b


def mu_sieve(n):
    mu=[1]*(n+1);mu[0]=0
    pf=[0]*(n+1)
    for k in range(2,n+1):
        if not pf[k]:
            for j in range(k,n+1,k):
                if pf[j]==0:pf[j]=k
    for k in range(2,n+1):
        x=k;y=1
        while x>1:
            p=pf[x];x//=p
            if x%p==0:
                y=0;break
            y=-y
        mu[k]=y
    return mu


def mobius_transform(f,mu):
    N=len(f)-1; L=[0]*(N+1)
    for d in range(1,N+1):
        for m in range(1,N//d+1):
            L[d*m]+=mu[m]*f[d]
    return L


def expected_multipliers(P,p):
    if p==2:
        return (3,3) if P%2 else (2,1)
    if (P*P+4)%p==0:
        return p,1
    r=rank_mod(P,p)
    k=r//gcd(r,p-1)
    return k,(k if r%2==0 else 1)


def tests():
    N=200
    mu=mu_sieve(N)
    primes=primes_le(43)
    cases=0
    for P in range(1,21):
        U,V=sequences(P,N)
        for p in primes:
            aa=[0]+[p**val(U[n],p) for n in range(1,N+1)]
            bb=[0]+[p**val(V[n],p) for n in range(1,N+1)]
            fa=[0]+[forecast(P,p,n,U,V)[0] for n in range(1,N+1)]
            fb=[0]+[forecast(P,p,n,U,V)[1] for n in range(1,N+1)]
            assert aa==fa and bb==fb,('valuation',P,p)
            LA=mobius_transform(aa,mu)
            LB=mobius_transform(bb,mu)
            ku,kv=expected_multipliers(P,p)
            assert all(ku*LA[n]%n==0 and kv*LB[n]%n==0 for n in range(1,N+1)),('Dold repair',P,p)
            assert all(x>=0 for x in LA[1:]),('U sign',P,p)
            if p==2:
                expectU=False;expectV=(P%2==0)
            else:
                D=P*P+4
                chi=0 if D%p==0 else (1 if pow(D%p,(p-1)//2,p)==1 else -1)
                expectU=(chi==1)
                expectV=(chi>=0 or p%4==1)
            assert (ku==1)==expectU,('U criterion',P,p,ku,expectU)
            assert (kv==1)==expectV,('V criterion',P,p,kv,expectV)
            expect_negative=(any(b>1 for b in bb[1:]) and not (p==2 and P%4==2))
            assert (min(LB[1:])<0)==expect_negative,('V sign',P,p)
            # Exact minimality via lcm of denominators of Mobius transforms
            # (the finite range detects the listed multiplier except where
            # the necessary witness r*p lies beyond N).
            forced=1
            for n in range(1,N+1):
                d=n//gcd(n,LA[n])
                forced=forced*d//gcd(forced,d)
            assert ku%forced==0,('finite necessity',P,p)
            cases+=1
    print('VERIFY_OK parameter_prime_cases=%d max_index=%d  U_and_V_exact_valuations=PASS repair=PASS signs=PASS'%(cases,N))

if __name__=='__main__':tests()
