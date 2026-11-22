"""Independent finite enumeration of cycle profiles in restricted-range transformation semigroups.

Run with Python 3: python CHECK.py
"""
from collections import Counter
from itertools import product
from math import comb, factorial


def falling(n, k):
    ans = 1
    for j in range(k):
        ans *= n - j
    return ans


def rooted_forest_z(k, m, a):
    # a specified cyclic vertices inside Z, all remaining Y vertices flow to them.
    if a == k:
        return k ** (m - k)
    return a * k ** (m - a - 1)


def rooted_forest_w(n, m, b):
    # b specified cyclic vertices outside Y, Y is an additional absorbing root set.
    w = n - m
    if b == w:
        return 1
    return (m + b) * n ** (w - b - 1)


def theoretical_profile(n, m, k):
    w = n - m
    return {
        (a, b): falling(k, a) * rooted_forest_z(k, m, a)
                * falling(w, b) * rooted_forest_w(n, m, b)
        for a in range(1, k + 1)
        for b in range(0, w + 1)
    }


def partitions_of_cycles(f):
    """Return sorted cycle-length multisets in Z and the complement of Y."""
    seen = set()
    cycles = []
    for start in range(len(f)):
        if start in seen:
            continue
        positions = {}
        path = []
        cur = start
        while cur not in seen and cur not in positions:
            positions[cur] = len(path)
            path.append(cur)
            cur = f[cur]
        if cur in positions:
            cyc = path[positions[cur]:]
            cycles.append(cyc)
        seen.update(path)
    return cycles


def multiplicity_partition(part):
    z = 1
    for length, count in Counter(part).items():
        z *= length ** count * factorial(count)
    return z


def theoretical_cycle_type(n, m, k, lam, mu):
    """Count maps for prescribed full cycle types in Z and outside Y."""
    a, b = sum(lam), sum(mu)
    w = n - m
    if not (1 <= a <= k and 0 <= b <= w):
        return 0
    return (comb(k, a) * factorial(a) // multiplicity_partition(lam)
            * comb(w, b) * factorial(b) // multiplicity_partition(mu)
            * rooted_forest_z(k, m, a) * rooted_forest_w(n, m, b))


def observed(n, m, k):
    profile, types = Counter(), Counter()
    for on_y in product(range(k), repeat=m):
        for on_w in product(range(n), repeat=n-m):
            f = on_y + on_w
            cycles = partitions_of_cycles(f)
            assert all(all(x < k for x in cyc) or all(x >= m for x in cyc)
                       for cyc in cycles)
            lam = tuple(sorted(len(cyc) for cyc in cycles if cyc[0] < k))
            mu = tuple(sorted(len(cyc) for cyc in cycles if cyc[0] >= m))
            profile[sum(lam), sum(mu)] += 1
            types[lam, mu] += 1
    return profile, types


def main():
    cases = 0
    for n in range(1, 7):
        for m in range(1, n + 1):
            for k in range(1, m + 1):
                counts, types = observed(n, m, k)
                predicted = theoretical_profile(n, m, k)
                assert counts == Counter(predicted), (n, m, k, counts, predicted)
                assert sum(counts.values()) == k ** m * n ** (n-m)
                for (lam, mu), count in types.items():
                    assert count == theoretical_cycle_type(n, m, k, lam, mu), (n, m, k, lam, mu)
                assert sum(value for (a, b), value in counts.items() if b == 0) * n == m * sum(counts.values())
                assert counts.get((1, 0), 0) * k * n == m * sum(counts.values())
                cases += 1
    n, m, k = 5, 3, 2
    expected = {(1, 0): 60, (1, 1): 32, (1, 2): 8,
                (2, 0): 60, (2, 1): 32, (2, 2): 8}
    assert theoretical_profile(n, m, k) == expected
    print('RESTRICTED_RANGE_CYCLE_CENSUS_VERIFIED', cases)


if __name__ == '__main__':
    main()
