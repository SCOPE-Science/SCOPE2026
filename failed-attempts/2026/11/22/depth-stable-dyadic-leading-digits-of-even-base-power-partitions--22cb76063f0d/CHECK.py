#!/usr/bin/env python3
"""Independent finite residue check of the even-base m-ary partition law.

Computes partition counts directly from b(n)=b(n-1)+[m|n]b(n/m).
This does not rely on the proof's polynomial summation operator.
"""
from collections import defaultdict

CASES = {
    2: (11, 14),
    4: (7, 12),
    6: (5, 12),
    8: (5, 12),
    10: (4, 12),
    12: (4, 12),
    14: (4, 12),
    16: (4, 12),
    18: (3, 12),
    20: (3, 12),
}


def check_base(m, last_r, max_n):
    a = 0
    mm = m
    while mm % 2 == 0:
        a += 1
        mm //= 2
    largest = max_n * m ** last_r
    exp = 1 + (last_r - 1) * (a - 1)
    modulus = 1 << (exp + 1)
    b = [1] * largest
    for j in range(1, largest):
        b[j] = (b[j - 1] + (b[j // m] if j % m == 0 else 0)) % modulus
    # RHS is the parity of the binomial-weighted convolution with ordinary partition values.
    rhs = [0] * (max_n + 1)
    for n in range(1, max_n + 1):
        rhs[n] = sum(j * (b[n - j] & 1) for j in range(1, n + 1)) & 1
    tests = 0
    odd_witnesses = 0
    for r in range(2, last_r + 1):
        e = 1 + (r - 1) * (a - 1)
        d = 1 << e
        for n in range(1, max_n + 1):
            val = b[m ** r * n - 1]
            assert val % d == 0, (m, r, n, 'divisibility', val)
            assert (val // d) % 2 == rhs[n], (m, r, n, 'parity')
            tests += 1
            odd_witnesses += (n == 1)
            if n == 1:
                assert rhs[n] == 1
    return tests, odd_witnesses, largest, [rhs[n] for n in range(1, min(max_n, 8) + 1)]


def main():
    test_count = 0
    witness_count = 0
    for m, (r, n) in CASES.items():
        tests, witnesses, largest, bits = check_base(m, r, n)
        print('base', m, 'depths 2..', r, 'n 1..', n,
              'checks', tests, 'bound', largest, 'leading parities', ''.join(map(str, bits)))
        test_count += tests
        witness_count += witnesses
    print('PASS', test_count, 'complete sample parameter/target checks;',
          witness_count, 'sharp n=1 witnesses.')
    print('Universality for arbitrary even bases/depths follows from the polynomial proof.')


if __name__ == '__main__':
    main()
