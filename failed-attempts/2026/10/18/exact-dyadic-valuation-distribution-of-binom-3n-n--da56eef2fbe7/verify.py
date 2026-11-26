#!/usr/bin/env python3
"""Standalone exact-integer checks of the dyadic (3n choose n) valuation identity."""
from collections import Counter
from math import comb
from fractions import Fraction

STATES = ((0, 0), (0, 1), (1, 0), (1, 1))

def valuation_factorial(n):
    s = 0
    while n:
        n //= 2
        s += n
    return s

def valuation(n):
    return valuation_factorial(3 * n) - valuation_factorial(2 * n) - valuation_factorial(n)

def matrix_hist(k):
    states = {(0, 0): Counter({0: 1})}
    for _ in range(k):
        next_states = {}
        for (previous, carry), hist in states.items():
            for digit in (0, 1):
                new_carry = (digit + previous + carry) // 2
                target = (digit, new_carry)
                out = next_states.setdefault(target, Counter())
                for v, count in hist.items():
                    out[v + new_carry] += count
        states = next_states
    result = Counter()
    for (previous, carry), hist in states.items():
        terminal = (previous + carry) // 2
        for v, count in hist.items():
            result[v + terminal] += count
    return +result

def poly_add(a, b):
    c = dict(a)
    for exponent, count in b.items():
        c[exponent] = c.get(exponent, 0) + count
    return {e:v for e,v in c.items() if v}

def poly_scale(a, factor):
    return {e:factor*v for e,v in a.items() if factor*v}

def poly_shift(a, shift):
    return {e+shift:v for e,v in a.items()}

def rhs(k):
    # [t^k](1+t)(1-zt), including k=0.
    if k == 0:
        return Counter({0: 1})
    if k == 1:
        return Counter({0: 1, 1: -1})
    if k == 2:
        return Counter({1: -1})
    return Counter()

def test():
    hist = [matrix_hist(k) for k in range(31)]
    for k in range(31):
        assert sum(hist[k].values()) == 2 ** k
        assert hist[k].get(1, 0) == 0
        if k >= 3:
            # (1-(1+z)t-(1-z+z^2)t^2+(z+z^2)t^3)F=(1+t)(1-zt).
            lhs = hist[k]
            lhs = poly_add(lhs, poly_scale(hist[k-1], -1))
            lhs = poly_add(lhs, poly_scale(poly_shift(hist[k-1], 1), -1))
            lhs = poly_add(lhs, poly_scale(hist[k-2], -1))
            lhs = poly_add(lhs, poly_shift(hist[k-2], 1))
            lhs = poly_add(lhs, poly_scale(poly_shift(hist[k-2], 2), -1))
            lhs = poly_add(lhs, poly_shift(hist[k-3], 1))
            lhs = poly_add(lhs, poly_shift(hist[k-3], 2))
            assert lhs == rhs(k), (k, lhs)
        total = sum(v * c for v,c in hist[k].items())
        exact_mean = Fraction(k,2) - Fraction(2,3) + Fraction(3+(-1)**k, 6*2**k)
        assert Fraction(total, 2**k) == exact_mean
        ff = sum(v*(v-1)*c for v,c in hist[k].items())
        exact_ff = (Fraction(9*k*k-9*k-16,36)
                    + Fraction((3*k-1)*(-1)**k,18*2**k)
                    + Fraction(k+1,2*2**k))
        assert Fraction(ff,2**k) == exact_ff
    tested = 0
    for k in range(13):
        direct = Counter(valuation(n) for n in range(1<<k))
        assert direct == hist[k], (k,direct,hist[k])
        for n in range(1<<k):
            if n < 65:  # direct integer binomial cross-check
                m = comb(3*n,n)
                v = (m & -m).bit_length()-1
                assert v == valuation(n)
            tested += 1
    # Fibonacci no-carry layer, Fibonacci(0)=0, Fibonacci(1)=1.
    a,b = 0,1
    fib = [0,1]
    for _ in range(34):
        a,b = b,a+b
        fib.append(b)
    for k in range(31):
        assert hist[k].get(0,0) == fib[k+2]
        assert hist[k].get(3,0) == (hist[k-1].get(2,0) if k else 0)
    print('BINOMIAL_3N_N_VALUATION_EXACT_OK', 'dyadic_lengths=0..30',
          'direct_inputs=',tested,'rational_recurrences=28', 'moments=31')

if __name__ == '__main__':
    test()
