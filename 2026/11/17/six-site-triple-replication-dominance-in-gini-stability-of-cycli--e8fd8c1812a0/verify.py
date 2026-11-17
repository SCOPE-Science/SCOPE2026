#!/usr/bin/env python3
"""Exact finite diagnostics for the Gini modulus of cyclic two-site morphological opening."""
from fractions import Fraction
from itertools import permutations
from random import Random


def filt(x):
    n = len(x)
    return [min(x[i], max(x[(i - 1) % n], x[(i + 1) % n])) for i in range(n)]


def gini(x):
    return sum(abs(x[i] - x[j]) for i in range(len(x)) for j in range(i + 1, len(x)))


def predicted(n):
    if n == 2:
        return Fraction(0)
    if n == 3:
        return Fraction(1)
    if n == 4:
        return Fraction(4, 3)
    if n == 5:
        return Fraction(3, 2)
    return Fraction(3 * (n - 3), n - 1)


def selector(x):
    n = len(x)
    out = []
    for i in range(n):
        l = (i - 1) % n
        r = (i + 1) % n
        neighbor = l if x[l] > x[r] else r
        out.append(i if x[i] < x[neighbor] else neighbor)
    return out


def selector_norm(s):
    n = len(s)
    best = Fraction(0)
    best_cut = None
    for mask in range(1, (1 << n) - 1):
        p = mask.bit_count()
        q = sum((mask >> j) & 1 for j in s)
        rat = Fraction(q * (n - q), p * (n - p))
        if rat > best:
            best = rat
            best_cut = mask
    return best, best_cut


def exact_exhaustive():
    n_orders = 0
    for n in range(2, 9):
        best = Fraction(0)
        for p in permutations(range(n)):
            vals = list(p)
            s = selector(vals)
            v, _ = selector_norm(s)
            if v > best:
                best = v
            assert v <= predicted(n), (n, p, v)
            n_orders += 1
        assert best == predicted(n), (n, best, predicted(n))
    print("ALL_ORDER_CHAMBERS_EXACT_CUT_NORMS_PASSED", n_orders)


def exact_multiplicity_bound():
    tests = 0
    for n in range(6, 201):
        target = predicted(n)
        for size in range(1, n):
            lower = max(0, n - 3 * (n - size))
            upper = min(n, 3 * size)
            for q in range(lower, upper + 1):
                assert Fraction(q * (n - q), size * (n - size)) <= target, (n, size, q)
                tests += 1
    print("MULTIPLICITY_CUT_GRID_PASSED", tests)


def witness(n):
    if n in (3, 4, 5):
        x = list(range(n))
        j = n - 2 if n >= 4 else 0
    else:
        x = [-(i + 10) for i in range(n)]
        x[0] = 0
        x[1] = 4
        x[n - 1] = 5
        x[2] = -2
        x[n - 2] = -1
        j = 0
    assert len(set(x)) == n, (n, x)
    y = [Fraction(a) for a in x]
    y[j] += Fraction(1, 100)
    xx = [Fraction(a) for a in x]
    h = [b - a for a, b in zip(filt(xx), filt(y))]
    inp = [b - a for a, b in zip(xx, y)]
    assert gini(inp) > 0
    assert Fraction(gini(h), gini(inp)) == predicted(n), (n, j, x, gini(h), gini(inp))


def exact_witnesses():
    for n in range(3, 201):
        witness(n)
    assert gini(filt([0, 1])) == 0
    print("ARBITRARILY_CLOSE_SHARP_WITNESSES_PASSED", 198)


def arbitrary_two_inputs():
    rng = Random(10911)
    tests = 0
    for n in range(2, 31):
        for _ in range(150):
            a = [Fraction(rng.randrange(-90, 91), 7) for _ in range(n)]
            b = [Fraction(rng.randrange(-90, 91), 11) for _ in range(n)]
            input_diff = [u - v for u, v in zip(a, b)]
            output_diff = [u - v for u, v in zip(filt(a), filt(b))]
            assert gini(output_diff) <= predicted(n) * gini(input_diff)
            tests += 1
    print("EXACT_ARBITRARY_TWO_INPUT_DIAGNOSTICS_PASSED", tests)


if __name__ == '__main__':
    exact_exhaustive()
    exact_multiplicity_bound()
    exact_witnesses()
    arbitrary_two_inputs()
    print("ALL_CYCLIC_OPENING_GINI_CHECKS_PASSED")
