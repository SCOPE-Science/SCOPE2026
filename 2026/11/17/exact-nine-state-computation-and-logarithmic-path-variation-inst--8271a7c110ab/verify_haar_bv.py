"""Exact integer certificate for dyadic Haar soft-shrinkage path-variation bounds.

No external packages. This independently enumerates the active Haar wavelets
for each one-jump perturbation at small depths and compares an all-depth
nine-state dynamic program.
"""
from fractions import Fraction
import sys

STATES = (-1, 0, 1)


def dynamic(depth):
    """Return integer numerators R=(2**depth)*Q for each 0<cut<n."""
    previous = None
    rows = []
    for d in range(1, depth + 1):
        n = 1 << d
        half = n // 2
        current = [None] * n
        for k in range(1, n):
            record = {}
            for p in STATES:
                for q in STATES:
                    if k == half:
                        value = max(0, n + half * (q - p))
                    elif k < half:
                        value = max(
                            2 * previous[k][p, 1],
                            2 * previous[k][p, -1] + k * (2 - p + q),
                        )
                    else:
                        value = max(
                            2 * previous[k - half][-1, q],
                            2 * previous[k - half][1, q] + (n - k) * (2 - p + q),
                        )
                    record[p, q] = value
            current[k] = record
        sharp = max(current[k][0, 0] for k in range(1, n))
        rows.append(Fraction(sharp, n))
        previous = current
    return rows


def brute_one_cut(n, k):
    """Compute exact BV of every mask on the nonzero Haar details for a jump."""
    d = n.bit_length() - 1
    contribution = []
    for level in range(d):
        size = 1 << (level + 1)
        start = k // size * size
        offset = k - start
        deltas = {}
        if offset:
            a = Fraction(-min(offset, size - offset), size)
            if start > 0:
                deltas[start] = a
            midpoint = start + size // 2
            deltas[midpoint] = deltas.get(midpoint, 0) - 2 * a
            if start + size < n:
                j = start + size
                deltas[j] = deltas.get(j, 0) + a
        contribution.append(deltas)
    best = Fraction(0)
    for mask in range(1 << d):
        gradient = [Fraction(0)] * n
        for level, deltas in enumerate(contribution):
            if (mask >> level) & 1:
                for j, val in deltas.items():
                    gradient[j] += val
        val = sum(abs(x) for x in gradient)
        if val > best:
            best = val
    return best


def verify():
    values = dynamic(14)
    expected = [
        Fraction(1), Fraction(3, 2), Fraction(2), Fraction(21, 8),
        Fraction(3), Fraction(117, 32), Fraction(4), Fraction(597, 128),
        Fraction(5), Fraction(2901, 512), Fraction(6), Fraction(13653, 2048),
        Fraction(7), Fraction(62805, 8192),
    ]
    assert values == expected, (values, expected)
    print("EXACT_NINE_STATE_DP_DEPTHS_1_TO_14_PASS")
    for d in range(1, 8):
        n = 1 << d
        direct = max(brute_one_cut(n, k) for k in range(1, n))
        assert direct == values[d - 1], (d, direct, values[d - 1])
    print("INDEPENDENT_HAAR_MASK_ENUMERATION_DEPTHS_1_TO_7_PASS")
    for d in range(3, 15):
        n = 1 << d
        k = (n + 1) // 3 if d % 2 else (n - 1) // 3
        m = d // 3
        supports = []
        lower = Fraction(0)
        for j in range(0, d - 2, 3):
            size = 1 << (j + 1)
            start = k // size * size
            r = k - start
            assert 0 < start and start + size < n
            supp = {start, start + size // 2, start + size}
            assert not any(supp.intersection(other) for other in supports)
            supports.append(supp)
            lower += Fraction(4 * min(r, size - r), size)
        assert len(supports) == m
        assert lower >= Fraction(4 * m, 3) + Fraction(4, 7)
        assert lower <= values[d - 1]
    print("DISJOINT_SCALE_CONSTRUCTION_AND_LOG_GROWTH_DEPTHS_3_TO_14_PASS")
    print("ALL_HAAR_BV_CHECKS_PASS")


if __name__ == "__main__":
    verify()
