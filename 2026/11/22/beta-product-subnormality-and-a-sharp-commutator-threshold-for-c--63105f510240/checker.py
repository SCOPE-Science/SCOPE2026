"""Supplementary exact and floating checks for the power-Fock monomial Volterra theorem.

Only finite instances are checked. Infinite statements are proved separately in RESULT.md.
Run with: python3 checker.py
"""
from fractions import Fraction
from math import exp, lgamma, isclose


def q(m, n):
    return Fraction((n + 1) * (2 * n + m + 2), 2 * (n + m)**2)


def poch(x, N):
    y = Fraction(1)
    for j in range(N):
        y *= x+j
    return y


def beta_product_moment(m, r, N):
    a = Fraction(r + 1, m)
    b = a + Fraction(1, 2)
    c = 1 + Fraction(r, m)
    return poch(a, N) * poch(b, N) / poch(c, N)**2


def raw_gamma_weight_sq(alpha, k, n):
    hratio_log = (-2*k/alpha)*__import__('math').log(2) + lgamma((2*n+2*k+2)/alpha)-lgamma((2*n+2)/alpha)
    return (k/(n+k))**2 * exp(hratio_log)


count=0
for m in range(3, 17):
    for r in range(m):
        for N in range(0, 27):
            direct = Fraction(1)
            for j in range(N):
                direct *= q(m, r+j*m)
            assert direct == beta_product_moment(m,r,N)
            count+=1
    for n in range(1, 401):
        assert q(m,n)>q(m,n-1)
        assert q(m,n)<1
        count+=2
    for n in range(m, 401):
        assert q(m,n) - q(m,n-m) > 0
        count+=1
    for N in range(0, 45):
        trace_partial=sum((q(m,n) if n<m else q(m,n)-q(m,n-m) for n in range(N+m)), Fraction(0))
        exact_tel=sum((q(m,N+r) for r in range(m)), Fraction(0))
        assert trace_partial == exact_tel
        count+=1
    for n in [10_000, 100_000, 1_000_000]:
        d=q(m,n)-q(m,n-m)
        C=Fraction(m*(3*m-4),2)
        assert abs(float(d*n*n/C)-1) < 0.0012 if n>=100_000 else abs(float(d*n*n/C)-1)<0.08
        count+=1

for alpha in (2.1, 2.5, 3.0, 3.3, 4.0, 5.7):
    for k in range(1, 7):
        for n in (0, 1, 5, 20, 100):
            val=raw_gamma_weight_sq(alpha,k,n)
            if k==alpha:
                assert isclose(val,float(q(k,n)),rel_tol=1e-11,abs_tol=1e-12)
            assert val>0
            count+=1
print('PASS',count,'supplementary finite assertion groups')
