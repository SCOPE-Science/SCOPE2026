#!/usr/bin/env python3
"""Exact arithmetic verification of five-primary Fibonacci power-window identities."""
from math import gcd


def valuation_five(value):
    count = 0
    while value > 0 and value % 5 == 0:
        value //= 5
        count += 1
    return count


def expected_valuation(k):
    r = 0
    while k % 5 == 0:
        r += 1
        k //= 5
    return max(0, r - 1)


def fibonacci_mod(length, modulus):
    out = [0, 1]
    for _ in range(length - 2):
        out.append((out[-1] + out[-2]) % modulus)
    return out[:length]


def test_block_congruences():
    checked = 0
    for exponent in (4, 8, 12, 20):
        for r in range(1, 6):
            modulus = 5**r
            starts = 30
            numbers = fibonacci_mod(modulus + starts, modulus)
            fourth = [pow(v, exponent, modulus) for v in numbers]
            running = sum(fourth[:modulus]) % modulus
            for n in range(starts):
                if n:
                    running = (running - fourth[n - 1] + fourth[n + modulus - 1]) % modulus
                assert running == (-5**(r - 1)) % modulus, (exponent, r, n, running)
                checked += 1
    return checked


def test_exact_window_gcds():
    checked = 0
    for exponent, max_k in ((4, 650), (8, 230), (12, 145), (20, 95)):
        f = [0, 1]
        for _ in range(max_k + exponent + 2):
            f.append(f[-1] + f[-2])
        powers = [z**exponent for z in f]
        for k in range(1, max_k + 1):
            window = sum(powers[:k])
            g = 0
            for n in range(exponent + 1):
                if n:
                    window += powers[n + k - 1] - powers[n - 1]
                g = gcd(g, window)
            assert valuation_five(g) == expected_valuation(k), (exponent, k, g)
            checked += 1
    return checked


def main():
    a = ((0, 1), (1, 1))
    power = ((1, 0), (0, 1))
    for _ in range(5):
        power = tuple(tuple(sum(power[i][h] * a[h][j] for h in range(2))
                            for j in range(2)) for i in range(2))
    assert power == ((3, 5), (5, 8)), power
    blocks = test_block_congruences()
    gcds = test_exact_window_gcds()
    print(f"PASS: {blocks} universal block-congruence checks")
    print(f"PASS: {gcds} exact finite-window GCD checks")
    print("All checks use only Python's integer arithmetic.")


if __name__ == '__main__':
    main()
