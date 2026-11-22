#!/usr/bin/env python3
"""Exact finite checks for polynomial Fibonacci exponential degree formulas.

The infinite-degree proof is in RESULT.md; these tests are diagnostics, not a
substitute for the valuation argument. Python 3 standard library only.
"""
from collections import defaultdict
from fractions import Fraction
from math import comb
import random


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def lucas(n):
    if n == 0:
        return 2
    a, b = 2, 1
    for _ in range(1, n):
        a, b = b, a + b
    return b


def v5(x):
    if x == 0:
        return 10**6
    x = abs(x)
    out = 0
    while x % 5 == 0:
        x //= 5
        out += 1
    return out


def predicted_h(coeff):
    return max([0] + [j - v5(c) for j, c in enumerate(coeff) if j > 0 and c])


def factor_data(coeff):
    central = defaultdict(Fraction)
    pair = defaultdict(Fraction)
    for j, cj in enumerate(coeff):
        if cj == 0:
            continue
        f = Fraction(cj, 5**j)
        sg = (-1)**j
        central[sg] += f * sg * comb(2*j, j)
        for t in range(1, j+1):
            sg = (-1)**(j-t)
            pair[t, sg] += f * sg * comb(2*j, j-t)
    return central, pair


def eval_poly(coeff, x):
    return sum(c * x**(2*j) for j, c in enumerate(coeff))


def ghost(coeff, n):
    central, pair = factor_data(coeff)
    return sum(c * sg**n for sg, c in central.items()) + sum(
        b * sg**n * lucas(2*t*n) for (t, sg), b in pair.items()
    )


def exp_coeffs(ghosts):
    nmax = len(ghosts)
    out = [Fraction(1)]
    for n in range(1, nmax+1):
        out.append(sum(ghosts[k-1]*out[n-k] for k in range(1, n+1))/n)
    return out


def mul(a, b, size):
    c = [Fraction(0)] * size
    for i, ai in enumerate(a[:size]):
        for j, bj in enumerate(b[:size-i]):
            c[i+j] += ai*bj
    return c


def invert(a, size):
    assert a[0] == 1
    b = [Fraction(1)]
    for k in range(1, size):
        b.append(-sum(a[j]*b[k-j] for j in range(1, min(k, len(a)-1)+1)))
    return b


def intpow(a, exponent, size):
    if exponent < 0:
        a = invert(a, size)
        exponent = -exponent
    result = [Fraction(1)] + [Fraction(0)]*(size-1)
    while exponent:
        if exponent & 1:
            result = mul(result, a, size)
        exponent >>= 1
        if exponent:
            a = mul(a, a, size)
    return result


def check(coeff, size=11):
    h = predicted_h(coeff)
    m = 5**h
    cen, pair = factor_data(coeff)
    all_den = [b.denominator for b in list(cen.values()) + list(pair.values())]
    assert all(m % b == 0 for b in all_den)
    if h:
        marks = [j for j, c in enumerate(coeff) if j > 0 and c and j-v5(c) == h]
        highest = max(marks)
        top = pair[highest, +1]
        assert v5(top.numerator) == 0 and top.denominator == m, (coeff, m, top)
    for n in range(1, size+1):
        assert ghost(coeff, n) == eval_poly(coeff, fib(n)), (coeff,n)
    g = [m*eval_poly(coeff, fib(n)) for n in range(1,size+1)]
    direct = exp_coeffs(g)
    reconstructed = [Fraction(1)] + [Fraction(0)]*size
    for sg, weight in cen.items():
        exponent = -m*weight
        assert exponent.denominator == 1
        p = [Fraction(1),Fraction(-sg)] + [Fraction(0)]*(size-1)
        reconstructed = mul(reconstructed, intpow(p,int(exponent),size+1),size+1)
    for (t,sg), weight in pair.items():
        exponent = -m*weight
        assert exponent.denominator == 1
        p = [Fraction(1),Fraction(-sg*lucas(2*t)),Fraction(1)] + [Fraction(0)]*(size-2)
        reconstructed = mul(reconstructed,intpow(p,int(exponent),size+1),size+1)
    assert direct == reconstructed, (coeff, direct, reconstructed)
    return h


def main():
    examples = [
        [0], [7], [0,5], [0,0,5], [0,-1,0,1], [0,0,-1,0,1],
        [11,5,25,125], [3,0,5,0,0,25], [0,1,-1], [0,5,0,0,0,1],
        [0,-1,0,1,0,0,1],
    ]
    for c in examples:
        check(c)
    assert check([0,-1,0,1]) == 3
    assert check([0,0,-1,0,1]) == 4
    assert check([0,0,5]) == 1
    assert check([0,5]) == 0
    rng = random.Random(20261112)
    for _ in range(100):
        d=rng.randrange(1,7)
        c=[rng.choice([-25,-5,-2,-1,0,1,2,5,25,125]) for _ in range(d+1)]
        check(c, size=9)
    print('FIBONACCI_POLYNOMIAL_DEGREE_EXACT_OK', len(examples)+100, 'cases', '125_degree_example', '625_degree_example')


if __name__ == '__main__':
    main()
