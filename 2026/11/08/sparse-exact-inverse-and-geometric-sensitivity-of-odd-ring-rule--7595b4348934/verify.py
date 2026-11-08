#!/usr/bin/env python3
"""Exact small-ring checks for inverse and inverse Boolean sensitivities of cyclic Rule 45."""
from collections import Counter

def rule45(x, n):
    y = 0
    for i in range(n):
        a = (x >> ((i - 1) % n)) & 1
        b = (x >> i) & 1
        c = (x >> ((i + 1) % n)) & 1
        t = 1 ^ a ^ c ^ (b & c)
        y |= t << i
    return y

def inv_coordinate(y, n, i):
    assert n % 2 == 1 and n >= 1
    m = (n - 1) // 2
    prefix = 1
    answer = 0
    for k in range(m + 1):
        odd = (y >> ((i + 2 * k + 1) % n)) & 1
        answer ^= prefix & (1 ^ odd)
        if k < m:
            prefix &= (y >> ((i + 2 * k + 2) % n)) & 1
    return answer

def inverse(y, n):
    return sum(inv_coordinate(y, n, i) << i for i in range(n))

def expected_influence(n, j):
    m = (n - 1)//2
    if n == 1:
        return 2
    if j == 1:
        return 1 << n
    if j == 0:
        return 1 << (n-m)
    return 1 << (n - (j//2))

def anf_coeffs(v, n):
    coeff = v[:]
    for j in range(n):
        for mask in range(1<<n):
            if mask & (1<<j):
                coeff[mask] ^= coeff[mask ^ (1<<j)]
    return coeff

def main():
    rounds = 0
    tested = 0
    for n in range(1, 16, 2):
        q = 1 << n
        inverse_table = [inverse(y, n) for y in range(q)]
        assert set(inverse_table) == set(range(q))
        for y in range(q):
            x = inverse_table[y]
            assert rule45(x, n) == y, (n, y, x)
        for j in range(n):
            count = sum(((inverse_table[y] ^ inverse_table[y^(1<<j)]) & 1) != 0 for y in range(q))
            assert count == expected_influence(n, j), (n, j, count, expected_influence(n,j))
            tested += 1
        if n <= 13:
            coeff = anf_coeffs([x & 1 for x in inverse_table], n)
            m = (n-1)//2
            # Construct the two monomials from each factor in the inverse formula.
            support = set()
            prefix = 0
            for k in range(m+1):
                support.add(prefix)
                support.add(prefix | (1<<((2*k+1)%n)))
                if k < m:
                    prefix |= (1<<((2*k+2)%n))
            assert {a for a, b in enumerate(coeff) if b} == support, n
            assert len(support) == n+1
            assert max(z.bit_count() for z in support) == m+1
        rounds += 1
    print(f"VERIFY_OK odd_sizes={rounds} single_bit_checks={tested} n_max=15")

if __name__ == '__main__':
    main()
