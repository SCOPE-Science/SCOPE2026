#!/usr/bin/env python3
"""Independent exact polynomial checks for quadric-cycle intersection cohomology.

Finite arithmetic checks only; the geometric assertions require the proof.
"""
from functools import lru_cache
from math import comb

@lru_cache(maxsize=None)
def gaussian(N, k):
    assert 0 <= k <= N
    if k == 0 or k == N:
        return (1,)
    a = gaussian(N-1, k)
    b = gaussian(N-1, k-1)
    offset = N-k
    out = [0]*max(len(a), len(b)+offset)
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i+offset] += value
    return tuple(out)

def poly_mul(a,b):
    out = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j] += x*y
    return out

def data(p,n):
    assert 1 <= p < n
    k = p+1
    b = comb(k+2,2)-1
    dimension = (k+1)*(n-k)+b
    codim = dimension - k*(n+1-k)
    r = n-k
    assert codim == n+comb(k,2)
    wall = 2*k+comb(k,2)
    y = poly_mul(gaussian(n+1,k+1),[1]*(b+1))
    assert len(y) == dimension+1
    assert sum(y)==comb(n+1,k+1)*(b+1)
    assert (2*r<codim) == (n<wall)
    assert (2*r<=codim) == (n<=wall)
    if n>wall:
        return None
    ih = y[:]
    if n==wall:
        correction = gaussian(n+1,k)
        for i,v in enumerate(correction):
            ih[i+r] -= v
        assert sum(ih)==sum(y)-comb(n+1,k)
    assert len(ih)==dimension+1
    assert ih[0] == ih[-1] == 1
    assert ih == ih[::-1]
    assert all(x>=0 for x in ih)
    return ih

assert data(1,3)==[1,2,3,4,4,4,3,2,1]
assert data(1,4)==[1,2,4,6,8,9,9,8,6,4,2,1]
assert data(1,5)==[1,2,4,6,9,11,13,13,13,11,9,6,4,2,1]
assert sum(data(1,5))==105
counts=0
for p in range(1,9):
    k=p+1
    wall=2*k+comb(k,2)
    for n in range(k,wall+1):
        data(p,n)
        counts+=1
print('Admissible small/semismall parameter pairs checked:', counts)
print('Plane-conic boundary:', data(1,5))
print('VERIFY_OK')
