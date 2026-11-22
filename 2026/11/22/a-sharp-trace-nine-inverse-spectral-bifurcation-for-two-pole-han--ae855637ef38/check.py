"""Arithmetic and finite-section checks for the equal-mass two-pole Hankel theorem.

Requires only Python 3.10+ standard library. The infinite-dimensional
assertion and global inverse classification are proved analytically in RESULT.md.
"""
from fractions import Fraction
from math import sqrt


def d_from_trace_product(t, p):
    return (t - 2 - t*p) / ((1-p)**2 * (1+p))


# Exact-rational algebra for 1224 pairs, including the zero pole.
checks = 0
for i in range(0, 48):
    for j in range(i+1, 50):
        a, b = Fraction(i, 60), Fraction(j, 60)
        t = 1/(1-a*a) + 1/(1-b*b)
        d = 1/((1-a*a)*(1-b*b)) - 1/(1-a*b)**2
        assert d == d_from_trace_product(t, a*b)
        q = (t-2+t*(a*b)**2)/(t-1)
        assert q == a*a+b*b
        assert (q*q-4*(a*b)**2) == ((1-(a*b)**2)*((t-2)**2-t*t*(a*b)**2))/(t-1)**2
        checks += 3


def bisect_root(f, left, right):
    fa = f(left)
    fb = f(right)
    assert fa*fb < 0
    for _ in range(100):
        mid = (left+right)/2
        if f(mid)*fa > 0:
            left, fa = mid, f(mid)
        else:
            right, fb = mid, f(mid)
    return (left+right)/2


# A single exact-target spectral fiber with three distinct pole pairs.
t = 12.0
d = 199.0 / 20.0
pmin = (t-3-sqrt((t-1)*(t-9)))/(2*t)
pmax = (t-3+sqrt((t-1)*(t-9)))/(2*t)
upper = (t-2)/t
f = lambda p: d_from_trace_product(t,p)-d
roots = [bisect_root(f,lo,hi) for lo,hi in ((0,pmin),(pmin,pmax),(pmax,upper))]
assert 0 < roots[0] < pmin < roots[1] < pmax < roots[2] < upper
pairs=[]
for p in roots:
    q=(t-2+t*p*p)/(t-1)
    delta=sqrt(q*q-4*p*p)
    a=sqrt((q-delta)/2)
    b=sqrt((q+delta)/2)
    assert 0 <= a < b < 1
    tt=1/(1-a*a)+1/(1-b*b)
    dd=1/((1-a*a)*(1-b*b))-1/(1-a*b)**2
    assert abs(tt-t)<1e-10 and abs(dd-d)<1e-10
    pairs.append((a,b))
    checks+=4

# Check the finite Hankel Gram reductions (not a proof of any infinite limit).
for a,b in pairs:
    for n in (3, 10, 100, 300):
        tr=(1-a**(2*n))/(1-a*a)+(1-b**(2*n))/(1-b*b)
        cross=(1-(a*b)**n)/(1-a*b)
        dn=((1-a**(2*n))/(1-a*a))*((1-b**(2*n))/(1-b*b))-cross**2
        assert tr > 0 and dn > -1e-10
        if n==300:
            assert abs(tr-t)<1e-8 and abs(dn-d)<1e-8
        checks+=2

print('PASS',checks,'assertions; three distinct pairs for T=12 and determinant=199/20:')
for a,b in pairs:
    print('a=%.12f b=%.12f' % (a,b))
