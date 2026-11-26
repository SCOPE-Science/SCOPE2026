#!/usr/bin/env python3
"""Verify the sharpness criterion for Calkin's binary-digit divisibility bound.
No external packages; finite tests corroborate, rather than prove, the theorem.
"""
from math import comb


def digit_sum(n):
    return n.bit_count()


def val_two(n):
    assert n > 0
    return (n & -n).bit_length() - 1


def franel_recurrence(limit):
    out = [1, 2]
    for n in range(1, limit):
        numerator = (7*n*n + 7*n + 2) * out[-1] + 8*n*n*out[-2]
        denominator = (n+1)**2
        assert numerator % denominator == 0
        out.append(numerator // denominator)
    return out[:limit+1]


def franel_strehl(n):
    return sum(comb(n, 2*j)*comb(2*j, j)*comb(2*(n-j), n-j)
               for j in range(n//2+1))


def verify():
    f = franel_recurrence(6000)
    assert f[:8] == [1, 2, 10, 56, 346, 2252, 15184, 104960]
    for n in range(0, 6001):
        s = digit_sum(n)
        neighbor_count = (n & (n >> 1)).bit_count()
        required_odd = neighbor_count == 0
        assert f[n] % (1 << s) == 0
        assert ((f[n] >> s) & 1) == int(required_odd)
        if n <= 100:
            assert f[n] == sum(comb(n, k)**3 for k in range(n+1))
            assert f[n] == franel_strehl(n)
            min_parity_count = 0
            for j in range(n//2+1):
                term = comb(n, 2*j)*comb(2*j, j)*comb(2*(n-j), n-j)
                assert val_two(term) >= s
                is_minimal = val_two(term) == s
                expected_minimal = ((j & ~n) == 0) and (((j << 1) & ~n) == 0)
                assert is_minimal == expected_minimal
                min_parity_count += is_minimal
            assert min_parity_count == 2**neighbor_count
    fibonacci=[0,1]
    for l in range(1,18):
        fibonacci.append(fibonacci[-1]+fibonacci[-2])
    for L in range(1,14):
        actual = sum((n & (n >> 1)) == 0 for n in range(1, 1<<L))
        assert actual == fibonacci[L+2]-1
    print('VERIFY_OK: 6001 exact recurrence valuations; 101 exact binomial-cube/Strehl identities; 2601 termwise valuation and bit-mask equivalences; 13 independent Fibonacci counting cutoffs')


if __name__ == '__main__':
    verify()
