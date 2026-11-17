#!/usr/bin/env python3
"""Exact finite prime-field verification of the three consecutive NS-cube theorem."""
from math import isqrt
BOUND = 106000
EXPECTED = [7,13,19,31,37,43,61,67,73,79,97,103,109,127,157,163,229,277,283,409,421,457,487,577,601,727,733,1399]

def primes_below(n):
    sieve=bytearray(b'\x01')*n
    sieve[:2]=b'\x00\x00'
    for p in range(2,isqrt(n-1)+1):
        if sieve[p]: sieve[p*p:n:p]=b'\x00'*len(sieve[p*p:n:p])
    return [p for p in range(n) if sieve[p]]

def factors(n):
    out=[];d=2
    while d*d<=n:
        if n%d==0:
            out.append(d)
            while n%d==0: n//=d
        d+=1
    if n>1: out.append(n)
    return out

def primitive_root(p):
    fac=factors(p-1)
    for g in range(2,p):
        if all(pow(g,(p-1)//q,p)!=1 for q in fac): return g
    raise ArithmeticError('no generator')

def has_triple(p):
    g=primitive_root(p)
    first=pow(g,3,p);mult=pow(g,6,p)
    seen=bytearray(p);x=first
    for j in range((p-1)//6):
        assert not seen[x]
        seen[x]=1;x=x*mult%p
    assert x==first
    for a in range(1,p-2):
        if seen[a] and seen[a+1] and seen[a+2]: return True,a
    return False,None

def direct_is_ns_cube(p,x):
    return x%p!=0 and pow(x,(p-1)//2,p)==p-1 and pow(x,(p-1)//3,p)==1

ps=[p for p in primes_below(BOUND) if p%6==1]
exceptions=[];witnesses={}
for p in ps:
    ok,a=has_triple(p)
    if not ok: exceptions.append(p)
    else: witnesses[p]=a
assert exceptions==EXPECTED,(exceptions,EXPECTED)
for p in ps[:40]+ps[-40:]+[1399,1409,1429]:
    if p not in ps:continue
    ok,a=has_triple(p)
    if ok: assert all(direct_is_ns_cube(p,a+i) for i in range(3))
    else: assert not any(all(direct_is_ns_cube(p,a+i) for i in range(3)) for a in range(1,p-2))
assert 106000-325*(106000**0.5)-108>0
print('VERIFY_OK bound=',BOUND,'eligible_primes=',len(ps),'exceptions=',exceptions,'largest_exception=',max(exceptions),'witness_1409=',witnesses.get(1409))
