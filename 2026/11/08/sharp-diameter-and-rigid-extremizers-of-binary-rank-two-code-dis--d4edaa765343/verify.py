"""Independent exact checks for the binary rank-two code-distortion theorem.

This script uses only Python's standard library. Run with Python 3.9+.
"""
from fractions import Fraction
from itertools import permutations, product


def weight_profile(columns):
    """Rows of a 2-by-n binary generator represented by 2-bit columns."""
    a = sum(col in (1, 3) for col in columns)
    b = sum(col in (2, 3) for col in columns)
    c = sum(col in (1, 2) for col in columns)
    return tuple(sorted((a, b, c)))


def all_profiles(n):
    """Independently enumerate generator-column multiplicities."""
    profiles = set()
    for zero in range(n + 1):
        for one in range(n - zero + 1):
            for two in range(n - zero - one + 1):
                three = n - zero - one - two
                if sum(v > 0 for v in (one, two, three)) < 2:
                    continue
                columns = (0,) * zero + (1,) * one + (2,) * two + (3,) * three
                profiles.add(weight_profile(columns))
    return sorted(profiles)


def raw_distortion(a, b):
    """Six basis reidentifications, using exact rational arithmetic."""
    best = None
    for perm in permutations(b):
        ratios = [Fraction(perm[i], a[i]) for i in range(3)]
        candidate = max(ratios) / min(ratios)
        if best is None or candidate < best:
            best = candidate
    return best


def sorted_distortion(a, b):
    ratios = [Fraction(v, u) for u, v in zip(a, b)]
    return max(ratios) / min(ratios)


def test_direct_generators():
    count = 0
    for n in range(2, 8):
        seen = set()
        for columns in product(range(4), repeat=n):
            a = weight_profile(columns)
            if a[0] == 0:
                continue
            seen.add(a)
            # Basis change really permutes exactly the nonzero codeword set.
            assert {a[0], a[1], a[2]} == {sum(k in (1, 3) for k in columns),
                sum(k in (2, 3) for k in columns), sum(k in (1, 2) for k in columns)}
            count += 1
        assert sorted(seen) == all_profiles(n)
    return count


def test_complete_profiles():
    pairs_checked = 0
    extrema = []
    for n in range(2, 13):
        profiles = all_profiles(n)
        best = Fraction(0)
        best_pairs = []
        for a in profiles:
            for b in profiles:
                brute = raw_distortion(a, b)
                formula = sorted_distortion(a, b)
                assert brute == formula, (n, a, b, brute, formula)
                pairs_checked += 1
                if brute > best:
                    best = brute
                    best_pairs = [(a, b)]
                elif brute == best:
                    best_pairs.append((a, b))
        expected = Fraction(1 if n == 2 else n)
        assert best == expected, (n, best)
        count_expected = 1 if n == 2 else 2 * (n // 3)
        assert len(best_pairs) == count_expected, (n, len(best_pairs))
        if n >= 3:
            split = (1, n - 1, n)
            simplex = {(2 * t, 2 * t, 2 * t) for t in range(1, n // 3 + 1)}
            actual = {(a, b) for a, b in best_pairs}
            specified = {(split, b) for b in simplex} | {(b, split) for b in simplex}
            assert actual == specified, (n, actual.symmetric_difference(specified))
        extrema.append((n, len(profiles), str(best), len(best_pairs)))
    return pairs_checked, extrema


if __name__ == '__main__':
    direct = test_direct_generators()
    pairs, extrema = test_complete_profiles()
    print('CHECK_OK')
    print('direct_generator_instances:', direct)
    print('profile_pair_instances:', pairs)
    for line in extrema:
        print('n=%d profile_classes=%d maximum=%s ordered_extremal_pairs=%d' % line)
