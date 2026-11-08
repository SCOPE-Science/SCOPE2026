#!/usr/bin/env python3
"""Independent finite-state checks for the K(3,n) fixed-hub avalanche law."""
from collections import Counter
from itertools import product
from math import comb


def topple(n, a, b, leaves, source=None, burn=False):
    height = [a, b] + list(leaves)
    if burn:
        for i in range(n):
            height[i + 2] += 1
    else:
        height[source] += 1
    count = [0] * (n + 2)
    while True:
        unstable = next((j for j in range(n + 2)
                         if height[j] >= (n if j < 2 else 3)), None)
        if unstable is None:
            break
        count[unstable] += 1
        assert sum(count) <= 10 * (n + 2)
        if unstable < 2:
            height[unstable] -= n
            for j in range(2, n + 2):
                height[j] += 1
        else:
            height[unstable] -= 3
            height[0] += 1
            height[1] += 1
    return tuple(count)


def predicted(n):
    p = Counter()
    for r in range(1, n):
        p[r + 1] += n * comb(n - 1, r) * (2 ** (n - 1 - r))
    for k in range(1, n):
        p[k + 2] += n * comb(n - 1, k - 1) * (2 ** (k - 1))
    p[n + 3] += n * 2 ** (n - 1)
    p[0] += n * ((n - 2) * 3 ** (n - 1) + 2 ** (n - 1))
    return p


def finite_check(n):
    counts = Counter()
    rec_count = 0
    for a in range(n):
        for b in range(n):
            for leaves in product((0, 1, 2), repeat=n):
                z0 = leaves.count(0)
                z1 = leaves.count(1)
                rec_burn = topple(n, a, b, leaves, burn=True) == (1,) * (n + 2)
                rec_formula = min(a, b) >= z0 and max(a, b) >= z0 + z1
                assert rec_burn == rec_formula
                if rec_burn:
                    rec_count += 1
                    count = topple(n, a, b, leaves, source=0)
                    assert max(count) <= 2
                    counts[sum(count)] += 1
    assert rec_count == n*n*3**(n-1)
    assert counts == predicted(n), (n, counts, predicted(n))
    return rec_count


def algebra_check(n):
    p = predicted(n)
    assert sum(p.values()) == n*n*3**(n-1)
    assert sum(k for k in p if k < 0) == 0
    positive = sum(value for k, value in p.items() if k > 0)
    assert positive == n*(2*3**(n-1)-2**(n-1))
    assert p[n+3] == n*2**(n-1)
    for size, coeff in p.items():
        assert coeff >= 0 and size >= 0


def main():
    for n in range(2, 8):
        r = finite_check(n)
        print(f"n={n}: {r} recurrent states; burning and all source avalanches agree")
    for n in range(2, 81):
        algebra_check(n)
    print("79 exact generating-polynomial normalization checks; PASS")
    print("The infinite-n limit follows from binomial weak laws, not these finite tests.")


if __name__ == '__main__':
    main()
