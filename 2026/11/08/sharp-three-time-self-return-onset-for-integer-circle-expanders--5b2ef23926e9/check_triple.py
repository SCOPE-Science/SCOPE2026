#!/usr/bin/env python3
"""Exact rational verification for three-time recurrences of expanding circle maps.

This finite checker corroborates a separately written all-integer proof.
It certifies the complete base-two piecewise law because every possible
endpoint crossing has been included in its rational breakpoint list.
"""
from fractions import Fraction as Q
from itertools import combinations, product


def segments(multiplier, radius):
    """Disjoint rational components of {x in [0,1]: ||multiplier*x||<radius}."""
    assert multiplier >= 1 and Q(0) <= radius <= Q(1, 2)
    intervals = []
    for k in range(multiplier + 1):
        low = max(Q(0), (Q(k) - radius) / multiplier)
        high = min(Q(1), (Q(k) + radius) / multiplier)
        if high > low:
            intervals.append((low, high))
    intervals.sort()
    result = []
    for low, high in intervals:
        if result and low <= result[-1][1]:
            result[-1] = (result[-1][0], max(high, result[-1][1]))
        else:
            result.append((low, high))
    return result


def intersect(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        low = max(left[i][0], right[j][0])
        high = min(left[i][1], right[j][1])
        if high > low:
            result.append((low, high))
        if left[i][1] <= right[j][1]:
            i += 1
        else:
            j += 1
    return result


def probability(multipliers, radius):
    parts = [(Q(0), Q(1))]
    for multiplier in multipliers:
        parts = intersect(parts, segments(multiplier, radius))
    return sum((high - low for low, high in parts), Q(0))


TABLE = (
    (Q(0), Q(1, 4), Q(2, 7), Q(0)),
    (Q(1, 4), Q(3, 10), Q(18, 7), -Q(4, 7)),
    (Q(3, 10), Q(1, 3), Q(74, 21), -Q(6, 7)),
    (Q(1, 3), Q(3, 8), Q(38, 21), -Q(2, 7)),
    (Q(3, 8), Q(2, 5), Q(86, 21), -Q(8, 7)),
    (Q(2, 5), Q(1, 2), Q(106, 21), -Q(32, 21)),
)


def all_possible_kinks(multipliers):
    """All radii where any two circle-window boundary lines may cross."""
    candidates = {Q(0), Q(1, 2)}
    # Each endpoint is (integer + sign*radius)/multiplier.
    # The endpoints in (0,1) are covered with k=0,...,multiplier.
    for m, n in combinations(multipliers, 2):
        for k, l in product(range(m + 1), range(n + 1)):
            for s, t in product((-1, 1), repeat=2):
                denominator = n * s - m * t
                if denominator == 0:
                    continue
                radius = Q(m * l - n * k, denominator)
                if 0 < radius < Q(1, 2):
                    candidates.add(radius)
    return tuple(sorted(candidates))


def base_two_piecewise_certificate():
    kinks = all_possible_kinks((1, 3, 7))
    for radius in kinks:
        target = next((slope * radius + offset for low, high, slope, offset in TABLE
                       if low <= radius <= high), None)
        assert target is not None
        assert probability((1, 3, 7), radius) == target, radius
    # Within each adjacent pair of candidate points all endpoint orderings are
    # fixed; hence the intersection length is affine. Endpoint identities
    # therefore certify its value on the entire real interval.
    assert set(kinks) >= {entry[0] for entry in TABLE}
    assert set(kinks) >= {entry[1] for entry in TABLE}
    print('exact base-two breakpoint certificate:', len(kinks), 'candidate breakpoints')


def universal_regime_spot_tests():
    checks = 0
    for a in range(2, 31):
        N = a * a + a + 1
        rho = Q(a, N + 1)
        eta = Q(a, 2 * N * (N + 1))
        for radius in (rho / 3, rho * Q(3, 4), rho, rho + eta / 3, rho + eta):
            observed = probability((1, a + 1, N), radius)
            predicted = Q(2) * radius / N
            if radius > rho:
                predicted += Q(2 * (N + 1), N) * (radius - rho)
            assert observed == predicted, (a, radius, observed, predicted)
            checks += 1
        # Pair-window threshold below triple threshold, strict for a>2.
        pair = Q(1, a + 2)
        assert pair <= rho and (pair == rho) == (a == 2)
        assert probability((1, a + 1), pair) == Q(2) * pair / (a + 1)
        checks += 1
    print('exact rational universal-regime spot checks:', checks)


if __name__ == '__main__':
    base_two_piecewise_certificate()
    universal_regime_spot_tests()
    print('PASS: exact rational checks completed')
