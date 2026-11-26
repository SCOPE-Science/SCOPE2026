#!/usr/bin/env python3
"""Finite sanity checks for sharp team-profile witness bounds.

The general statements follow from a separate proof. This program checks
small cases exhaustively and tests the explicit separating-row algorithm.
"""
from itertools import product


def profile(rows, k):
    if not rows:
        raise ValueError("profiles are for nonempty teams")
    columns = tuple(tuple(row[i] for row in rows) for i in range(k))
    equalities = tuple(columns[i] == columns[j]
                       for i in range(k) for j in range(i + 1, k))
    constant = tuple(len(set(column)) == 1 for column in columns)
    r = len({column for column in columns if len(set(column)) > 1})
    return (equalities, constant), r


def replacement_bound(m, r):
    if not r:
        return 1
    t = 1
    while m**t - m < r:
        t += 1
    return t


def greedy_subteam(rows, m, k):
    """Greedily separate actual column functions and all constant columns."""
    indices = [0]
    augmented = [tuple(row[i] for row in rows) for i in range(k)]
    augmented += [tuple([a] * len(rows)) for a in range(m)]

    def classes(chosen):
        d = {}
        for j, column in enumerate(augmented):
            key = tuple(column[i] for i in chosen)
            d.setdefault(key, []).append(j)
        return tuple(tuple(g) for g in d.values())

    while True:
        groups = classes(indices)
        separated = all(len({augmented[j] for j in group}) == 1
                        for group in groups)
        if separated:
            break
        old_count = len(groups)
        for i in range(len(rows)):
            if i not in indices and len(classes(indices + [i])) > old_count:
                indices.append(i)
                break
        else:
            raise AssertionError("An indistinguished pair had no separating row")
    return tuple(rows[i] for i in indices)


def exhaustive(m, k):
    points = tuple(product(range(m), repeat=k))
    n = len(points)
    if n > 16:
        raise ValueError("This test is intended for at most 16 assignments")
    profiles = [None] * (1 << n)
    types = [None] * (1 << n)
    minimum_subteam = [0] * (1 << n)
    least_by_profile = {}
    observed_max = 0
    for mask in range(1, 1 << n):
        rows = tuple(points[i] for i in range(n) if mask & (1 << i))
        typ, r = profile(rows, k)
        profiles[mask] = typ
        types[mask] = r
        size = len(rows)
        least_by_profile[typ] = min(size, least_by_profile.get(typ, size))
        prev_best = [minimum_subteam[mask ^ (1 << i)]
                     for i in range(n)
                     if mask & (1 << i)
                     and profiles[mask ^ (1 << i)] == typ]
        minimum_subteam[mask] = min(prev_best) if prev_best else size
        assert minimum_subteam[mask] <= r + 1
        observed_max = max(observed_max, minimum_subteam[mask])
        sub = greedy_subteam(rows, m, k)
        assert profile(sub, k)[0] == typ
        assert len(sub) <= r + 1
    for typ, size in least_by_profile.items():
        mask = next(i for i in range(1, 1 << n) if profiles[i] == typ)
        assert size == replacement_bound(m, types[mask])
    assert observed_max == k + 1
    print(f"EXHAUSTIVE_OK alphabet={m} variables={k} "
          f"teams={2**n - 1} profiles={len(least_by_profile)} "
          f"max_min_subteam={observed_max}")


def check_chain(m, r):
    rows = tuple(tuple(int(j >= i) for i in range(1, r+1))
                 for j in range(r+1))
    full, nonconstant = profile(rows, r)
    assert nonconstant == r
    for j in range(r+1):
        assert profile(rows[:j] + rows[j+1:], r)[0] != full


if __name__ == "__main__":
    for m, k in ((2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (4, 1), (4, 2)):
        exhaustive(m, k)
    for m in (2, 3, 5):
        for r in range(1, 12):
            check_chain(m, r)
    print("SHARP_SMALL_TEAM_BOUNDS_VERIFY_OK")
