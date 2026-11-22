"""Independent arithmetic checks for two-stage one-dimensional rod adsorption.

Run: python checks.py
Requires Python 3, scipy, numpy. Analytical asymptotic arguments are in RESULT.md.
"""
from functools import lru_cache
from fractions import Fraction
import math
import numpy as np
from scipy.integrate import quad

ASSERTS = 0

def check(x, reason=""):
    global ASSERTS
    if not x:
        raise AssertionError(reason)
    ASSERTS += 1


def finite_mean(s, length):
    b = [Fraction(0)] * (length + 1)
    for n in range(s, length + 1):
        b[n] = Fraction(s) + Fraction(2, n - s + 1) * sum(b[:n - s + 1])
    return b


def brute_mean(s, n):
    @lru_cache(None)
    def recurse(mask):
        starts = [i for i in range(n-s+1) if not mask & (((1<<s)-1)<<i)]
        if not starts:
            return Fraction(mask.bit_count())
        return sum((recurse(mask | (((1<<s)-1)<<i)) for i in starts), Fraction(0))/len(starts)
    return recurse(0)


def single_density(s):
    idx = np.arange(1, s, dtype=float)
    return s * quad(lambda z: math.exp(-2 * np.sum((1-z**idx)/idx)), 0, 1,
                    epsabs=2e-12, limit=200)[0]


def pair_density(s, k):
    j = np.arange(1, k, dtype=float)
    harm = np.sum(1/j)
    b = np.array([float(x) for x in finite_mean(s,k-1)])
    def kernel(z):
        return math.exp(-2 * (harm - float(np.sum(z**j/j))))
    mk = k * quad(kernel,0,1,epsabs=2e-12,limit=250)[0]
    extra = quad(lambda z: 2*(1-z)*kernel(z)*float(np.polynomial.polynomial.polyval(z,b)),
                 0,1,epsabs=2e-12,limit=250)[0]
    return mk+extra, mk


def main():
    for s in (2,3,4,5):
        bs = finite_mean(s,18)
        for n in range(s,11):
            check(bs[n] == brute_mean(s,n), f'finite recurrence s={s},n={n}')
    # The exact recurrence residual is an identity, checked at additional sizes.
    for s in (2,3,4,5,6):
        b = finite_mean(s,45)
        for n in range(s,46):
            check((n-s+1)*b[n] == s*(n-s+1)+2*sum(b[:n-s+1]))
    m_inf = 0.7475979202534114
    eta = math.exp(-2*np.euler_gamma)
    mk_coefficient = (m_inf-eta)/2
    # Numerical diagnostics confirm the large-k constants, not an infinite proof.
    for k in (50,100,200,400):
        for s in (2,3,4):
            if s>=k: continue
            two,mk = pair_density(s,k)
            ms=single_density(s)
            limit = ms + (1-ms)*m_inf
            coefficient = (1-ms)*(mk_coefficient-s*m_inf)
            check(two<limit, f'negative correction s={s},k={k}')
            check(abs(k*(two-limit)-coefficient)<0.012, f'first-order s={s},k={k}')
            check(abs(k*(mk-m_inf)-mk_coefficient)<0.012, f'single-k correction k={k}')
    print(f'PASS {ASSERTS} exact and numerical assertions')

if __name__=='__main__':
    main()
