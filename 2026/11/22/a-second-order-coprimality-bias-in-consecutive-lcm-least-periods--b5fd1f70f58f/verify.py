"""Finite diagnostics for the coprimality-bias theorem.

Uses only Python's standard library; not a proof of any asymptotic.
"""
import math


def lcm(a, b):
    return a // math.gcd(a, b) * b


def raw_g(k, n):
    product = 1
    common = 1
    for a in range(n, n + k + 1):
        product *= a
        common = lcm(common, a)
    return product // common


def factors(n):
    result = {}
    d = 2
    while d * d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                e += 1
                n //= d
            result[d] = e
        d += 1
    if n > 1:
        result[n] = 1
    return result


def defect(k):
    result = 1
    for p, exponent in factors(k + 1).items():
        a = 0
        power = p
        while power <= k:
            power *= p
            a += 1
        if a > 0 and exponent >= a:
            assert result == 1  # unique omitted prime, from the period theorem
            result = p ** a
    return result


def brute_period(k):
    L = 1
    for j in range(1, k + 1):
        L = lcm(L, j)
    values = [raw_g(k, n) for n in range(1, 2 * L + 1)]
    for d in range(1, L + 1):
        if L % d == 0 and all(values[n] == values[n + d] for n in range(L)):
            return L // d
    raise AssertionError('No period divisor found')


def main():
    for k in range(1, 9):
        assert defect(k) == brute_period(k), (k, defect(k), brute_period(k))
    N = 12000
    exceptional = []
    for k in range(1, N + 1):
        D = defect(k)
        if D > 1:
            exceptional.append(k + 1)
            q = max(factors(k + 1))
            if q * q >= k + 1:
                assert D == q, (k, D, q)
    for modulus in (2, 3, 4, 5, 6, 10):
        phi = sum(math.gcd(i, modulus) == 1 for i in range(1, modulus + 1))
        count = sum(math.gcd(n, modulus) == 1 for n in exceptional)
        base = phi * len(exceptional) / modulus
        constant = phi / modulus * sum(
            math.log(p) / (p - 1) for p in factors(modulus)
        ) - (1 - phi / modulus)
        print(f'q={modulus}: centered={count-base:+.1f}, '
              f'scaled={(count-base)*math.log(N)/N:+.5f}, '
              f'limit={constant:+.5f}')
    print('FARHI_LOCAL_BIAS_FINITE_CHECK_OK 8 12000 6')


if __name__ == '__main__':
    main()
