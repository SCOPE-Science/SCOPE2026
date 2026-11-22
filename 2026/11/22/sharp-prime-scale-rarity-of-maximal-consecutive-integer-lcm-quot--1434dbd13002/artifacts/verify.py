#!/usr/bin/env python3
"""Exact local and full-period checks for extremal consecutive LCM quotients."""
import math

def primes(n):
    s=bytearray(b'\x01')*(n+1)
    s[:2]=b'\x00\x00'
    for p in range(2,math.isqrt(n)+1):
        if s[p]:s[p*p::p]=b'\x00'*(((n-p*p)//p)+1)
    return [p for p in range(n+1) if s[p]]

def local(k,p):
    pe=1;e=0
    while pe*p<=k:pe*=p;e+=1
    m=k+1;digits=[]
    for _ in range(e):digits.append(m%p);m//=p
    t=next((i for i,z in enumerate(digits) if z),e)
    if t==e:return pe,pe
    h=p**t*digits[t]
    for i in range(t+1,e):h*=digits[i]+1
    return pe,h

def quotient(k,n):
    a=list(range(n,n+k+1))
    return math.prod(a)//math.lcm(*a)

local_checks=0
for k in range(2,300):
    for p in primes(k):
        pe,h=local(k,p)
        e=0;u=pe
        while u>1:e+=1;u//=p
        valmax=sum(k//(p**j) for j in range(1,e+1))
        direct=0
        for n in range(1,pe+1):
            exponent=0
            for j in range(1,e+1):
                q=p**j
                exponent+=sum((n+i)%q==0 for i in range(k+1))-1
            direct+=int(exponent==valmax)
        assert h==direct,(k,p,h,direct)
        local_checks+=1
full_checks=0
for k in range(2,13):
    L=math.lcm(*range(1,k+1))
    exact=math.prod(local(k,p)[1] for p in primes(k))
    observed=sum(quotient(k,n)==math.factorial(k) for n in range(1,L+1))
    assert exact==observed,(k,exact,observed)
    full_checks+=1

# Independent prime sieve and approximate large-window log-frequency values.
pp=primes(1000000)
for k in (1000,10000,100000,1000000):
    logd=sum(math.log(h/q) for p in pp if p<=k for q,h in (local(k,p),))
    measured=-logd*math.log(k)/k
    assert 1.25<measured<1.50
    print('k=%d scaled_negative_log_density=%.9f'%(k,measured))
print('EXTREMAL_LCM_CHECK_OK local_pairs=%d full_period_windows=%d'%(local_checks,full_checks))
