#!/usr/bin/env python3
"""Independent small-matrix enumeration and arithmetic tests for interval rook maps."""
from collections import Counter
from math import gcd, pi, log


def compose(left, right):
    """Apply right first, then left; sparse maps are tuples of (input, output)."""
    lm = dict(left)
    return tuple(sorted((i, lm[j]) for i, j in right if j in lm))


def nil_index_by_powers(f, n):
    if not f:
        return 1
    product = f
    for power in range(2, n + 2):
        product = compose(f, product)
        if not product:
            return power
    return None


def actual_monoid(n):
    maps = {()}
    for d in range(1 - n, n):
        lo, hi = max(1, 1 - d), min(n, n - d)
        for a in range(lo, hi + 1):
            for b in range(a, hi + 1):
                maps.add(tuple((i, i + d) for i in range(a, b + 1)))
    return maps


def tail_formula(n, t):
    return sum((n - t * h) * (n - t * h + 1)
               for h in range(1, (n - 1) // t + 1))


def index_distribution_formula(n):
    result = {}
    for j in range(2, n + 1):
        result[j] = tail_formula(n, j - 1) - tail_formula(n, j)
    return result


def divisor_weighted_sum(n):
    tau = [0] * n
    for d in range(1, n):
        for m in range(d, n, d):
            tau[m] += 1
    return sum(tau[m] * (n - m) * (n - m + 1) for m in range(1, n))


def main():
    for n in range(2, 13):
        M = actual_monoid(n)
        assert len(M) == 1 + n * (n + 1) * (2 * n + 1) // 6
        observed = Counter()
        for f in M:
            if not f:
                continue
            images = [j - i for i, j in f]
            assert len(set(images)) == 1
            if images[0] == 0:
                assert compose(f, f) == f
            else:
                k = nil_index_by_powers(f, n)
                assert isinstance(k, int) and k >= 2
                observed[k] += 1
        expected = index_distribution_formula(n)
        assert observed == Counter({k: v for k, v in expected.items() if v})
        N = (n ** 3 - n) // 3
        assert sum(observed.values()) == N
        for t in range(1, n):
            assert sum(v for k, v in observed.items() if k >= t + 1) == tail_formula(n, t)
        assert sum(k * v for k, v in observed.items()) == N + divisor_weighted_sum(n)
        print(f'DIRECT_MAP_POWERS_OK n={n} monoid={len(M)} nonzero_nilpotents={N}')

    for n in (100, 1000, 10000):
        N = (n ** 3 - n) // 3
        weighted = divisor_weighted_sum(n)
        mean = 1 + weighted / N
        assert abs(mean - (log(n) + 2 * 0.5772156649015329 - 5 / 6)) < 10 / n ** 0.5
        if n == 10000:
            print(f'MEAN_TEST_OK n={n} exact={mean:.10f} asymptotic={log(n)+2*0.5772156649015329-5/6:.10f}')

    # High-precision arithmetic checks on the macroscopic-tail and second-moment formulas.
    for n in (100, 1000, 10000):
        N = (n**3-n)//3
        # Sum by displacement and length, not using the tail formula.
        second = 0
        for h in range(1, n):
            L = n - h
            # Each block length r occurs (L-r+1) times on each signed diagonal.
            # Aggregate by quotient r/h to avoid a quadratic loop.
            for q in range((L - 1) // h + 1):
                lo = q*h + 1
                hi = min((q+1)*h, L)
                if lo > hi:
                    continue
                cnt = hi - lo + 1
                count_weight = cnt*(L+1) - (lo+hi)*cnt//2
                second += 2*count_weight*(q+2)**2
        if n == 10000:
            print(f'SECOND_MOMENT_TEST n={n} E[K^2]/n={second/N/n:.9f} limit={pi*pi/12:.9f}')
        assert abs(second/N/n-pi*pi/12)<4/n**0.35
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
