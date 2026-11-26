"""Exact finite arithmetic for projective-plane group coupon coverage.

Only Python standard-library modules are required. Execute: python verify.py
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb


def projective_plane_ternary():
    """Canonical points and incidence lines of PG(2,3)."""
    points = set()
    for triple in product(range(3), repeat=3):
        if triple == (0, 0, 0):
            continue
        leading = next(x for x in triple if x)
        scale = 1 if leading == 1 else 2
        points.add(tuple((scale * x) % 3 for x in triple))
    points = sorted(points)
    assert len(points) == 13
    lines = []
    for normal in points:
        mask = sum(1 << i for i, point in enumerate(points)
                   if sum(x * y for x, y in zip(normal, point)) % 3 == 0)
        lines.append(mask)
    assert len(lines) == len(set(lines)) == 13
    assert all(line.bit_count() == 4 for line in lines)
    assert all(sum(bool(line & (1 << i)) for line in lines) == 4
               for i in range(13))
    assert all((lines[i] & lines[j]).bit_count() == 1
               for i in range(13) for j in range(i))
    return lines


def missed_subset_coefficients(blocks, n):
    """Exhaust all nonempty subsets of uncovered points (inclusion-exclusion)."""
    coefficients = defaultdict(int)
    for missed in range(1, 1 << n):
        avoidance = sum((block & missed) == 0 for block in blocks)
        coefficients[avoidance] += 1 if missed.bit_count() % 2 else -1
    return dict(coefficients)


def full_model_coefficients(n, k):
    coefficients = defaultdict(int)
    for size in range(1, n + 1):
        avoiding = comb(n - size, k) if size <= n - k else 0
        coefficients[avoiding] += (1 if size % 2 else -1) * comb(n, size)
    return dict(coefficients)


def survival(coefficients, m, t):
    assert t >= 1
    return Fraction(sum(weight * (avoiding ** t)
                        for avoiding, weight in coefficients.items()), m ** t)


def covering_family_counts(blocks, n):
    """Independent enumeration of all distinct-block covering subfamilies."""
    counts = Counter()
    for mask in range(1, 1 << len(blocks)):
        covered = 0
        for i, block in enumerate(blocks):
            if mask & (1 << i):
                covered |= block
        if covered == (1 << n) - 1:
            counts[mask.bit_count()] += 1
    return dict(counts)


def onto_maps(t, j):
    return sum((-1) ** (j - h) * comb(j, h) * h ** t for h in range(j + 1))


def cover_via_subfamilies(counts, m, t):
    return Fraction(sum(number * onto_maps(t, j)
                        for j, number in counts.items() if j <= t), m ** t)


def direct_cover_paths(blocks, n, t):
    """Independent exact count through the state-chain of covered-point masks."""
    states = {0: 1}
    for _ in range(t):
        following = defaultdict(int)
        for covered, multiplicity in states.items():
            for block in blocks:
                following[covered | block] += multiplicity
        states = following
    return Fraction(states.get((1 << n) - 1, 0), len(blocks) ** t)


def main():
    n, k = 13, 4
    lines = projective_plane_ternary()
    full = [sum(1 << i for i in selection)
            for selection in combinations(range(n), k)]
    assert len(full) == 715

    projective = missed_subset_coefficients(lines, n)
    all_quads = full_model_coefficients(n, k)
    assert projective == {9: 13, 6: -78, 4: 234, 3: -182,
                          2: -78, 1: 130, 0: -38}
    assert all_quads == {495: 13, 330: -78, 210: 286, 126: -715,
                         70: 1287, 35: -1716, 15: 1716,
                         5: -1287, 1: 715, 0: -220}
    assert missed_subset_coefficients(full, n) == all_quads
    assert sum(projective.values()) == sum(all_quads.values()) == 1

    count_covering = covering_family_counts(lines, n)
    assert count_covering == {4: 13, 5: 117, 6: 702, 7: 1248,
                              8: 1170, 9: 702, 10: 286, 11: 78,
                              12: 13, 13: 1}
    for t in range(1, 9):
        assert 1 - survival(projective, 13, t) == cover_via_subfamilies(count_covering, 13, t)
    for t in (3, 4, 5):
        assert 1 - survival(projective, 13, t) == direct_cover_paths(lines, n, t)
    for t in (4, 5):
        assert 1 - survival(all_quads, 715, t) == direct_cover_paths(full, n, t)

    assert all(survival(projective, 13, t) == survival(all_quads, 715, t) == 1
               for t in range(1, 4))
    gap = lambda t: survival(projective, 13, t) - survival(all_quads, 715, t)
    assert gap(4) == -Fraction(15480, 2924207)
    assert gap(5) == Fraction(2178216, 418161601)
    assert all(gap(t) > 0 for t in range(5, 10))

    # For t >= 10, 234*(220/715)^t exceeds the sum of every
    # negative term of the exact tail difference. The six ratios
    # below decrease strictly with t, proving an infinite-time bound.
    bound_at_ten = (Fraction(286, 234) * Fraction(21, 22) ** 10
                    + Fraction(182, 234) * Fraction(3, 4) ** 10
                    + Fraction(78, 234) * Fraction(1, 2) ** 10
                    + Fraction(1287, 234) * Fraction(7, 22) ** 10
                    + Fraction(1716, 234) * Fraction(3, 44) ** 10
                    + Fraction(715, 234) * Fraction(1, 220) ** 10)
    assert bound_at_ten < 1

    expected_line = 1 + sum(Fraction(c * h, 13 - h)
                            for h, c in projective.items() if h)
    expected_full = 1 + sum(Fraction(c * h, 715 - h)
                            for h, c in all_quads.items() if h)
    assert expected_line == Fraction(43633, 4620)
    assert expected_full == Fraction(1746879067753, 185252315340)
    assert expected_line > expected_full
    print("PASS: exact PG(2,3) incidence, 8,191 point subsets,")
    print("      all 715 four-subsets, 8,191 line subfamilies,")
    print("      independent covered-set DP, tail formulas, crossings,")
    print("      infinite-time positivity certificate and prior mean values")
    print("t=4 tail gap:", gap(4))
    print("t=5 tail gap:", gap(5))
    print("negative-to-positive transition verified; all later gaps positive")


if __name__ == "__main__":
    main()
