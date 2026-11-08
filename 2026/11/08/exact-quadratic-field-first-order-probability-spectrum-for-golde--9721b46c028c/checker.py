"""Finite, exact checks for the quadratic-field spectrum of 11-avoiding words.

Usage: python3 checker.py
No network or third-party modules required. Finite checks are not an infinite proof.
"""
from fractions import Fraction as Q
from itertools import permutations


def fibonacci(n):
    x, y = 0, 1
    for _ in range(n):
        x, y = y, x + y
    return x


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def multiply(x, y):
    # In Q(phi), phi^2 = phi+1.
    a, b = x
    c, d = y
    return a*c + b*d, a*d + b*c + b*d


def phi_power(k):
    t = (Q(1), Q(0))
    base = (Q(-1), Q(1)) if k < 0 else (Q(0), Q(1))
    for _ in range(abs(k)):
        t = multiply(t, base)
    return t


def enumerate_words(n):
    if n == 0:
        yield ''
    else:
        for s in enumerate_words(n - 1):
            yield s + '0'
            if not s or s[-1] == '0':
                yield s + '1'


def first_pattern(w, patterns):
    one = [i for i, c in enumerate(w) if c == '1']
    gaps = tuple(one[j+1] - one[j] - 1 for j in range(len(one)-1))
    l = len(patterns[0])
    for j in range(len(gaps)-l+1):
        g = gaps[j:j+l]
        if g in patterns:
            return patterns.index(g)
    return None


def test_fibonacci_counts():
    for n in range(1, 17):
        ww = list(enumerate_words(n))
        assert len(ww) == fibonacci(n + 2)
        assert sum(s[-1] == '0' for s in ww) == fibonacci(n + 1)
        assert sum(s[-1] == '1' for s in ww) == fibonacci(n)
        assert all('11' not in s for s in ww)


def test_exact_field_mix():
    # Check exact coefficient identities in Q(phi) and rational conditional coins.
    examples = [(Q(-1,3), Q(1,3)), (Q(1,3), Q(1,3)),
                (Q(1,2), Q(0)), (Q(2,3), Q(-1,4))]
    for a, b in examples:
        value = a + b * (1 + 5 ** .5) / 2
        if not 0 < value < 1:
            continue
        for m in range(3, 15):
            f0, f1 = fibonacci(m+1), fibonacci(m)
            r0 = a + b * Q(fibonacci(m+2), f0)
            r1 = a + b * Q(fibonacci(m+1), f1)
            lhs = add(multiply((f0*r0, Q(0)), phi_power(-m)),
                      multiply((f1*r1, Q(0)), phi_power(-m-1)))
            assert lhs == (a, b), (a,b,m,lhs)
        assert all(Q(0) < a + b * Q(fibonacci(m+2), fibonacci(m+1)) < Q(1)
                   and Q(0) < a + b * Q(fibonacci(m+1), fibonacci(m)) < Q(1)
                   for m in range(30, 41))


def test_equal_first_hit():
    # Independent finite-word check of an unbiased two-way marker race.
    p = [(3,1,2), (3,2,1)]
    for n in range(10, 23):
        count = [0,0]
        for w in enumerate_words(n):
            k = first_pattern(w, p)
            if k is not None:
                count[k] += 1
        assert count[0] == count[1], (n, count)
    # A larger six-way race: distinct orderings of the same three gap values.
    p6 = [(4,) + v for v in permutations((1,2,3))]
    for n in range(19, 24):
        count = [0]*6
        for w in enumerate_words(n):
            k = first_pattern(w, p6)
            if k is not None:
                count[k] += 1
        assert len(set(count)) == 1, (n, count)


if __name__ == '__main__':
    test_fibonacci_counts()
    test_exact_field_mix()
    test_equal_first_hit()
    print('FIBONACCI_SPECTRUM_FINITE_CHECKS_OK')
