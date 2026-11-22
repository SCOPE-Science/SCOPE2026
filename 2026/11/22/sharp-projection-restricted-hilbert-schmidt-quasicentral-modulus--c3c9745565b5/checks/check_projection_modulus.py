"""Finite diagnostics for an exact Hilbert--Schmidt projection theorem.

These checks do not certify an infinite-dimensional statement. Run with Python 3.
"""
import math
from fractions import Fraction


def mul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(x) for x in zip(*a)]


def hs2(a):
    return sum(x*x for row in a for x in row)


def subtract(a,b):
    return [[x-y for x,y in zip(ar,br)] for ar,br in zip(a,b)]


checks = 0
for n in (2,3,4,5):
    a = [[Fraction(((7*i + 11*j + 3*i*j) % 13)-6, 5)
          for j in range(n)] for i in range(n)]
    at = transpose(a)
    f = subtract(mul(at,a),mul(a,at))
    for rank in range(1,n):
        p = [[Fraction(int(i==j and i<rank)) for j in range(n)] for i in range(n)]
        comm = subtract(mul(a,p),mul(p,a))
        trpf = sum(f[i][i] for i in range(rank))
        outside = sum(a[i][j]**2 for i in range(rank,n) for j in range(rank))
        inside = sum(a[i][j]**2 for i in range(rank) for j in range(rank,n))
        assert hs2(comm) == outside+inside
        assert trpf == outside-inside
        assert hs2(comm) >= abs(trpf)
        checks += 3

prev=float('inf')
for m in range(1,17):
    n=2**m
    sinc=math.sin(math.pi/n)/(math.pi/n)
    energy=2*n*(1-sinc*sinc)
    assert 0<energy<prev
    if m>=8:
        assert abs(n*energy-2*math.pi*math.pi/3)<0.002
    prev=energy
    checks += 1
print('PROJECTION_QUASICENTRAL_DIAGNOSTIC_OK',checks)
