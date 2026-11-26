#!/usr/bin/env python3
from math import comb


def primes_upto(n):
    sieve=[True]*(n+1)
    sieve[:2]=[False,False]
    for i in range(2,int(n**0.5)+1):
        if sieve[i]:
            sieve[i*i:n+1:i]=[False]*(((n-i*i)//i)+1)
    return [i for i,v in enumerate(sieve) if v]


def vp_fact(n,p):
    s=0
    while n:
        n//=p; s+=n
    return s

def vp_binom(n,k,p):
    return vp_fact(n,p)-vp_fact(k,p)-vp_fact(n-k,p)

def gcd_row_vp(N,m,p):
    return min(vp_binom(N,k,p) for k in range(m,N,m))

cases=0
coeff_checks=0
lower_checks=0
for m in range(2,81):
    for p in primes_upto(401):
        if p<=m: continue
        T=m*((p//m)+1)  # p is prime > m, hence m does not divide p
        # target row: every selected coefficient has valuation exactly one
        vals=[vp_binom(T,k,p) for k in range(m,T,m)]
        assert vals and set(vals)=={1}, (m,p,T,vals)
        coeff_checks += len(vals)
        assert gcd_row_vp(T,m,p)==1
        # all earlier admissible rows are below p and have valuation zero
        for N in range(2*m,T,m):
            assert N < p
            assert gcd_row_vp(N,m,p)==0, (m,p,N)
            lower_checks += 1
        # independent formula check through direct exact binomial divisibility on small subrange
        if m<=14 and p<=79:
            for k in range(m,T,m):
                b=comb(T,k)
                assert b%p==0 and b%(p*p)!=0
        cases += 1
print(f'VERIFY_OK cases={cases} target_coefficients={coeff_checks} lower_rows={lower_checks} m_max=80 p_max=401')
