"""Reproduce finite arithmetic certificates for 11-adic derangement fibers.
Run with Python 3 (standard library only): python check.py
"""
from collections import Counter

P = 11
CRITICAL = (1, 2, 7)
REGULAR_COUNTS = {0: 2, 1: 3, 5: 1, 9: 2}


def jets(a, power, degree=2):
    """Coefficients of F(a+T) through T^degree modulo 11^power.

    Terms of index >= (power+degree)*11 vanish in these jets.
    """
    mod = P**power
    products = [1] + [0] * degree
    totals = products[:]
    for n in range(1, (power + degree) * P):
        b = a - n + 1
        products = [(b * products[j] + (products[j - 1] if j else 0)) % mod
                    for j in range(degree + 1)]
        sign = -1 if n % 2 else 1
        totals = [(totals[j] + sign * products[j]) % mod
                  for j in range(degree + 1)]
    return totals


def square_roots_count(y, level):
    """Number of s mod 11^level with s^2 = y mod 11^level."""
    if level == 0:
        return 1
    modulus = P**level
    y %= modulus
    if y == 0:
        return P**(level // 2)
    valuation = 0
    while y % P == 0:
        y //= P
        valuation += 1
    if valuation % 2 or pow(y, (P - 1) // 2, P) != 1:
        return 0
    return 2 * P**(valuation // 2)


def critical_data(k):
    """Returns a, center-digit t, critical value, quadratic unit at level k."""
    assert k >= 2
    data = []
    for a in CRITICAL:
        tau = 0
        for digit_index in range(k - 2):
            place = P**digit_index
            choices = []
            for digit in range(P):
                t = tau + digit * place
                deriv = jets(a + P * t, digit_index + 2, 1)[1]
                assert deriv % P == 0
                if (deriv // P) % (P**(digit_index + 1)) == 0:
                    choices.append(t)
            assert len(choices) == 1
            tau = choices[0]
        center = a + P * tau
        critical_value = jets(center, k, 0)[0]
        quad_unit = jets(a, max(k - 2, 1), 2)[2] % P**max(k - 2, 1)
        assert quad_unit % P != 0
        data.append((a, tau, critical_value, quad_unit))
    return data


def predicted_fiber(k, y, critical):
    modulus = P**k
    y %= modulus
    if k == 1:
        c = lambda r: REGULAR_COUNTS.get(r % P, 0) + int(r % P in (0, 1, 5))
        return c(y) + c(-y)
    total = REGULAR_COUNTS.get(y % P, 0) + REGULAR_COUNTS.get((-y) % P, 0)
    for _, _, gamma, unit in critical:
        for target in (y, -y):
            delta = (target - gamma) % modulus
            if delta % P**2 == 0:
                if k == 2:
                    q = 0
                else:
                    q = (delta // P**2) * pow(unit, -1, P**(k - 2))
                total += P * square_roots_count(q, k - 2)
    return total


def check_jets():
    rows = [jets(a, 3, 2) for a in range(P)]
    assert [r[0] % P for r in rows] == [1, 0, 1, 9, 9, 0, 1, 5, 5, 0, 1]
    assert [r[1] % P for r in rows] == [10, 0, 0, 10, 6, 5, 3, 0, 6, 7, 7]
    assert [(a, (rows[a][1] // P) % P, rows[a][2] % P)
            for a in CRITICAL] == [(1, 1, 8), (2, 9, 6), (7, 10, 4)]
    assert [(a, t, g, u) for a, t, g, u in critical_data(3)] == [
        (1, 2, 121, 8), (2, 2, 1090, 6), (7, 7, 1050, 4)]
    print('Exact degree-two coefficient and critical-center certificates: PASS')


def check_fibers(max_power=6):
    for k in range(1, max_power + 1):
        modulus = P**k
        counts = [0] * modulus
        d = 1
        for n in range(2 * modulus):
            if n:
                d = (n * d + (-1 if n % 2 else 1)) % modulus
            counts[d] += 1
        critical = critical_data(k) if k >= 2 else []
        for y, count in enumerate(counts):
            expected = predicted_fiber(k, y, critical)
            assert count == expected, (k, y, count, expected)
            assert bool(count) == (y % P in (0, 1, 2, 5, 6, 9, 10))
        assert sum(counts) == 2 * modulus
        assert sum(bool(x) for x in counts) == 7 * modulus // P
        print('Power', k, ': all', modulus, 'residue fibers PASS; max fiber', max(counts))


if __name__ == '__main__':
    check_jets()
    check_fibers()
    print('ALL CHECKS PASS')
