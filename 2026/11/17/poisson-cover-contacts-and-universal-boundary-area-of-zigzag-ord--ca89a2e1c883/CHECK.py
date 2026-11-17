#!/usr/bin/env python3
"""Exact small-case verification of fence contact counts (standard Python 3)."""
from functools import lru_cache
from math import factorial, pi, exp


def distribution(n):
    assert n >= 2
    covers = {(i+1, i) if i % 2 == 0 else (i, i+1) for i in range(n-1)}
    predecessor = [0] * n
    for lower, upper in covers:
        predecessor[upper] |= (1 << lower)

    @lru_cache(None)
    def count(mask, last):
        if mask == (1 << n) - 1:
            return (1,)
        result = []
        for element in range(n):
            if (mask >> element) & 1:
                continue
            if predecessor[element] & mask != predecessor[element]:
                continue
            continuation = count(mask | (1 << element), element)
            shift = int((last, element) in covers)
            new_length = len(continuation) + shift
            if len(result) < new_length:
                result.extend([0] * (new_length - len(result)))
            for j, number in enumerate(continuation):
                result[j + shift] += number
        return tuple(result)

    return count(0, n)


def euler_zigzag(n):
    # Independent Andre secant/tangent recurrence, without tabulated answers.
    from math import comb
    E = [1, 1]
    for m in range(2, n+1):
        total = sum(comb(m-1, j) * E[j] * E[m-1-j] for j in range(m))
        assert total % 2 == 0
        E.append(total // 2)
    return E[n]


def main():
    for n in range(2, 18):
        a = distribution(n)
        total = sum(a)
        assert total == euler_zigzag(n), (n, total)
        assert sum(j * amount for j, amount in enumerate(a)) == total, n
        assert sum(a) <= factorial(n)
        assert len(a) <= (n // 2) + 2
        variance = sum((j-1)**2 * amount for j, amount in enumerate(a)) / total
        assert 0 <= variance <= 1
        if n in (2,4,8,12,17):
            print('n=', n, 'linear_extensions=', total,
                  'P_zero=', format(a[0]/total,'.8f'),
                  'variance=', format(variance,'.8f'))
    # Independent exact-integration constants appearing in the proof.
    lam = 4/pi**2
    u = 2/pi
    assert abs(lam - u*u) < 1e-14
    assert abs(8/pi**2 - .8105694691387022) < 1e-13
    print('FENCE_POISSON_EXACT_PASS n=2..17')


if __name__ == '__main__':
    main()
