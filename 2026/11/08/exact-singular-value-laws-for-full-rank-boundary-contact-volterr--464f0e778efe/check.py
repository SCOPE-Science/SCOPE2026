"""Exact monomial normalization and finite asymptotic diagnostics.

Run with Python 3.10 or newer. These tests are finite checks, not a
substitute for the proof of the infinite singular-value asymptotic.
"""
from fractions import Fraction
from itertools import product
from math import factorial, comb, prod


def norm_sq(d, alpha):
    """Normalized-volume Bergman norm squared of a monomial."""
    return Fraction(factorial(d) * prod(factorial(a) for a in alpha), factorial(sum(alpha) + d))


def rising(a, k):
    return prod(range(a, a + k))


def weight_sq_closed(d, h, k, alpha, lam):
    N = sum(alpha)
    if N == 0:
        return Fraction(0)
    beta = alpha[h:]
    q = Fraction(N, N + k)**2
    q *= prod(lam[j]**(2 * beta[j]) for j in range(d - h))
    q *= Fraction(rising(beta[0] + 1, k), rising(N + d + 1, k))
    return q


def weight_sq_from_action(d, h, k, alpha, lam):
    N = sum(alpha)
    if N == 0:
        return Fraction(0)
    dest = list(alpha)
    dest[h] += k
    beta = alpha[h:]
    coefficient_sq = Fraction(N, N + k)**2 * prod(lam[j]**(2 * beta[j]) for j in range(d - h))
    return coefficient_sq * norm_sq(d, tuple(dest)) / norm_sq(d, alpha)


def weak_coefficient(d, h, k, lam, cutoff=1200):
    """Finite truncation of the proved positive coefficient series."""
    import math
    t = 2 * h / k
    c = 0.0
    for b in range(cutoff):
        c += lam[0]**(t * b) * float(rising(b + 1, k))**(h / k)
    c /= factorial(h)
    for q in lam[1:]:
        c /= (1 - q**t)
    return c


def finite_counts(d, h, k, lam, eps, max_b=12):
    import math
    max_b = max_b if (d - h) < 3 else min(max_b, 8)
    result = 0
    for beta in product(range(max_b), repeat=d - h):
        a2 = prod(float(lam[j])**(2 * beta[j]) for j in range(d - h)) * rising(beta[0] + 1, k)
        if a2 <= 0:
            continue
        upper = int((a2 / (eps * eps))**(1/k)) + 5
        for M in range(upper):
            N = M + sum(beta)
            if not N:
                continue
            w2 = (N / (N + k))**2 * a2 / rising(N + d + 1, k)
            if w2 > eps**2:
                result += comb(M + h - 1, h - 1)
    return result


def main():
    checks = 0
    for d in range(2, 6):
        for h in range(1, d):
            for k in range(1, 5):
                lam = (Fraction(1, 2),) * (d - h)
                seen = set()
                for alpha in product(range(4), repeat=d):
                    lhs = weight_sq_closed(d, h, k, alpha, lam)
                    rhs = weight_sq_from_action(d, h, k, alpha, lam)
                    assert lhs == rhs, (d, h, k, alpha, lhs, rhs)
                    checks += 1
                    dest = list(alpha)
                    dest[h] += k
                    assert tuple(dest) not in seen
                    seen.add(tuple(dest))
                    checks += 1
    assert weak_coefficient(2, 1, 1, [0.5], cutoff=100) - (1-.25)**(-2) < 1e-10
    checks += 1
    print('MONOMIAL_COMPANION_EXACT_OK', checks)
    for d, h, k, lam in [(2, 1, 1, [0.5]),(3, 1, 2,[0.5,0.25]),(4,2,2,[0.5,0.333333333333])]:
        C = weak_coefficient(d,h,k,lam)
        print('diagnostic', d,h,k,lam,'C=',round(C,8))
        for eps in [0.08,0.04,0.02]:
            count=finite_counts(d,h,k,lam,eps)
            print(' eps',eps,'count',count,'scaled',round(count*eps**(2*h/k),8))

if __name__=='__main__':main()
