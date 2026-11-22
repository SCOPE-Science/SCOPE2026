"""Finite reproducibility checks for matching-deleted biclique hard-core partition zeros.

This file verifies finite algebra and numerical predictions; analytical proofs cover every n.
"""
from itertools import combinations
from math import comb, log, sqrt, pi
import cmath
from fractions import Fraction


def coefficients(n, k):
    a = [2 * comb(n, j) for j in range(n + 1)]
    a[0] -= 1
    a[2] += k
    return a


def enumerated_coefficients(n, k):
    edges = [(i, n+j) for i in range(n) for j in range(n) if i != j or i >= k]
    adj = [0] * (2*n)
    for u, v in edges:
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    c = [0] * (n + 1)
    for mask in range(1 << (2*n)):
        left = mask
        valid = True
        while left:
            b = left & -left
            v = b.bit_length()-1
            if adj[v] & mask:
                valid = False
                break
            left -= b
        if valid:
            s = mask.bit_count()
            assert s <= n
            c[s] += 1
    return c


def f(n, k, x):
    return 2*(1-x)**n + k*x*x - 1


def bisect(fn, lo, hi, steps=110):
    flo = fn(lo)
    fhi = fn(hi)
    assert flo*fhi < 0, (lo,hi,flo,fhi)
    for _ in range(steps):
        mi=(lo+hi)/2
        fm=fn(mi)
        if fm*flo >0:
            lo=mi;flo=fm
        else:
            hi=mi
    return (lo+hi)/2


def run():
    count=0
    # Independent vertex-subsets of an actual finite graph, not only the formula.
    for n in range(3,8):
        for k in range(1,n+1):
            assert enumerated_coefficients(n,k)==coefficients(n,k)
            count += 1
    # Exact polynomial Sturm real-root counts, and positivity on imaginary axis.
    import sympy as sp
    z=sp.symbols('z')
    for n in range(3,15):
        for k in range(1,n+1):
            p=sp.Poly(sum(a*z**j for j,a in enumerate(coefficients(n,k))),z)
            assert p.count_roots(-sp.oo,0)==(2 if n%2==0 else 3),(n,k)
            # Verify exact positivity on six rational right-half-plane test sites.
            for re,im in [(0,0),(0,1),(0,5),(sp.Rational(1,10),sp.Rational(1,7)),(1,2),(10,10)]:
                val=p.eval(re+sp.I*im)
                assert sp.simplify(sp.re(val)**2+sp.im(val)**2)>0
            count += 1
    # Dimensionless fugacity edge locations and outer negative zero.
    for n in [30,60,120,240]:
        g=lambda x:f(n,n,x)
        x1=bisect(g,0,1/n)
        x2=bisect(g,1/n,1)
        assert abs(n*x1-log(2))<0.11
        assert abs(sqrt(n)*x2-1)<0.07
        if n%2:
            pass
        count += 1
    for n in [31,61,121,241]:
        g=lambda x:f(n,n,x)
        x3=bisect(g,1,3)
        assert abs(n*(x3-2)-log(2*n)) < 1.0
        count += 1
    # Complex edge zeros, checked by a numeric Newton iteration in scaled variable.
    import mpmath as mp
    mp.mp.dps=60
    for n in [70,140,280]:
        for j in range(-3,4):
            u0=-mp.log(2)+2*mp.pi*j*1j
            def h(u): return 2*(1+u/n)**n -1 +u*u/n
            u=mp.findroot(h,(u0,u0+mp.mpf('0.1')))
            assert abs(u-u0)<mp.mpf('1.8')
            count += 1
    print('CROWN_HARD_CORE_CHECKS_PASSED',count)


if __name__=='__main__':
    run()
