#!/usr/bin/env python3
"""Numerical spectral tests and exact stationary-fiber counts for the stated theorem."""
from math import gcd
import cmath
import numpy as np

def predict(p):
    if p % 4 == 3:
        return (p - 1) ** 2 // 4
    return (p - 1) * (p + 3) // 8 if p % 8 == 1 else (p - 1) ** 2 // 8

def build(p, c=1):
    n=p*p
    units=[v for v in range(1,n) if v%p]
    q=sorted({v*v % n for v in units})
    assert len(q)==p*(p-1)//2
    inv={x: pow(x,-1,n) for x in q}
    M=np.empty((len(q),len(q)),dtype=complex)
    for i,x in enumerate(q):
        for j,y in enumerate(q):
            z=(x*y)%n
            M[i,j]=cmath.exp(2j*cmath.pi*(c*(z+inv[z])%n)/n)
    return q,M

for p in [3,5,7,11,13]:
    n=p*p
    sq={x*x%p for x in range(1,p)}
    values={ (x-pow(x,-1,p))%p for x in sq }
    assert len(values)*(p-1)//2 == predict(p)
    for c in (1,2):
        if c%p==0: continue
        pts,M=build(p,c)
        s=np.linalg.svd(M,compute_uv=False)
        r=int(np.sum(s>1e-7))
        assert r==predict(p),(p,c,r,predict(p))
        assert (len(s)-r)==len(pts)-predict(p)
        if p%4==3:
            assert np.max(abs(s[:r]-p))<1e-7
        print('PASS',p,c,'size',len(pts),'rank',r,
              'largest',round(float(s[0]),9),'smallest_nonzero',round(float(s[r-1]),9))
for p in [17,19,23,29,31,37,41]:
    sq={x*x%p for x in range(1,p)}
    values={(x-pow(x,-1,p))%p for x in sq}
    assert len(values)*(p-1)//2 == predict(p)
    print('PASS exact map',p,'rank',predict(p))
print('SQUARE_UNIT_HYPERBOLA_RANK_PASS')
