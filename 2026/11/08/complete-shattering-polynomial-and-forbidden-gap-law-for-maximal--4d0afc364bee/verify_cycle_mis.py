"""Independent finite checks for the maximal-independent-cycle shattering theorem.

Run with Python 3.10+ without third-party packages.
The checks are exhaustive only over the finite ranges printed below;
the unrestricted claims rely on the accompanying mathematical proof.
"""
from collections import Counter
from fractions import Fraction
from math import comb


def maximal_independent_sets(n):
    assert n >= 3
    out = []
    for mask in range(1 << n):
        if any(((mask >> i) & 1) and ((mask >> ((i + 1) % n)) & 1)
               for i in range(n)):
            continue
        if any(not ((mask >> i) & 1) and
               not ((mask >> ((i - 1) % n)) & 1) and
               not ((mask >> ((i + 1) % n)) & 1)
               for i in range(n)):
            continue
        out.append(mask)
    return out


def cyclic_gap_condition(support_mask, n):
    indices = [i for i in range(n) if (support_mask >> i) & 1]
    if not indices:
        return True
    k = len(indices)
    gaps = [((indices[(j + 1) % k] - indices[j] - 1) % n) + 1
            for j in range(k)]
    if min(gaps) < 2:
        return False
    short = [j for j, gap in enumerate(gaps) if gap == 2]
    if len(short) < 2:
        return True
    for j, start in enumerate(short):
        end = short[(j + 1) % len(short)]
        if end <= start:
            end += k
        if all(gaps[i % k] == 3 for i in range(start + 1, end)):
            return False
    return True


def exact_coefficient(n, k):
    if k == 0:
        return 1
    count = 3 * (n == 3 * k) + n * (n == 3 * k - 1)
    for p in range(1, k + 1):
        for q in range(min(p, k - p) + 1):
            r = k - p - q
            excess = n - 3 * k - p + q
            if excess < 0:
                continue
            term = (Fraction(n, p) * comb(p, q) *
                    comb(k - 1, r) * comb(excess + p - 1, p - 1))
            count += term
    assert count.denominator == 1 if isinstance(count, Fraction) else True
    return int(count)


def main():
    tested_supports = 0
    for n in range(3, 19):
        concepts = maximal_independent_sets(n)
        profile = Counter()
        for support in range(1 << n):
            k = support.bit_count()
            direct = len({c & support for c in concepts}) == (1 << k)
            predicted = cyclic_gap_condition(support, n)
            assert direct == predicted, (n, support, direct, predicted)
            tested_supports += 1
            if direct:
                profile[k] += 1
        for k in range(n + 1):
            assert profile[k] == exact_coefficient(n, k), (n, k, profile[k])
        assert max(profile) == (n + 1) // 3, n
        if n >= 5 and (n + 1) % 3 == 0:
            assert profile[(n + 1) // 3] == n
    for n in range(19, 91):
        d = (n + 1) // 3
        for k in range(d + 1, min(n, d + 3) + 1):
            assert exact_coefficient(n, k) == 0
        if n >= 5 and (n + 1) % 3 == 0:
            assert exact_coefficient(n, d) == n
    print('MAXIMAL_CYCLE_SHATTERING_PASS supports=', tested_supports,
          'direct_lengths=3..18', 'formula_boundary_lengths=19..90')


if __name__ == '__main__':
    main()
