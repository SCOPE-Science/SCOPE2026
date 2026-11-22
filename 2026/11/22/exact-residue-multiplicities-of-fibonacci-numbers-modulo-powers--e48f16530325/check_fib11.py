"""Finite exact-arithmetic checks for the Fibonacci residue-fiber theorem.

Run: python check_fib11.py
No third-party dependencies. Finite checks do not replace the proof.
"""
from collections import Counter
from math import gcd

P = 11


def fib_reduced_first_ten():
    a, b = 0, 1
    out = []
    for _ in range(10):
        out.append(a)
        a, b = b, a + b
    return out


def kappa(k):
    """2/sqrt(5) modulo 11**k; choose square root congruent to 7."""
    s = 7
    for j in range(1, k):
        q = P**j
        s = next(s + q*d for d in range(P)
                 if (s + q*d)**2 % (P*q) == 5 % (P*q))
    return (2 * pow(s, -1, P**k)) % (P**k)


def root_count(e, z):
    """Number of square roots of z modulo 11**e, including e=0."""
    if e == 0:
        return 1
    z %= P**e
    if z == 0:
        return P**(e // 2)
    v = 0
    while z % P == 0:
        z //= P
        v += 1
    if v % 2:
        return 0
    if pow(z % P, (P - 1)//2, P) != 1:
        return 0
    return 2 * P**(v // 2)


def predicted(k, y, c, center):
    z = c[y % P]
    if k == 1:
        return z + (1 if y == 5 else 0)
    if (y - center) % (P*P) != 0:
        return z
    e = k - 2
    q = P**e
    gamma = (((y - center)//(P*P)) * pow(2, -1, q)) % q
    return z + P * root_count(e, gamma)


def check_level(k):
    modulus = P**k
    period = 10*P**(k - 1)
    observed = [0]*modulus
    a, b = 0, 1
    for _ in range(period):
        observed[a] += 1
        a, b = b, (a+b) % modulus
    assert (a, b) == (0, 1), (k, 'period does not close')
    # Explicitly rule out every proper subperiod by checking the state.
    for divisor in (2, 5, 11):
        if period % divisor:
            continue
        a, b = 0, 1
        for _ in range(period // divisor):
            a, b = b, (a+b) % modulus
        assert (a, b) != (0, 1), (k, divisor)
    init = fib_reduced_first_ten()
    c = Counter(init[i] % P for i in range(10) if i != 5)
    assert dict(c) == {0: 1, 1: 3, 2: 2, 3: 1, 8: 1, 10: 1}
    center = kappa(k)
    for y in range(modulus):
        expected = predicted(k, y, c, center)
        assert observed[y] == expected, (k, y, observed[y], expected)
    nonzero_count = sum(x > 0 for x in observed)
    square_count = 1 + sum(5 * P**(k - 2 - 2*j - 1)
                           for j in range((k - 2 + 1) // 2)) if k >= 2 else 0
    if k >= 2:
        assert nonzero_count == 6*P**(k-1) + square_count
    assert sum(observed) == period
    return (k, period, modulus, nonzero_count, max(observed))


if __name__ == '__main__':
    for level in range(1, 7):
        print('verified level, period, modulus, support, max-fiber:',
              *check_level(level))
    for e in range(1, 4):
        mod = P**e
        roots = Counter(t*t % mod for t in range(mod))
        for z in range(mod):
            assert roots[z] == root_count(e, z), (e, z)
        print('verified square-root count formula modulo', mod)
    print('ALL FINITE CHECKS PASSED')
