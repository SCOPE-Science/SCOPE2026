#!/usr/bin/env python3
"""Exact finite checks for the odd nonsquare abundant signed-divisor obstruction.
Finite tests corroborate the written symbolic proof, not density or infinite validity.
"""
from math import prod, isqrt

def sigma_from_factor(f):
    return prod(sum(p**j for j in range(e+1)) for p,e in f.items())

def divisors(f):
    z=[1]
    for p,e in f.items(): z=[d*p**j for d in z for j in range(e+1)]
    return sorted(z)

def prime(n):
    if n<2:return False
    for d in range(2,isqrt(n)+1):
        if n%d==0:return False
    return True

def next_prime(n):
    n+=1
    while not prime(n):n+=1
    return n

a=3**2*5**2*7**2
fa={3:2,5:2,7:2}
sa=sigma_from_factor(fa)
delta=sa-2*a
assert (a,sa,delta)==(11025,22971,921)
print('CORE_OK a=11025 sigma=22971 delta=921')

ps=[next_prime(n) for n in (sa,sa+100,50000,100000,200000,300000)]
assert len(set(ps))==len(ps)
examples=[({ps[0]:1},'single prime'),({ps[2]:1,ps[4]:1},'two primes'),({ps[3]:1,ps[4]:1,ps[5]:1},'three primes'),({ps[4]:2,ps[5]:1},'repeated prime factor')]
for fm,desc in examples:
    m=prod(p**e for p,e in fm.items())
    sm=sigma_from_factor(fm)
    assert m%2==1 and any(e%2 for e in fm.values())
    E=sa*(sm-m)
    assert E<m,(desc,E,m)
    fn={**fa,**fm}
    n=a*m
    sn=sigma_from_factor(fn)
    assert sn==sa*sm and sn>2*n
    H=(sn-2*n)//2
    q=(delta-1)//2
    assert q*m+E < H <(q+1)*m
    divs=divisors(fn)
    assert divs[-1]==n and sum(divs)==sn
    low=[d for d in divs[1:-1] if d%m !=0]
    assert sum(low)<=E
    print('OBSTRUCTION_OK',desc,'m=',m,'count_divisors=',len(divs),'offset=',E,'gap_verified=True')
print('FINITE_CERTIFICATES_OK density_uses_symbolic_sieve=True independent_audit=False')
