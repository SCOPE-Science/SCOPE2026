"""Reproducible integer and modular checks for balancing-power window sums.

No finite test is used as a proof of the unrestricted assertion.
"""
from math import gcd


def sequence(n, modulus=None):
    values = [0, 1]
    for _ in range(n - 1):
        value = 6 * values[-1] - values[-2]
        if modulus:
            value %= modulus
        values.append(value)
    return values[:n + 1]


def valuation(a, p=5):
    if a == 0:
        raise ValueError('zero has no finite valuation')
    result = 0
    while a % p == 0:
        result += 1
        a //= p
    return result


def exact_gcd_test():
    checks = 0
    for exponent in (2, 4, 6, 8, 10, 12):
        values = sequence(190)
        powers = [v ** exponent for v in values]
        pref = [0]
        for a in powers:
            pref.append(pref[-1] + a)
        for length in range(1, 146):
            g = 0
            for start in range(exponent + 1):
                g = gcd(g, pref[start + length + 1] - pref[start + 1])
            expected = valuation(length) if length % 3 == 0 else 0
            assert valuation(g) == expected, (exponent, length, g, expected)
            checks += 1
    return checks


def modular_test():
    checks = 0
    modulus = 5 ** 6
    maxlen = 3 * 5 ** 5
    values = sequence(maxlen + 22, modulus)
    for exponent in [2, 4, 6, 8, 10, 12, 14, 20, 30, 50, 100]:
        powers = [pow(x, exponent, modulus) for x in values]
        prefix = [0]
        for a in powers:
            prefix.append((prefix[-1] + a) % modulus)
        for r in range(6):
            length = 3 * (5 ** r)
            mod = 5 ** (r + 1)
            for start in range(16):
                observed = (prefix[start + length + 1] - prefix[start + 1]) % mod
                assert observed == (2 * 5 ** r) % mod, (exponent, r, start, observed)
                checks += 1
        for length in range(1, 201):
            if length % 3:
                continue
            r = valuation(length)
            mod = 5 ** (r + 1)
            for start in range(6):
                observed = (prefix[start + length + 1] - prefix[start + 1]) % mod
                assert observed == (2 * length // 3) % mod, (exponent, length, start)
                checks += 1
    return checks


def matrix_test():
    checks = 0
    for r in range(6):
        modulus = 5 ** (r + 1)
        B = sequence(3 * 5 ** r + 2, modulus)
        # (B_{n+1},B_n) is transformed by M^{3*5^r}=-I mod 5^{r+1}.
        length = 3 * 5 ** r
        for n in (0, 1, 2):
            assert (B[n + length] + B[n]) % modulus == 0
            checks += 1
    return checks


if __name__ == '__main__':
    a, b, c = exact_gcd_test(), modular_test(), matrix_test()
    print(f'PASS: exact integer GCD checks={a}; modular window congruences={b}; matrix shifts={c}; total={a+b+c}')
