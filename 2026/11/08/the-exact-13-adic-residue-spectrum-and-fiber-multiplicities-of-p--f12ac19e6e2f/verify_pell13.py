#!/usr/bin/env python3
"""Independent finite checks of the Pell sequence at prime 13.

No external dependencies. Tests corroborate, but do not establish, the
infinite 13-adic image classification proved in RESULT.md.
"""
from collections import Counter

P = 13
S = {0, 1, 2, 5, 12, 29, 70, 99, 140, 157, 164, 167, 168}
M = (2, 1, 1, 0)


def matrix_mul(a, b, modulus):
    return ((a[0]*b[0]+a[1]*b[2]) % modulus,
            (a[0]*b[1]+a[1]*b[3]) % modulus,
            (a[2]*b[0]+a[3]*b[2]) % modulus,
            (a[2]*b[1]+a[3]*b[3]) % modulus)


def matrix_power(a, exponent, modulus):
    ans = (1, 0, 0, 1)
    while exponent:
        if exponent % 2:
            ans = matrix_mul(ans, a, modulus)
        a = matrix_mul(a, a, modulus)
        exponent //= 2
    return ans


def pell_fast(n, modulus):
    return matrix_power(M, n, modulus)[1]


def valuation(number, p):
    if number == 0:
        raise ValueError('Valuation of zero is not finite')
    number = abs(number)
    ans = 0
    while number % p == 0:
        number //= p
        ans += 1
    return ans


def verify():
    assert matrix_power(M, 4, 13) == (3, 12, 12, 5)
    assert matrix_power(M, 7, 13) == (5, 0, 0, 5)
    assert matrix_power(M, 14, 13) == (12, 0, 0, 12)
    assert matrix_power(M, 28, 13**3) == (1015, 1014, 1014, 1184)
    base = [pell_fast(r, 169) for r in range(28)]
    assert set(base) == S
    cbase = Counter(base)
    assert cbase[0] == 4 and all(cbase[s] == 2 for s in S if s)
    assert sorted(set(a % 13 for a in base)) == [0, 1, 2, 3, 5, 8, 10, 11, 12]
    max_period = 0
    for k in range(1, 7):
        modulus = 13**k
        period = 28 if k == 1 else 28 * 13**(k - 2)
        max_period = period
        counts = Counter()
        a, b = 0, 1
        for _ in range(period):
            counts[a] += 1
            a, b = b, (2 * b + a) % modulus
        assert (a, b) == (0, 1)
        if k == 1:
            assert len(counts) == 9
        else:
            assert len(counts) == 13**(k - 1)
            assert sum(counts.values()) == period
            assert all((v % 169) in S for v in counts)
            assert all(counts[v] == (4 if v % 169 == 0 else 2) for v in counts)
            # Every allowed class is realized; comparison is of full finite sets.
            assert set(counts) == {s + 169*j for s in S for j in range(13**(k-2))}
    # Verify the exact valuation formula in many bounded instances.  The modulus
    # 13**10 is sufficient for these differences, including shifts by 13**3.
    mod = 13**10
    checked = 0
    for r in range(28):
        for u in (0, 1, 2, 13, 27, 169, 175, 13**3):
            for v in (3, 4, 14, 170, 13**3 + 1):
                if u == v:
                    continue
                difference = (pell_fast(r + 28*u, mod) - pell_fast(r + 28*v, mod)) % mod
                expected = 2 + valuation(u - v, 13)
                assert difference % 13**expected == 0
                assert difference % 13**(expected + 1) != 0
                checked += 1
    print('VERIFY_OK levels=1..6 max_period=%d image_size_k6=%d base_classes=%d isometry_pairs=%d' %
          (max_period, 13**5, len(S), checked))


if __name__ == '__main__':
    verify()
