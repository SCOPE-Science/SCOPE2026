"""Finite diagnostics for the Rademacher absolute-power kernel.

The theorem for arbitrary dimension and exponent follows analytically; these
finite checks only catch normalization and indexing errors.
"""
from itertools import product, combinations
from math import comb


def eigenvalue(n, order, p):
    assert order % 2 == 0 and 0 <= order <= n
    return sum(((-1) ** a) * comb(order, a) * comb(n - order, b)
               * abs(n - 2 * a - 2 * b) ** p
               for a in range(order + 1)
               for b in range(n - order + 1)) / 2


def run():
    count = 0
    for n in range(2, 13):
        for order in range(0, n + 1, 2):
            ev = eigenvalue(n, order, 1)
            assert ev > 0 if order == 0 else (ev > 0 if order % 4 == 2 else ev < 0)
            count += 1
        for order in range(0, n + 1, 2):
            ev = eigenvalue(n, order, 2)
            target = (n if order == 0 else 2 if order == 2 else 0) * 2 ** (n - 1)
            assert ev == target, (n, order, ev, target)
            count += 1
    for n in range(2, 9):
        for p in (0.5, 1.25, 1.75):
            for order in range(0, n + 1, 2):
                ev = eigenvalue(n, order, p)
                assert ev > 1e-7 if order == 0 or order % 4 == 2 else ev < -1e-7, (n, order, p, ev)
                count += 1
    for n in range(2, 7):
        # Keep the representatives with first coordinate +1.
        signs = [(1,) + t for t in product((-1, 1), repeat=n - 1)]
        for p in (1, 1.5):
            for order in range(0, n + 1, 2):
                choice = set(range(order))
                ev = eigenvalue(n, order, p)
                for a in signs:
                    left = sum(abs(sum(x * y for x, y in zip(a, b))) ** p
                               * product_sign(b, choice) for b in signs)
                    right = ev * product_sign(a, choice)
                    assert abs(left - right) < 1e-7, (n, order, p, left, right)
                    count += 1
    print('RADEMACHER_ABSOLUTE_POWER_DIAGNOSTICS_OK', count)


def product_sign(v, choice):
    result = 1
    for i in choice:
        result *= v[i]
    return result


if __name__ == '__main__':
    run()
