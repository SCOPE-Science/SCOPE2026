#!/usr/bin/env python3
"""Exact finite verification of a prime-power Jacobsthal fiber theorem.

The proof is independent of this script. The script needs only standard Python 3.
"""
from collections import Counter


def is_prime(n):
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


def distinct_factors(n):
    ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ans.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        ans.append(n)
    return ans


def primitive_mod_power(a, p, r):
    q = p ** r
    order = (p - 1) * p ** (r - 1)
    return (a % p != 0 and pow(a, order, q) == 1
            and all(pow(a, order // t, q) != 1 for t in distinct_factors(order)))


def legendre(x, p):
    y = pow(x % p, (p - 1) // 2, p)
    return 0 if y == 0 else (1 if y == 1 else -1)


def c_value(p):
    u, v = legendre(2, p), legendre(-2, p)
    assert (p - 1 - u + v) % 4 == 0
    return (p - 1 - u + v) // 4


def check(p, r, a):
    q = p ** r
    T = (p - 1) * p ** (r - 1)
    assert primitive_mod_power(a, p, r)
    assert (a + 1) % p != 0
    a0, a1 = 0, 1
    actual = [0] * q
    for n in range(T):
        actual[a0] += 1
        a0, a1 = a1, ((a - 1) * a1 + a * a0) % q
    assert (a0, a1) == (0, 1)
    expected = [int(legendre(1 + (a + 1) * y, p) == 1) +
                int(legendre((a + 1) * y - 1, p) == -1)
                for y in range(q)]
    assert actual == expected, ('target mismatch', p, r, a)
    histogram = Counter(actual)
    c = c_value(p)
    assert histogram == {0: (c + 1) * p ** (r - 1),
                         1: (p - 1 - 2 * c) * p ** (r - 1),
                         2: c * p ** (r - 1)}, (p, r, a, histogram)
    count_characters = sum(legendre(z + 1, p) == 1 and
                           legendre(z - 1, p) == -1 for z in range(p))
    assert count_characters == c, (p, c)
    if r > 1:
        lower = p ** (r - 1)
        for j in range(lower):
            assert actual[j] == actual[j + lower]
    return q, T


def main():
    cases = 0
    targets = 0
    sequence_terms = 0
    for p in range(5, 48):
        if not is_prime(p):
            continue
        # A primitive root modulo p^2 is primitive at every p-power.
        candidates = [a for a in range(2, p * p) if primitive_mod_power(a, p, 2)]
        assert candidates
        for a in candidates[:2]:
            for r in (1, 2, 3):
                if p ** r > 100000:
                    continue
                q, T = check(p, r, a)
                cases += 1
                targets += q
                sequence_terms += T
    print('VERIFY_OK', f'cases={cases}', f'targets={targets}',
          f'sequence_terms={sequence_terms}')


if __name__ == '__main__':
    main()
