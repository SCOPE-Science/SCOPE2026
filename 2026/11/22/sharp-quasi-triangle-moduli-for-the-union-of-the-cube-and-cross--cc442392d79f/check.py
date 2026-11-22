"""Exact-rational finite diagnostics for the sharp quasi-triangle modulus.
No third-party dependencies. This does not replace the all-dimensional proof.
"""
from fractions import Fraction as F
from itertools import product
from random import Random

def q(x,t):
    a=[abs(z) for z in x]
    return min(sum(a),t*max(a))

def h(x,t):
    a=sorted((abs(z) for z in x),reverse=True)
    n=len(a)
    if t<=1: return t*a[0]
    if t>=n: return sum(a)
    k=int(t)
    return sum(a[:k])+(t-k)*a[k]

def K(n,t):
    if t<=1 or t>=n:return F(1)
    return t*(n-1)/((n-1)+(t-1)**2)

rng=Random(22054)
count=0
for n in range(2,9):
    ts=[F(1,2),F(1),F(11,10),F(n+1,2),F(2*n-1,2),F(n),F(n+1)]
    for t in ts:
        t=F(t)
        kk=K(n,t)
        if F(1)<t<n:
            c=(t-1)/(n-1)
            u=[F(1)-c]+[F(0)]*(n-1)
            v=[c]*n
            w=[a+b for a,b in zip(u,v)]
            assert q(w,t)==kk*(q(u,t)+q(v,t))
            count+=1
        for _ in range(450):
            x=[F(rng.randrange(-15,16),rng.randrange(1,9)) for _ in range(n)]
            y=[F(rng.randrange(-15,16),rng.randrange(1,9)) for _ in range(n)]
            z=[a+b for a,b in zip(x,y)]
            assert q(z,t)<=kk*(q(x,t)+q(y,t))
            assert h(x,t)<=q(x,t)
            assert q(x,t)<=kk*h(x,t)
            assert h(z,t)<=h(x,t)+h(y,t)
            count+=4
print('QUASINORM_CUBE_CROSSPOLYTOPE_CHECK_OK',count)
