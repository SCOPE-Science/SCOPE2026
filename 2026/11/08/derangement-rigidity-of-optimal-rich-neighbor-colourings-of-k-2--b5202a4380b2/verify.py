"""Standalone direct check of optimal rich-neighbor edge colorings of K_{2,n}.

Usage: python3 verify.py
No external packages are required.
"""
from itertools import permutations
from math import factorial


def derangements(n):
    out = [1, 0]
    for k in range(2, n + 1):
        out.append((k - 1) * (out[-1] + out[-2]))
    return out[n]


def cycle_type(p):
    unseen = set(range(len(p)))
    sizes = []
    while unseen:
        i = next(iter(unseen))
        v = i
        size = 0
        while v in unseen:
            unseen.remove(v)
            v = p[v]
            size += 1
        sizes.append(size)
    return tuple(sorted(sizes))


def independent_counts(n):
    # Canonicalize the first row by a palette permutation; every fixed first
    # row has the same number of completing rows, and there are (n+1)! of them.
    k = n + 1
    edges = [(side, j) for side in range(2) for j in range(n)]
    adjacent = [tuple(y for y, (t, b) in enumerate(edges)
                      if y != x and (side == t or col == b))
                for x, (side, col) in enumerate(edges)]
    possible = 0
    success = 0
    cycle_types = set()
    rich_profiles = set()
    for second in permutations(range(k), n):
        colors = tuple(range(n)) + second
        if any(colors[j] == colors[n+j] for j in range(n)):
            continue
        possible += 1
        rich = {i for i, near in enumerate(adjacent)
                if len(set(colors[j] for j in near)) == len(near)}
        if all(any(j in rich for j in adjacent[i]) for i in range(2*n)):
            success += 1
            left = {i % n for i in rich if i < n}
            right = {i % n for i in rich if i >= n}
            assert len(rich) == 2 and left == right and len(left) == 1
            j0 = next(iter(left))
            cols = [j for j in range(n) if j != j0]
            # Use the first row's off-column colors as labels for the
            # derangement defined by the second row.
            label_to_pos = {colors[j]: a for a, j in enumerate(cols)}
            sigma = tuple(label_to_pos[colors[n+j]] for j in cols)
            assert all(sigma[t] != t for t in range(n-1))
            cycle_types.add(cycle_type(sigma))
            rich_profiles.add(j0)
    return possible, success, rich_profiles, cycle_types


def restricted_partition_count(n):
    # Number of integer partitions of n with all parts at least two.
    memo = {}
    def partitions(left, minimum):
        if left == 0: return 1
        key = (left, minimum)
        if key not in memo:
            memo[key] = sum(partitions(left - p, p)
                            for p in range(minimum, left+1))
        return memo[key]
    return partitions(n, 2)


for n in range(2, 9):
    possible, successes, rich_cols, cycles = independent_counts(n)
    expected = n * derangements(n-1)
    expected_proper = derangements(n+1) + derangements(n)
    expected_orbits = restricted_partition_count(n-1)
    assert successes == expected, (n, successes, expected)
    assert possible == expected_proper, (n, possible, expected_proper)
    assert len(cycles) == expected_orbits, (n, cycles, expected_orbits)
    if n >= 3:
        assert rich_cols == set(range(n))
    else:
        assert not rich_cols
    full = successes * factorial(n+1)
    formula = (n * (n+1) * n * factorial(n-1) * derangements(n-1))
    assert full == formula
    print('DIRECT_ADJACENCY_ENUMERATION_OK', n, 'proper',
          possible * factorial(n+1), 'rich_neighbor', full,
          'orbit_types', len(cycles))
print('VERIFY_OK')
