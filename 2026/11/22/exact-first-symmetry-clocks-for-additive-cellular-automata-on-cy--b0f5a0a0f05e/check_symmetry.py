#!/usr/bin/env python3
"""Independent finite exhaustive verifier for a spatial-symmetry first-passage theorem.
Uses only the Python standard library.  This does not replace the infinite proof.
"""
from collections import Counter
from itertools import product


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n):
    ans, t = 1, n
    for p in range(2, n + 1):
        if p * p > t:
            break
        if t % p == 0:
            t //= p
            ans = -ans
            if t % p == 0:
                return 0
            while t % p == 0:
                t //= p
        if t == 1:
            break
    return -ans if t > 1 else ans


def radical(n):
    return sum(0 for _ in []) + __import__('math').prod(p for p in range(2, n + 1)
         if n % p == 0 and all(p % d for d in range(2, __import__('math').isqrt(p) + 1)))


def predicted(q, p, n):
    primitive = sum(mobius(n // d) * q**d for d in divisors(n))
    result = {0: q**n - primitive}
    a, m = 0, n
    while m % p == 0:
        a += 1
        m //= p
    if not a:
        result['infinite'] = primitive
        return result
    L = (p - 1) * p**(a - 1)
    H = sum(mobius(r) * q**(n // (p * r)) for r in divisors(radical(m)))
    for t in range(1, L + 1):
        result[t] = (q - 1) * q**(t - 1) * H
    result['infinite'] = primitive - (q**L - 1) * H
    return result


def field_sub(x, y, p, h):
    out, multiplier = 0, 1
    for _ in range(h):
        out += ((x % p) - (y % p)) % p * multiplier
        x //= p
        y //= p
        multiplier *= p
    return out


def first_symmetry(x, p, h):
    n = len(x)
    seen, t = set(), 0
    while True:
        if any(all(x[i] == x[(i + d) % n] for i in range(n))
               for d in range(1, n)):
            return t
        tup = tuple(x)
        if tup in seen:
            return 'infinite'
        seen.add(tup)
        x = tuple(field_sub(x[i], x[(i + 1) % n], p, h) for i in range(n))
        t += 1


def test():
    cases = [(2, 1, range(2, 13)), (3, 1, range(2, 9)),
             (2, 2, range(2, 7)), (3, 2, range(2, 5))]
    total_configs = 0
    for p, h, sizes in cases:
        q = p**h
        for n in sizes:
            counted = Counter(first_symmetry(x, p, h)
                              for x in product(range(q), repeat=n))
            expected = {t: count for t, count in predicted(q, p, n).items()
                        if count != 0}
            assert dict(counted) == expected, (q, n, dict(counted), expected)
            assert sum(counted.values()) == q**n
            total_configs += q**n
            print('PASS q=%d n=%d: %s' % (q, n, str(dict(counted))))
    print('ALL PASS: %d field/ring cases, %d initial configurations' %
          (sum(len(sizes) for _, _, sizes in cases), total_configs))


if __name__ == '__main__':
    test()
