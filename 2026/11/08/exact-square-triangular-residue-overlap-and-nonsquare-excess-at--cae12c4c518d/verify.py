"""Exact integer verification of modular square/triangular image intersection counts."""
from fractions import Fraction
from math import isqrt


def factor(n):
    out = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            k = 0
            while n % d == 0:
                n //= d
                k += 1
            out.append((d, k))
        d += 1 if d == 2 else 2
    if n > 1:
        out.append((n, 1))
    return out


def chi(a, p):
    a %= p
    if not a:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def square_count_two(k):
    if k == 0:
        return 1
    return (2 ** (k - 1) + (5 if k % 2 else 4)) // 3


def divisible_square_count_odd(p, k):
    return 1 + sum((p - 1) * p ** (k - 2 * j - 1) // 2
                   for j in range(1, (k - 1) // 2 + 1))


def intersection_prime_power(p, k):
    if p == 2:
        return square_count_two(k)
    eps, eta = chi(2, p), chi(-2, p)
    generic = (p - 3 - eps - eta) // 4
    exceptional = 1 + (eta == 1)
    return p ** (k - 1) * generic + exceptional * divisible_square_count_odd(p, k)


def overlap(n):
    out = 1
    for p, k in factor(n):
        out *= intersection_prime_power(p, k)
    return out


def squares(n):
    return {x * x % n for x in range(n)}


def triangular(n):
    return {(x * (x + 1) // 2) % n for x in range(2 * n)}


def nonsquare_excess_prime(p):
    if p % 8 in (1, 5):
        return Fraction(p + 1, p + 3)
    if p % 8 == 3:
        return Fraction((p + 1) * (p - 3), (p - 1) * (p + 5))
    return Fraction(p + 1, p - 1)


def verify():
    count = 0
    for n in range(2, 2001):
        s, t = squares(n), triangular(n)
        got = len(s & t)
        assert got == overlap(n), (n, got, overlap(n))
        if n & (n - 1) == 0:
            assert len(t) == n, n
        if n % 2:
            assert len(s) == len(t), n
        count += 1
    prime_check = 0
    for p in range(3, 151, 2):
        if factor(p) != [(p, 1)]:
            continue
        s, t = squares(p), triangular(p)
        c = len(s & t)
        r = Fraction((len(t) - c) * len(s), c * (p - len(s)))
        assert r == nonsquare_excess_prime(p), (p, r, nonsquare_excess_prime(p))
        prime_check += 1
    prime_power_check = 0
    for p in [3, 5, 7, 11, 13, 17, 19]:
        k = 1
        while p ** k <= 30000:
            q = p ** k
            assert len(squares(q) & triangular(q)) == intersection_prime_power(p, k)
            k += 1
            prime_power_check += 1
    print('VERIFY_OK moduli=1999 prime_nonsquare_excess=%d prime_powers=%d exact_intersections=PASS dyadic_surjectivity=PASS CRT=PASS' % (prime_check, prime_power_check))

if __name__ == '__main__':
    verify()
