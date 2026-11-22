"""Exact checks for fixed-point incidence Walsh multipliers of involutions.

Public, standalone Python 3 script: no third-party dependencies.
"""
from collections import Counter
from math import comb


def all_involutions_fixed_sets(n):
    """Recursively enumerate involution fixed point masks, independently of Fourier formulas."""
    def rec(remaining, fixed):
        if not remaining:
            yield fixed
            return
        first = remaining[0]
        rest = remaining[1:]
        yield from rec(rest, fixed | (1 << first))
        for j, other in enumerate(rest):
            yield from rec(rest[:j] + rest[j + 1:], fixed)
    yield from rec(tuple(range(n)), 0)


def fwht(values):
    out = values[:]
    stride = 1
    while stride < len(out):
        for i in range(0, len(out), 2 * stride):
            for j in range(i, i + stride):
                a, b = out[j], out[j + stride]
                out[j], out[j + stride] = a + b, a - b
        stride *= 2
    return out


def counts(max_n):
    ans = [1, 1]
    for n in range(2, max_n + 1):
        ans.append(ans[n - 1] + (n - 1) * ans[n - 2])
    return ans


def alternating_binomial(n, k, telephone):
    return sum(comb(k, j) * (-2) ** j * telephone[n - j] for j in range(k + 1))


def central_moments(max_m):
    a = [1, 0]
    for m in range(1, max_m):
        a.append(2 * m * (a[m] + a[m - 1]))
    return a


def check():
    tel = counts(60)
    moments = central_moments(31)
    assert moments[:8] == [1, 0, 2, 8, 60, 544, 6040, 79008]
    total = 0
    for n in range(1, 12):
        d = [0] * (1 << n)
        for mask in all_involutions_fixed_sets(n):
            d[mask] += 1
        assert sum(d) == tel[n]
        raw = fwht(d)
        for subset, actual in enumerate(raw):
            k = subset.bit_count()
            assert actual == alternating_binomial(n, k, tel), (n, subset, actual)
            total += 1
        zeros = sum(v == 0 for v in raw)
        assert zeros == ({2: 2, 3: 6}.get(n, 0))
    for n in range(1, 61):
        row = [alternating_binomial(n, k, tel) for k in range(n + 1)]
        assert all(row[k] == (-1)**n * row[n-k] for k in range(n+1))
        if n >= 2:
            assert all(row[k] - row[k+1] == 2 * alternating_binomial(n-1, k, tel) for k in range(n))
        if n >= 4:
            assert all(v != 0 for v in row)
            assert min(abs(v) for v in row) == moments[n//2]
            if n%2:
                assert all(row[k] > row[k+1] for k in range(n))
            else:
                assert all(v > 0 for v in row)
    print(f'PASS: direct involution enumeration and independent Walsh transforms for n=1..11; {total} individual frequencies.')
    print('PASS: binomial formula, parity sign, adjacent-weight identity, nonvanishing and sharp gap for n=1..60.')
    print('Central moment sequence m=0..7:', moments[:8])
    for n in range(1, 11):
        row = [alternating_binomial(n,k,tel) for k in range(n+1)]
        print(f'n={n} count={tel[n]} min_abs={min(abs(x) for x in row)} zeros={sum(comb(n,k) for k,x in enumerate(row) if x==0)}')

if __name__ == '__main__':
    check()
