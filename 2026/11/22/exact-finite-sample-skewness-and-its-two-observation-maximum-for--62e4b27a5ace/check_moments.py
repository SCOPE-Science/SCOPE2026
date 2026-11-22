"""Exact rational checks for the null cubic moment of a uniformity statistic.

No third-party packages are required. Run with Python 3.9 or newer.
"""
from fractions import Fraction as F
from math import comb

VARS = 3

class Poly:
    def __init__(self, data):
        self.d = {k: F(v) for k, v in data.items() if v}
    @staticmethod
    def c(z):
        return Poly({(0, 0, 0): F(z)})
    @staticmethod
    def x(i):
        e = [0, 0, 0]; e[i] = 1
        return Poly({tuple(e): F(1)})
    def __add__(self, other):
        other = other if isinstance(other, Poly) else Poly.c(other)
        d = self.d.copy()
        for k, v in other.d.items():
            d[k] = d.get(k, F(0)) + v
        return Poly(d)
    __radd__ = __add__
    def __neg__(self):
        return Poly({k: -v for k, v in self.d.items()})
    def __sub__(self, other):
        return self + (-other if isinstance(other, Poly) else -F(other))
    def __rsub__(self, other):
        return other + (-self)
    def __mul__(self, other):
        other = other if isinstance(other, Poly) else Poly.c(other)
        d = {}
        for k, v in self.d.items():
            for l, w in other.d.items():
                idx = tuple(a + b for a, b in zip(k, l))
                d[idx] = d.get(idx, F(0)) + v * w
        return Poly(d)
    __rmul__ = __mul__
    def __truediv__(self, other):
        assert not isinstance(other, Poly)
        return self * (F(1) / F(other))
    def __pow__(self, n):
        z = Poly.c(1)
        for _ in range(n): z = z * self
        return z

def ordered_integral(p, d):
    """Integrate over 0<x0<...<x(d-1)<1, with remaining powers zero."""
    ans = F(0)
    for e, coef in p.d.items():
        assert all(v == 0 for v in e[d:])
        den = 1
        for j in range(d):
            den *= sum(e[:j+1]) + j + 1
        ans += coef / den
    return ans

u, v, w = (Poly.x(i) for i in range(3))

def J(x): return x*x/2 - x**3/3

def h(x,y,first_is_smaller=True):
    z = x if first_is_smaller else y
    return (2*x-1)*(2*y-1)*z-(2*x-1)*J(x)-(2*y-1)*J(y)+F(1,30)

def diag(x): return h(x,x)

def b(x): return diag(x)-F(2,15)

# Integral over paired order regions. Integrands are symmetric where multiplied by 2.
huv = h(u,v)
C0 = ordered_integral(b(u)**3, 1)
C1 = 2*ordered_integral(b(u)*b(v)*huv, 2)
C2 = ordered_integral((b(u)+b(v))*huv**2, 2)
C3 = 2*ordered_integral(huv**3, 2)
C4 = 6*ordered_integral(h(u,v)*h(u,w)*h(v,w), 3)
expected = [F(86677,13513500), F(15931,11583000), F(280583,121621500), F(225809,162162000), F(502883,324324000)]
assert [C0,C1,C2,C3,C4] == expected, (C0,C1,C2,C3,C4)
assert ordered_integral(diag(u),1) == F(2,15)
assert ordered_integral(b(u),1) == 0
assert ordered_integral(b(u)**2,1) == F(169,8100)
assert 2*ordered_integral(huv**2,2) == F(109,8100)

# Connected diagrams: (i) triple diagonal, (ii) two diagonal and one
# off-diagonal, (iii) diagonal with repeated edge, (iv) triple edge,
# (v) triangle of three distinct edges.
def third(n):
    assert n>=1
    k2=comb(n,2); k3=comb(n,3)
    return (n*C0 + 12*k2*C1 + 24*k2*C2 + 8*k2*C3 + 48*k3*C4)/n**3

def variance(n):
    return F(218*n-49,8100*n)

def claimed_third(n):
    return F(502883*n*n+174043*n-416895,40540500*n*n)

for n in range(1,151):
    assert third(n)==claimed_third(n),n
    assert variance(n)>0

# Positive skewness and the discrete maximum at n=2.
def squared_skew(n): return third(n)**2 / variance(n)**3
assert squared_skew(2) > squared_skew(1)
assert squared_skew(2) > squared_skew(3)
assert squared_skew(2) > F(502883,40540500)**2/F(109,4050)**3
# For every real x>=3, derivative = -9 P(x)/[1001 x^(3/2)(218x-49)^(5/2)].
# P(3)>0, P'(3)>0, P''(x)>0; hence strict decrease after x=3.
P=lambda n: 149806549*n*n-355004333*n+20427855
assert P(3)>0 and 2*149806549*3-355004333>0
for n in range(3,151):
    assert squared_skew(n)>squared_skew(n+1)
assert squared_skew(1) < F(502883,40540500)**2/F(109,4050)**3
for n in range(2,151):
    assert squared_skew(n)>F(502883,40540500)**2/F(109,4050)**3

print('PASS: five exact cubic contractions; mean, variance, 150 finite-n cubic moments, skewness maximum and monotonic boundary checks')
print('moments:',[str(v) for v in [C0,C1,C2,C3,C4]])
print('skewness n=1,2,3,10,limit:',*[round(float(squared_skew(n))**.5,9) for n in [1,2,3,10]],round(float(F(502883,40540500)**2/F(109,4050)**3)**.5,9))
