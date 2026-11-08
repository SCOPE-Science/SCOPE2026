#!/usr/bin/env python3
"""Exact integer checks of a joint ternary binomial-valuation theorem."""
from collections import Counter
from fractions import Fraction
from math import comb


def factorial_v3(n):
    acc = 0
    while n:
        n //= 3
        acc += n
    return acc


def digit_sum3(n):
    s = 0
    while n:
        n, d = divmod(n, 3)
        s += d
    return s


def polynomial_recurrence(levels):
    # Pair-count polynomials represented by dictionaries of exponents.
    f0 = {(0, 0, 0): 1}  # key: (valuation X, valuation Y, final carry)
    for r in range(levels + 1):
        if r == 0:
            yield Counter({(0, 0): 1})
        else:
            f1 = Counter()
            for (x, y, a), cnt in f0.items():
                for d in range(3):
                    b = (2 * d + a) // 3
                    f1[(x + b, y + d - b, b)] += cnt
            f0 = f1
            ans = Counter()
            for (x, y, a), cnt in f0.items():
                ans[(x, y)] += cnt
            yield ans


def direct_distribution(r):
    ans = Counter()
    for n in range(3**r):
        v_x = factorial_v3(2*n) - 2*factorial_v3(n)
        v_y = factorial_v3(3*n) - factorial_v3(2*n) - factorial_v3(n)
        assert v_x + v_y == digit_sum3(n), (r, n, v_x, v_y)
        ans[(v_x, v_y)] += 1
    return ans


def moments(counts, r):
    z = Fraction(1, 3**r)
    ex = z * sum(x*k for (x, y), k in counts.items())
    ey = z * sum(y*k for (x, y), k in counts.items())
    vx = z*sum(x*x*k for (x, y), k in counts.items())-ex*ex
    vy = z*sum(y*y*k for (x, y), k in counts.items())-ey*ey
    cov = z*sum(x*y*k for (x, y), k in counts.items())-ex*ey
    t = Fraction(1, 3**r)
    assert ex == Fraction(r,2)-Fraction(1-t,4)
    assert ey == Fraction(r,2)+Fraction(1-t,4)
    assert vx == Fraction(r,2)-Fraction(7,16)+t/2-t*t/16
    assert vy == Fraction(r,6)+(1-t*t)/16
    assert cov == (1-t)*(3-t)/16
    assert vx+vy+2*cov == Fraction(2*r,3)


def main():
    allindices = 0
    for r, pred in enumerate(polynomial_recurrence(9)):
        direct = direct_distribution(r)
        assert pred == direct, (r, pred-direct, direct-pred)
        allowed = {(0,j) for j in range(r+1)} | {(i,j) for i in range(1,r+1) for j in range(1,r+1)}
        assert set(pred) == allowed
        assert len(pred) == r*r+r+1
        assert sum(pred.values()) == 3**r
        moments(pred,r)
        allindices += 3**r
    # Integer binomial coefficients, independent of the factorial valuation routine.
    for n in range(301):
        a = comb(2*n, n)
        b = comb(3*n, n)
        u = 0
        v = 0
        while a % 3 == 0:
            a //= 3
            u += 1
        while b % 3 == 0:
            b //= 3
            v += 1
        assert u == factorial_v3(2*n)-2*factorial_v3(n)
        assert v == factorial_v3(3*n)-factorial_v3(2*n)-factorial_v3(n)
    print(f'VERIFY_OK levels=0..9 direct_indices={allindices} integer_binomial_cases=301 joint_polynomials=PASS support=PASS exact_moments=PASS')

if __name__ == '__main__':
    main()
