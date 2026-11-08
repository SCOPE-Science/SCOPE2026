"""Exact-rational cross-check for minimum-quota serial assignment.

Run: python CHECK.py
Python standard library only. Not a proof of the all-market theorem;
that part is proved analytically in RESULT.md.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import permutations, product


def event_algorithm(profile, lower):
    n, m = len(profile), len(lower)
    t = F(0)
    available = set(range(m))
    unfilled = {j for j in available if lower[j] > 0}
    outcome = [[F(0) for _ in range(m)] for _ in range(n)]
    forced = False
    while t < 1:
        destinations = [next(j for j in rank if j in available) for rank in profile]
        rates = Counter(destinations)
        column = [sum(outcome[i][j] for i in range(n)) for j in range(m)]
        hit_capacity = {j: t + (n - column[j]) / rates[j]
                        for j in available - unfilled if rates[j]}
        hit_minimum = {j: t + (lower[j] - column[j]) / rates[j]
                       for j in unfilled if rates[j]}
        unrestricted = set(range(m)) - unfilled
        outside_mass = sum(column[j] for j in unrestricted)
        outside_rate = sum(rates[j] for j in unrestricted)
        global_time = (t + (n - sum(lower[j] for j in unfilled)
                              - outside_mass) / outside_rate
                       if outside_rate else F(n + 1))
        next_time = min([F(1), global_time] + list(hit_capacity.values())
                        + list(hit_minimum.values()))
        assert next_time >= t
        for i, j in enumerate(destinations):
            outcome[i][j] += next_time - t
        t = next_time
        if t == global_time:
            forced = True
        unfilled -= {j for j, ht in hit_minimum.items() if ht == t}
        if forced:
            available = set(unfilled)
        else:
            available -= {j for j, ht in hit_capacity.items() if ht == t}
    ans = tuple(tuple(row) for row in outcome)
    assert all(sum(row) == 1 for row in ans)
    return ans


def polytope_algorithm(profile, lower):
    n, m = len(profile), len(lower)
    t = F(0)
    used = [F(0)] * m
    remaining = set(range(m))
    output = [[F(0) for _ in range(m)] for _ in range(n)]
    for _ in range(2 * m + 4):
        if t == 1:
            break
        assert remaining
        selected = [next(j for j in preference if j in remaining)
                    for preference in profile]
        flow = [selected.count(j) for j in range(m)]
        to_cap = [(n - used[j]) / flow[j] for j in remaining if flow[j]]
        to_kink = [(lower[j] - used[j]) / flow[j] for j in remaining
                   if flow[j] and used[j] < lower[j]]
        value = sum(max(F(lower[j]), used[j]) for j in range(m))
        derivative = sum(flow[j] for j in remaining if used[j] >= lower[j])
        to_boundary = (F(n) - value) / derivative if derivative else F(n + 1)
        dt = min([1 - t, to_boundary] + to_cap + to_kink)
        assert dt >= 0
        for i, j in enumerate(selected):
            output[i][j] += dt
        for j in range(m):
            used[j] += flow[j] * dt
        t += dt
        if sum(max(F(lower[j]), used[j]) for j in range(m)) == n:
            remaining = {j for j in remaining if used[j] < lower[j]}
        else:
            remaining = {j for j in remaining if used[j] < n}
    assert t == 1
    ans = tuple(tuple(row) for row in output)
    assert all(sum(row) == 1 for row in ans)
    return ans


def has_positive_utility_gain(truth_rank, current, deviation):
    partial = F(0)
    for j in truth_rank[:-1]:
        partial += deviation[j] - current[j]
        if partial > 0:
            return True
    return False


def one_minimum_formula(profile, lower):
    n, m = len(profile), len(lower)
    positive = [j for j, value in enumerate(lower) if value]
    assert len(positive) <= 1
    if not positive:
        return tuple(tuple(F(j == rank[0]) for j in range(m)) for rank in profile)
    a = positive[0]
    L = lower[a]
    s = sum(rank[0] == a for rank in profile)
    if s >= L:
        return tuple(tuple(F(j == rank[0]) for j in range(m)) for rank in profile)
    tau = F(n - L, n - s)
    return tuple(tuple(F(j == a) if rank[0] == a else
                       (tau if j == rank[0] else 1 - tau if j == a else F(0))
                       for j in range(m)) for rank in profile)


def verify():
    order3 = list(permutations(range(3)))
    profiles_checked = 0
    for lower in ((1, 1, 0), (1, 0, 0), (0, 0, 0), (1, 1, 1)):
        for profile in product(order3, repeat=3):
            e = event_algorithm(profile, lower)
            p = polytope_algorithm(profile, lower)
            assert e == p, (profile, lower, e, p)
            if sum(x > 0 for x in lower) <= 1:
                assert e == one_minimum_formula(profile, lower)
            profiles_checked += 1
    # Separate nontrivial universal-formula tests with four agents and three objects.
    order3 = list(permutations(range(3)))
    formula_checked = 0
    for L in range(5):
        lower = (L, 0, 0)
        for profile in product(order3, repeat=4):
            assert event_algorithm(profile, lower) == one_minimum_formula(profile, lower)
            formula_checked += 1
    profile_count = 0
    profitable_reports = 0
    per_profile = Counter()
    top_patterns = Counter()
    low = (1, 1, 0)
    example = ((0, 1, 2), (0, 2, 1), (2, 1, 0))
    for profile in product(order3, repeat=3):
        allocation = event_algorithm(profile, low)
        num_better = 0
        for i in range(3):
            for report in order3:
                if report == profile[i]:
                    continue
                changed_profile = list(profile)
                changed_profile[i] = report
                new_allocation = polytope_algorithm(changed_profile, low)
                if has_positive_utility_gain(profile[i], allocation[i], new_allocation[i]):
                    num_better += 1
        profile_count += bool(num_better)
        profitable_reports += num_better
        per_profile[num_better] += 1
        if num_better:
            top_patterns[tuple(sum(p[0] == j for p in profile) for j in range(3))] += 1
    assert (profile_count, profitable_reports) == (30, 36)
    assert per_profile == Counter({0: 186, 1: 24, 2: 6})
    assert sum(top_patterns.values()) == 30
    true = event_algorithm(example, low)[1]
    mis = event_algorithm((example[0], (2, 0, 1), example[2]), low)[1]
    assert true == (F(2, 3), F(1, 3), F(0))
    assert mis == (F(1, 4), F(1, 4), F(1, 2))
    utilities = (12, 1, 11)
    true_eu = sum(x*y for x, y in zip(true, utilities))
    mis_eu = sum(x*y for x, y in zip(mis, utilities))
    assert mis_eu - true_eu == F(5, 12)
    print('PASS: independent rational event/polytope algorithms:', profiles_checked, 'profiles')
    print('PASS: one-positive-minimum closed form:', formula_checked, 'four-agent profiles')
    print('PASS: susceptible true profiles 30/216; profitable agent-reports 36/3240')
    print('PASS: per-profile deviations', dict(sorted(per_profile.items())))
    print('PASS: strict-utility example improvement', mis_eu - true_eu)


if __name__ == '__main__':
    verify()
