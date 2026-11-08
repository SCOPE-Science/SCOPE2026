"""Finite exact checks for the one-threshold position-dependent-step walk.

Run with Python 3 standard library. Finite tests supplement, not replace,
the analytic proof for all states and all integer parameters.
"""
from collections import defaultdict
from fractions import Fraction


def destinations(x, r):
    s = 1 if abs(x) <= 1 else abs(x) + r
    return (x - s, x + s)


def propagate(q, r):
    z = defaultdict(Fraction)
    for x, p in q.items():
        for y in destinations(x, r):
            z[y] += p / 2
    return dict(z)


def power(x, r, t):
    q = {x: Fraction(1)}
    for _ in range(t):
        q = propagate(q, r)
    return q


def stationary_mass(x, r):
    if r == 1:
        if x in (-1, 0, 1):
            return Fraction(1, 5)
        if abs(x) < 2:
            return Fraction(0)
        v = abs(x) + 1
        if v % 3:
            return Fraction(0)
        u = v // 3
        if u & (u - 1):
            return Fraction(0)
        k = u.bit_length() - 1
        return Fraction(1, 5 * 2**(k + 1))
    if abs(x) < r or abs(x) % r:
        return Fraction(0)
    z = abs(x) // r + 1
    if z & (z - 1) or z < 2:
        return Fraction(0)
    k = z.bit_length() - 2
    return Fraction(1, 2**(k + 2))


def stationary_predecessor_mass(x, r):
    """Sum all stationary incoming transitions, without enumerating infinitely many states."""
    if r == 1:
        if x == 0:
            return Fraction(1, 2) * (stationary_mass(1, 1) + stationary_mass(-1, 1))
        if x == 1 or x == -1:
            # From origin plus all negative/positive excursions respectively.
            return Fraction(1, 2) * (stationary_mass(0, 1) + Fraction(1, 5))
        if abs(x) == 2:
            return stationary_mass(x // 2, 1) / 2
        v = abs(x) + 1
        if v % 3 or (v // 3) & ((v // 3) - 1):
            return Fraction(0)
        k = (v // 3).bit_length() - 1
        if k < 1:
            return Fraction(0)
        pred = (1 if x > 0 else -1) * (3 * 2**(k - 1) - 1)
        return stationary_mass(pred, 1) / 2
    if abs(x) == r:
        # Each side contributes half its total stationary mass (one quarter).
        return Fraction(1, 2) * Fraction(1, 2)
    if abs(x) < r or abs(x) % r:
        return Fraction(0)
    z = abs(x) // r + 1
    if z & (z - 1) or z < 4:
        return Fraction(0)
    k = z.bit_length() - 2
    pred = (1 if x > 0 else -1) * r * (2**k - 1)
    return stationary_mass(pred, r) / 2


def exact_tests():
    checks = 0
    for r in (1, 2, 3, 7, 19):
        for x in range(-400, 401):
            assert stationary_mass(x, r) == stationary_predecessor_mass(x, r), (r, x)
            checks += 1
        for k in range(0, 14):
            if r == 1:
                a = 3 * 2**k - 1
                assert stationary_mass(a, 1) == Fraction(1, 5 * 2**(k + 1))
                assert stationary_mass(-a, 1) == stationary_mass(a, 1)
            else:
                a = r * (2**(k + 1) - 1)
                assert stationary_mass(a, r) == Fraction(1, 2**(k + 2))
                assert stationary_mass(-a, r) == stationary_mass(a, r)
            checks += 2
    for x in range(-120, 121):
        assert power(x, 1, 4).get(0, 0) >= Fraction(1, 16), x
        checks += 1
    for r in (2, 3, 4, 9):
        for x in range(-120, 121):
            q = power(x, r, 5)
            assert q.get(r, 0) >= Fraction(1, 16), (r, x, q)
            assert q.get(-r, 0) >= Fraction(1, 16), (r, x, q)
            checks += 2
    for r in (1, 2, 3, 5):
        for x in range(-25, 26):
            a, b = destinations(x, r)
            mean = Fraction(abs(a) + abs(b), 2)
            diff = mean - abs(x)
            expected = (1 if x == 0 else 0 if abs(x) == 1 else r)
            assert diff == expected, (r, x, diff, expected)
            checks += 1
    for x in (-11, -2, -1, 0, 1, 2, 20):
        q = {x: Fraction(1)}
        total_drift = Fraction(0)
        for t in range(16):
            m0 = sum(p * abs(y) for y, p in q.items())
            d = sum(p * (1 - int(abs(y) == 1)) for y, p in q.items())
            qnext = propagate(q, 1)
            m1 = sum(p * abs(y) for y, p in qnext.items())
            assert m1 - m0 == d
            total_drift += d
            assert m1 == abs(x) + total_drift
            q = qnext
            checks += 2
    for r in (2, 3, 7):
        for k in (0, 1, 3, 7):
            x = r * (2**(k+1)-1)
            q = {x:Fraction(1)}
            for t in range(20):
                assert sum(abs(y)*p for y,p in q.items()) == x + r*t
                q = propagate(q,r)
                checks += 1
    print(f'PASS: {checks} exact rational assertions on transitions, invariant masses, minorization, and finite-time drift')

if __name__ == '__main__':
    exact_tests()
