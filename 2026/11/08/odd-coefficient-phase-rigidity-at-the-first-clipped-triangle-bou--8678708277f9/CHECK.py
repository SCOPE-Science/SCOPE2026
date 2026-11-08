#!/usr/bin/env python3
"""Exact aperiodic checks for clipped triangular Fourier apertures."""
from collections import Counter

def T(n):
    return [(i,j) for i in range(n) for j in range(n-i) if not (i==n-1 and j==0)]

def autocorr(f):
    out={}
    for (i,j),a in f.items():
        for (k,l),b in f.items():
            d=(i-k,j-l)
            out[d]=out.get(d,0)+a*b
    return tuple(sorted((d,v) for d,v in out.items() if v))

def convolution(A,B):
    C={}
    for (i,j),a in A.items():
        for (k,l),b in B.items():
            d=(i+k,j+l)
            C[d]=C.get(d,0)+a*b
    return C

# Every array modulo global sign, exact complete aperiodic autocorrelation.
for n in range(3,6):
    pts=T(n)
    seen=set()
    for bits in range(1<<(len(pts)-1)):
        f={pts[0]:1}
        f.update({p: (-1 if bits>>(k-1)&1 else 1) for k,p in enumerate(pts) if k})
        sig=autocorr(f)
        if sig in seen:
            raise AssertionError(('binary_collision',n,bits))
        seen.add(sig)
    assert len(seen)==1<<(len(pts)-1)
    print('binary',n,'unique',len(seen))

for n in range(3,7):
    A={(i,j):1 for i in range(n-1) for j in range(n-1-i)}
    plus=convolution(A,{(0,0):1,(0,1):2})
    minus=convolution(A,{(0,0):2,(0,1):1})
    assert set(plus)==set(minus)==set(T(n))
    assert all(v>0 for v in plus.values()) and all(v>0 for v in minus.values())
    assert autocorr(plus)==autocorr(minus)
    assert plus!=minus
    print('positive_integer_pair',n,'equal_autocorr')
print('ALL_CLIPPED_TRIANGLE_CHECKS_PASSED')
