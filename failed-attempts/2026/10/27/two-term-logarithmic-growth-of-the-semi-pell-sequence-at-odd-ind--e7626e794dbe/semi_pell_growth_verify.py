#!/usr/bin/env python3
"""Finite consistency tests for odd-index semi-Pell growth estimates.
No finite test is used as a proof of the asymptotic statement.
"""
import math


def recurrence_table(limit):
    a = [0] * (limit + 1)
    a[1] = 1
    for n in range(2, limit + 1):
        a[n] = a[n // 2] if n % 2 == 0 else 2 * a[n - 1] + a[n - 2]
    return a


def overpartition_table(limit):
    # B counts configurations of optional odd-multiplicity sizes,
    # with two marking choices for each included size.
    B = [0] * (limit + 1)
    B[0] = 1
    F = [0] * (limit + 1)
    size = 1
    while size <= limit:
        # Exactly one mandatory largest size, marked; its multiplicity is odd.
        for m in range(size, limit + 1, 2 * size):
            for v in range(limit - m + 1):
                F[v + m] += B[v]
        # Convert the level into an optional size for larger maximum levels.
        nxt = B[:]
        for m in range(size, limit + 1, 2 * size):
            for v in range(limit - m + 1):
                nxt[v + m] += 2 * B[v]
        B = nxt
        size *= 2
    return F


def lower_count(k):
    r = k - math.ceil(math.log2(k)) - 2
    if r < 1:
        return 0
    ans = 1
    for i in range(1, r + 1):
        ans *= (1 + (1 << (k - i)) // (8 * k))
    return ans


def main():
    limit = 512
    a = recurrence_table(limit)
    b = overpartition_table(limit)
    assert a == b, next((n, a[n], b[n]) for n in range(limit+1) if a[n] != b[n])
    assert all(a[i] < a[i+2] for i in range(1, limit-2, 2))
    N = (1 << 19) - 1
    long_a = recurrence_table(N)
    print('overpartition-bijection small test: 512 coefficients equal')
    print('odd-index monotonicity test: passed')
    for k in range(8, 20):
        value = long_a[(1 << k) - 1]
        count = lower_count(k)
        assert count <= value
        # Coarse elementary coefficient bound on overpartitions.
        assert value <= (1 << (k * (k + 1) // 2 + 2 * k))
        ratio = (math.log2(value) - (k * k / 2 - k * math.log2(k))) / k
        print(f'k={k:2d}; lower-construction={count}; log2(value)={math.log2(value):.6f}; normalized-remainder={ratio:.6f}')
    print('tested lower injection bound and coarse upper bound for k=8..19')


if __name__ == '__main__':
    main()
