#!/usr/bin/env python3
"""Finite diagnostic consistency checks for a geometric exponential perpetuity.
Requires mpmath. All infinite identities are established analytically in RESULT.md.
"""
import mpmath as mp
mp.mp.dps=50
q=mp.mpf('0.5'); p=mp.mpf('0.4'); h=mp.log(2); kap=-mp.log(p)/h

def prod(a, n=120):
    z=mp.mpf(1)
    for j in range(n): z*=1-a*q**j
    return z
Q=prod(q)
def tail_infinite(x):
    if x<=0:return mp.mpf(1)
    s=mp.mpf(0);d=mp.mpf(1)
    for j in range(25):
        if j:d*=1-q**j
        s+=(-1)**j*q**(j*(j+1)//2)*mp.exp(-q**(-j)*x)/d
    return s/Q

def tail_finite(n,x):
    s=mp.mpf(0);d=mp.mpf(1)
    for j in range(n+1):
        if j:d*=1-q**j
        back=mp.mpf(1)
        for r in range(1,n-j+1):back*=1-q**r
        s+=(-1)**j*q**(j*(j+1)//2)*mp.exp(-q**(-j)*x)/d/back
    return s

def phase(x):
    return (1-p)*sum(p**j*tail_infinite(mp.power(2,-j)*x) for j in range(-22,125))

def exact_tail(x):
    return (1-p)*sum(p**n*tail_finite(n,x*q**n) for n in range(95))

checks=0
for n in range(8):
    for s in (mp.mpf('.1'),mp.mpf('.3'),mp.mpf('1.2')):
        rhs=mp.mpf(1)
        for j in range(n+1):rhs/=(1+s*q**j)
        # sum of finite-mixture Laplace transforms from the residues
        lhs=mp.mpf(0);den=mp.mpf(1)
        for j in range(n+1):
            if j:den*=1-q**j
            back=mp.mpf(1)
            for r in range(1,n-j+1):back*=1-q**r
            a=(-1)**j*q**(j*(j+1)//2)/den/back
            lhs+=a/(1+s*q**j)
        assert abs(lhs-rhs)<mp.mpf('1e-38')
        checks+=1
for x in (mp.mpf('.8'),mp.mpf('1'),mp.mpf('1.3'),mp.mpf('1.8'),mp.mpf('2.4')):
    lhs=x**kap*phase(x)
    assert abs(lhs-(2*x)**kap*phase(2*x))<mp.mpf('1e-38')
    checks+=1
    for m in (7,12,17):
        ratio=exact_tail(mp.power(2,m)*x)/(p**m*phase(x))
        assert abs(ratio-1)<mp.mpf('.03')
        if m==17:assert abs(ratio-1)<mp.mpf('.00005')
        checks+=1
c0=(1-p)/h*prod(q**(kap+1))/Q*mp.gamma(kap)
c1=(1-p)/h*prod(q**(kap+1))/Q*mp.gamma(kap-2*mp.pi*1j/h)
assert abs(c1)>mp.mpf('1e-7');checks+=1
for x in (mp.mpf('1'),mp.mpf('1.3'),mp.mpf('1.8')):
    t=mp.log(x)
    harmonic=(1-p)/h*prod(q**(kap+1))/Q*sum(mp.gamma(kap-2*mp.pi*1j*j/h)*mp.exp(2*mp.pi*1j*j*t/h) for j in range(-8,9))
    assert abs(mp.re(harmonic)-x**kap*phase(x))<mp.mpf('1e-25')
    checks+=1
print('PASS:',checks,'finite high-precision diagnostics; no infinite theorem certified by numerics')
