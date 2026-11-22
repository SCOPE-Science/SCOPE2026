#!/usr/bin/env python3
"""Finite sanity checks for a closed-window toral Fourier construction.
The analytic theorem is proved in RESULT.md, not by this finite checker.
"""
import itertools, math
from mpmath import mp
mp.dps = 65
phi=(1+mp.sqrt(5))/2
chi=mp.log(phi*phi)
M=((2,1),(1,1))
def matmul(v):return (2*v[0]+v[1],v[0]+v[1])
def invmul(v):return (v[0]-v[1],-v[0]+2*v[1])
def power(v,n):
    for _ in range(abs(n)):v=(matmul if n>=0 else invmul)(v)
    return v
def L(v):
    a=mp.mpf(v[0])+mp.mpf(v[1])/phi
    b=phi*mp.mpf(v[1])-mp.mpf(v[0])
    assert a!=0 and b!=0
    return mp.log(abs(a/b))
p=4;w0=(1,3)
beta=mp.exp(p*chi);eta=mp.log(beta/(beta-2))
res=(L(w0)%(2*chi))
d=min(res-chi,2*chi-res)
assert beta>3 and eta<d
w={j:power(w0,p*j) for j in range(-3,4)}
seen=set();tested=0
for digits in itertools.product((-1,0,1),repeat=7):
    v=(sum(digits[j+3]*w[j][0] for j in range(-3,4)),sum(digits[j+3]*w[j][1] for j in range(-3,4)))
    assert v not in seen
    seen.add(v)
    if v==(0,0):assert not any(digits);continue
    active=[j for j in range(-3,4) if digits[j+3]]
    err=abs(L(v)-L(w0)-p*chi*(min(active)+max(active)))
    assert err<=eta+mp.mpf('1e-55'),(v,err,eta)
    assert not (0<=L(v)<=chi)
    for m in range(4):
        r=L(power(v,-m))
        assert not(0<=r<=chi)
    tested+=1
assert tested==2186
print('PASS: 2186 nonzero unique signed-frequency combinations; spectral window avoided across four cyclic phases.')
