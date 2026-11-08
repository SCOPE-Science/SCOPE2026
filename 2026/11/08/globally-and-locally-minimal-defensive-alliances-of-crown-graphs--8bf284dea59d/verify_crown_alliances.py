"""Independent exhaustive checks of defensive alliances in labelled crown graphs.

Run: python3 verify_crown_alliances.py

Each shore is represented by a bit mask of length n. Feasibility is checked
from the original graph neighborhood condition, not the theorem's classification.
"""
from collections import Counter
from math import comb


def is_defensive(n, x, y):
    """Test the closed-neighborhood inequality at every selected vertex."""
    if x == 0 and y == 0:
        return False
    a = [i for i in range(n) if x & (1 << i)]
    b = [j for j in range(n) if y & (1 << j)]
    for i in a:
        inside = sum(j != i for j in b)
        if 2 * inside + 1 < n - 1:
            return False
    for j in b:
        inside = sum(i != j for i in a)
        if 2 * inside + 1 < n - 1:
            return False
    return True


def coefficient(n, k):
    """Count ordered shore pairs of size s with intersection exactly k."""
    s = (n - 1) // 2 + 1
    if not (0 <= k <= s) or s - k > n - s:
        return 0
    return comb(n, k) * comb(n - k, s - k) * comb(n - s, s - k)


def verify_one(n):
    t = (n - 1) // 2
    s = t + 1
    candidates = range(1 << n)
    alliances = {
        (x, y) for x in candidates for y in candidates
        if is_defensive(n, x, y)
    }

    # This direct containment calculation does not rely on any proposed shape.
    global_min = {
        (x, y) for x, y in alliances
        if not any(
            (u, v) != (x, y) and (u & x) == u and (v & y) == v
            for u, v in alliances
        )
    }
    local_min = {
        (x, y) for x, y in alliances
        if all(
            not is_defensive(n, x & ~(1 << i), y)
            for i in range(n) if x & (1 << i)
        ) and all(
            not is_defensive(n, x, y & ~(1 << j))
            for j in range(n) if y & (1 << j)
        )
    }

    low = {
        (x, y) for x, y in alliances
        if x.bit_count() == t and y.bit_count() == t and (x & y) == 0
    }
    high_global = {
        (x, y) for x, y in alliances
        if x.bit_count() == s and y.bit_count() == s
        and (x & y).bit_count() >= 3
    }
    high_local = {
        (x, y) for x, y in alliances
        if x.bit_count() == s and y.bit_count() == s
        and (x & y).bit_count() >= 2
    }
    assert global_min == low | high_global, (n, 'global classification')
    assert local_min == low | high_local, (n, 'local classification')

    count_low = comb(n, t) * comb(n - t, t)
    count_global_high = sum(coefficient(n, k) for k in range(3, s + 1))
    count_local_high = sum(coefficient(n, k) for k in range(2, s + 1))
    assert len(global_min) == count_low + count_global_high
    assert len(local_min) == count_low + count_local_high
    assert len(local_min - global_min) == coefficient(n, 2)

    # Confirm that each locally-only alliance contains exactly two global minima.
    for x, y in local_min - global_min:
        witnesses = sum(
            ((u & x) == u) and ((v & y) == v)
            for u, v in global_min
        )
        assert witnesses == 2, (n, x, y, witnesses)

    print(f'n={n} subsets={4 ** n} alliances={len(alliances)} '
          f'global={len(global_min)} local={len(local_min)} '
          f'global_spectrum={dict(sorted(Counter(x.bit_count() + y.bit_count() for x, y in global_min).items()))}')
    return len(global_min), len(local_min)


if __name__ == '__main__':
    totals = [verify_one(n) for n in range(3, 9)]
    print(f'VERIFY_OK orders=3..8 subsets={sum(4 ** n for n in range(3, 9))} '
          f'global_minimal_sets={sum(x for x, _ in totals)} '
          f'local_minimal_sets={sum(y for _, y in totals)} '
          'neighborhood_condition=PASS local_global_classification=PASS '
          'binomial_counts=PASS exact_two_witnesses=PASS')
