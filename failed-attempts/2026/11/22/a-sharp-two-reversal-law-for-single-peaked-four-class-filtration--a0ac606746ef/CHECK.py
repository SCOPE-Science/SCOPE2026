"""Exact witness and finite-order checks for a selective-attenuation theorem.

Run with Python 3 and the standard library only. Analytic zero bounds are proved
in the accompanying document; numeric bisection is not their substitute.
"""
from fractions import Fraction
from itertools import combinations, permutations
from math import exp, log
from random import Random

S = (1, 2, 3, 4)
W = (1, 100, 100, 25)
R = (1, 4, 5, 3)
PAIR_COEFFICIENTS = {4: -150, 5: -300, 6: -800,
                     7: 5000, 8: 5000, 9: -10000}


def pair_terms(sizes, weights, rates):
    terms = []
    for i, j in combinations(range(len(sizes)), 2):
        coefficient = weights[i]*weights[j]*(sizes[j]-sizes[i])*(rates[i]-rates[j])
        terms.append((rates[i]+rates[j], coefficient, (i+1, j+1)))
    return sorted(terms)


def collect(terms):
    result = {}
    for exponent, coefficient, _ in terms:
        result[exponent] = result.get(exponent, 0) + coefficient
    return {x: y for x, y in sorted(result.items()) if y}


def variations(values):
    signs = [1 if x > 0 else -1 for x in values if x != 0]
    return sum(a != b for a, b in zip(signs, signs[1:]))


def q(y):
    return -3 - 6*y - 16*y*y + 100*y**3 + 100*y**4 - 200*y**5


def mean_at(t):
    n = [w*exp(-rate*t) for w, rate in zip(W, R)]
    return sum(size*count for size, count in zip(S, n))/sum(n)


def bisect(left, right):
    a, b = q(left), q(right)
    assert a*b < 0
    for _ in range(90):
        mid = (left+right)/2
        c = q(mid)
        if not c:
            return mid
        if (c > 0) == (a > 0):
            left, a = mid, c
        else:
            right, b = mid, c
    return (left+right)/2


def main():
    assert collect(pair_terms(S, W, R)) == PAIR_COEFFICIENTS
    assert q(Fraction(1)) == -25
    assert q(Fraction(1, 2)) == Fraction(5, 2)
    assert q(Fraction(1, 4)) == Fraction(-479, 128)
    assert variations(PAIR_COEFFICIENTS.values()) == 2
    # Exhaust all six strict rate rankings for three ordered size classes.
    for p in permutations((1, 2, 3)):
        c = collect(pair_terms((1,2,3), (1,1,1), p))
        assert variations(c.values()) <= 1
    # Sample the *strict* admissible single-peak rate cone, and check only
    # the coefficient-sign ordering (not an infinite root count).
    rng = Random(2024)
    for _ in range(3000):
        a = rng.uniform(0.2, 9.0)
        b = rng.uniform(0.2, 9.0)
        c = rng.uniform(0.01, a*0.95)
        r = (1.0, 1.0+a+b, 1.0+a+b+c, 1.0+a)
        w = tuple(rng.uniform(0.1, 20) for _ in range(4))
        s = tuple(sorted(rng.uniform(0.1, 20) for _ in range(4)))
        assert variations(x[1] for x in pair_terms(s,w,r)) <= 2
    y_lo = bisect(0.25, 0.5)
    y_hi = bisect(0.5, 1.0)
    assert 0.4332 < y_lo < 0.4334
    assert 0.8937 < y_hi < 0.8938
    t_min, t_max = -log(y_hi), -log(y_lo)
    assert mean_at(0) > mean_at(t_min) < mean_at(log(2))
    assert mean_at(log(2)) < mean_at(t_max) > mean_at(log(4))
    print('Exact pair coefficient check passed:', PAIR_COEFFICIENTS)
    print('Exact Q signs: Q(1)=-25, Q(1/2)=5/2, Q(1/4)=-479/128')
    print('Six three-class orderings and 3000 admissible four-class rankings checked.')
    print('Local minimum at t=%.12f; mean=%.12f' % (t_min, mean_at(t_min)))
    print('Local maximum at t=%.12f; mean=%.12f' % (t_max, mean_at(t_max)))
    print('Checks passed.')


if __name__ == '__main__':
    main()
