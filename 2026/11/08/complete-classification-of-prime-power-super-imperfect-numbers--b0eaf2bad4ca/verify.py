#!/usr/bin/env python3
"""Exact supplementary checks for prime-power super-imperfect classification.

No probabilistic primality tests, external dependencies, or assumptions that a
finite search proves the unrestricted result. See RESULT.md for the proof.
"""

def factor(n):
    factors = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            a = 0
            while n % d == 0:
                n //= d
                a += 1
            factors.append((d, a))
        d = 3 if d == 2 else d + 2
    if n > 1:
        factors.append((n, 1))
    return factors


def beta_prime_power(p, a):
    return sum((-1) ** (a - j) * p ** j for j in range(a + 1))


def beta(n):
    ans = 1
    for p, a in factor(n):
        ans *= beta_prime_power(p, a)
    return ans


def is_prime(n):
    return n >= 2 and factor(n) == [(n, 1)]


def main():
    assert beta(1) == 1
    # Direct, independently factored iterates of beta(2^a).
    found = []
    for a in range(1, 25):
        n = 1 << a
        if 2 * beta(beta(n)) == n:
            found.append(a)
    assert found == [1, 2, 3, 7, 15], found

    # A further witness beyond the direct interval, with explicit factorization.
    m31 = ((1 << 32) - 1) // 3
    assert factor(m31) == [(5, 1), (17, 1), (257, 1), (65537, 1)]
    assert 2 * beta(m31) == 1 << 31

    # Check prime-power beta fibers for small primes and all exponents <= 15.
    local_tests = 0
    for p in range(3, 150, 2):
        if not is_prime(p):
            continue
        for e in range(1, 16):
            b = beta_prime_power(p, e)
            pure = (b & (b - 1)) == 0
            expected = e == 1 and ((p - 1) & (p - 2)) == 0
            assert pure == expected, (p, e, b)
            local_tests += 1

    Fermat = [1 + (1 << (1 << j)) for j in range(6)]
    assert all(is_prime(Fermat[j]) for j in range(5))
    assert Fermat[5] == 641 * 6700417
    for t in range(1, 6):
        a = (1 << t) - 1
        m = ((1 << (a + 1)) - 1) // 3
        prod = 1
        for j in range(1, t):
            prod *= Fermat[j]
        assert m == prod
        assert beta(m) == 1 << (a - 1)
    print('VERIFY_OK direct_exponents=1..24 solutions=' + str(found)
          + ' extra_exponent=31 PASS local_odd_prime_power_tests=' + str(local_tests)
          + ' Fermat_primality_F0..F4=PASS F5_composite=PASS')


if __name__ == '__main__':
    main()
