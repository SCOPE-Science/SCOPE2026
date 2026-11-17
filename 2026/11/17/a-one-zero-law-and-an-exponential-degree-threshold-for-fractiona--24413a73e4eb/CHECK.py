"""Supplementary finite tests for sampled fractional Bergman kernels.

Run: python CHECK.py (requires scipy and mpmath).
These tests corroborate finite values; the general theorem is analytical.
"""
import math
from scipy.integrate import quad
from scipy.optimize import brentq
import mpmath as mp


def J(eps, k):
    assert 0 < eps < 1 and k >= 1
    c = math.sin(math.pi * eps) / math.pi
    def f(x):
        if x == 0:
            return 0.0
        a = -math.expm1(-x)
        b = -math.expm1(-k*x)
        return (c * math.exp(-(1+eps)*x) * b /
                (a**(1+eps) * (1+math.exp(-k*x))))
    return quad(f, 0, 1000, epsabs=4e-10, epsrel=4e-10,
                points=[1.0/k, 1.0], limit=200)[0]


def b(eps, n):
    return math.exp(math.lgamma(n+1+eps)-math.lgamma(1+eps)-math.lgamma(n+1))


count = 0
for eps in (0.1, 0.2, 0.5, 0.9):
    js = [J(eps, k) for k in (1, 2, 3, 5, 10, 40, 100)]
    assert all(x < y for x, y in zip(js, js[1:]))
    count += 6
    assert abs(js[0] - (1-2**(-eps))) < 1e-8
    count += 1
    for k in (1,2,3,5,10,40,100):
        # Alternating-moment estimate: b_k-1-(b_2k-b_k) <= J <= b_k-1
        lower = 2*b(eps,k)-b(eps,2*k)-1
        upper = b(eps,k)-1
        assert lower-1e-8 <= J(eps,k) <= upper+1e-8
        count += 1

for eps, lo, hi in ((0.9,2,3), (0.5,4,5), (0.2,20,40), (0.1,900,1100)):
    kstar = brentq(lambda k: J(eps,k)-1,lo,hi)
    assert lo < kstar < hi
    assert J(eps,kstar*.99999) < 1 < J(eps,kstar*1.00001)
    count += 3

# Verify the kernel root at a genuinely noninteger weight and k=5.
mp.mp.dps=40
eps=mp.mpf('0.5'); k=5
F=lambda r: mp.nsum(lambda n: mp.gamma(k*n+1+eps)/
                (mp.gamma(1+eps)*mp.gamma(k*n+1))*(-r)**n,[0,mp.inf])
root=mp.findroot(F,(mp.mpf('.05'),mp.mpf('.8')))
assert 0 < root < 1
assert abs(F(root)) < mp.mpf('1e-30')
count += 2

# Analytic prefactor sanity checks, not a proof of the limit.
lim=mp.pi*mp.exp(-mp.euler)/2
for eps in (mp.mpf('.05'),mp.mpf('.02'),mp.mpf('.01')):
    K=(mp.gamma(1+eps)/mp.altzeta(-eps))**(1/eps)
    ratio=K/mp.power(2,1/eps)
    assert abs(ratio-lim) < mp.mpf('0.06')
    count+=1
print('PASS:',count,'supplementary finite assertions, root',root)
