#!/usr/bin/env python3
"""Exact independent modular checks for a valuation classification of the FiboLaplace sequence."""
P = 971
MOD = P * P


def recurrence_mod(limit, modulus):
    e = [0] * (limit + 1)
    e[1] = e[2] = 1
    for n in range(3, limit + 1):
        e[n] = ((n - 1) * e[n - 1] - e[n - 2] + 1 - (-1) ** n) % modulus
    return e


def direct_even_a(a, modulus):
    if a == 0:
        return 1
    s, prod = 1, 1
    for j in range(1, a):
        prod = prod * (a * a - j * j) % modulus
        s = (s + prod) % modulus
    return s


def direct_odd_b(a, modulus):
    s, prod = 1, 1
    for j in range(1, a + 1):
        s = (s + a * (a + j) * prod) % modulus
        prod = prod * (a * a - j * j) % modulus
    return s


def fixed_polynomial(m, modulus):
    s, prod = 1, 1
    for j in range(1, P):
        prod = prod * (m * m - j * j) % modulus
        s = (s + prod) % modulus
    return s


def v_p_mod(x, p, upper):
    if x == 0:
        return upper
    v = 0
    while v < upper and x % p == 0:
        x //= p
        v += 1
    return v


def predicted(n):
    r = n % (2 * P)
    if r in (388, 1554):
        return 1
    if r == 0:
        x = n
        v = 0
        while x % P == 0:
            x //= P
            v += 1
        return v
    return 0


def main():
    e = recurrence_mod(4 * P + 1, MOD)
    roots = [r for r in range(1, 2 * P + 1) if e[r] % P == 0]
    assert roots == [388, 1554, 1942], roots
    direct_comparisons = 0
    for a in range(P):
        assert direct_odd_b(a, P) == e[2 * a + 1] % P
        direct_comparisons += 1
        if a:
            assert a * direct_even_a(a, P) % P == e[2 * a] % P
            direct_comparisons += 1
    assert e[2 * P] % P == 0

    certificate = {}
    for r in (388, 1554):
        a = r // 2
        assert e[r] % P == 0 and e[r] % MOD != 0
        assert e[r + 2 * P] == e[r]
        s = fixed_polynomial(a, MOD)
        shifted = fixed_polynomial(a + P, MOD)
        assert s == shifted == 459283
        assert s * a % MOD == e[r]
        assert shifted * (a + P) % MOD == e[r + 2 * P]
        certificate[r] = (e[r], s)
    beta = fixed_polynomial(0, P)
    assert beta == 383
    assert e[2 * P] // P == beta

    # The independent recurrence also checks entire initial blocks modulo p^3.
    upper = 2 * P * P
    e_large = recurrence_mod(upper, P ** 3)
    for n in range(1, upper + 1):
        want = predicted(n)
        assert v_p_mod(e_large[n], P, 3) == want, (n, e_large[n], want)
    print('CYCLE_ROOTS', roots)
    print('DIRECT_PRODUCT_COMPARISONS', direct_comparisons)
    print('TERMINAL_CERTIFICATES', certificate)
    print('DISTINGUISHED_UNIT', beta)
    print('INDEPENDENT_RECURSION_RANGE', upper)
    print('VERIFY_OK exhaustive_root_census=yes exact_modular_arithmetic=yes')


if __name__ == '__main__':
    main()
