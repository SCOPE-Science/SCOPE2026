#!/usr/bin/env python3
"""Exact finite consistency checks for parity-restricted geometric-sum gcds."""
from math import gcd


def R(b, k, h):
    return (pow(b, k * h) - 1) // (pow(b, h) - 1)


def odd_formula(b, k):
    t = k // (k & -k)
    return ((pow(b, k) - 1) // (pow(b, t) - 1)) * gcd(
        t, (pow(b, t) - 1) // (b - 1)
    )


def even_formula(b, k):
    return gcd(k, (pow(b, 2 * k) - 1) // (b * b - 1))


def run():
    cases = odd_checks = even_checks = 0
    for b in range(2, 11):
        for k in range(2, 41):
            t = k // (k & -k)
            want_odd = odd_formula(b, k)
            want_even = even_formula(b, k)
            assert gcd(R(b, k, 1), R(b, k, t)) == want_odd
            g_odd = g_even = 0
            for h in range(1, 2 * k + 2, 2):
                g_odd = gcd(g_odd, R(b, k, h))
                odd_checks += 1
                assert g_odd % want_odd == 0
            for h in range(2, 2 * k + 3, 2):
                g_even = gcd(g_even, R(b, k, h))
                even_checks += 1
                assert g_even % want_even == 0
            # The finite ranges include both theoretical witnesses for odd widths.
            assert g_odd == want_odd
            # The even-width reduction's finite gcd must stabilize to the formula.
            assert g_even == want_even
            cases += 1
    assert odd_formula(2, 4) == 15 and even_formula(2, 4) == 1
    assert odd_formula(2, 2) == 3 and even_formula(2, 2) == 1
    print(f'VERIFY_OK parameter_pairs={cases} odd_width_terms={odd_checks} '
          f'even_width_terms={even_checks} binary_k4_odd=15_even=1')

if __name__ == '__main__':
    run()
