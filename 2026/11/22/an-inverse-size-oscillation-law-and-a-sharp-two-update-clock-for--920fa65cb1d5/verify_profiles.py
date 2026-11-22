#!/usr/bin/env python3
"""Weighted six-pair-profile verification and exact closed-form counts.

The graph is represented by partner-pair types, not by its adjacency lists.
An ordered unlike-colour pair has multiplicity two. No external packages.
"""
from collections import Counter
from itertools import combinations_with_replacement
from math import comb, factorial

TYPES = ((0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2))


def formula_fixed(m):
    out = 3 + 3 * sum(comb(m, c) * 2**(m-c) for c in range(m+1) if m > 3*c)
    if m % 3 == 0:
        j = m // 3
        out += factorial(m) // factorial(j)**3
    if m == 2:
        out += 24
    return out


def formula_top_tie(m):
    F = factorial
    total = 0
    for a in range(m//2 + 1):
        for v in range((m-2*a)//2 + 1):
            for c in range(m-2*a-2*v+1):
                u = m - 2*a - 2*v - c
                if a+v == 0 or 2*a+u <= 2*c+v:
                    continue
                total += 3 * F(m) * 2**(u+2*v) // (F(a)**2 * F(v)**2 * F(c) * F(u))
    return total


def formula_three_tie(m):
    if m % 3:
        return 0
    out = 0
    for indices in combinations_with_replacement(range(6), m):
        a, b, c, u, v, w = (indices.count(i) for i in range(6))
        if 2*a+u+v != 2*b+u+w or 2*a+u+v != 2*c+v+w:
            continue
        leaders = sorted((a+w, b+v, c+u), reverse=True)
        if leaders[0] != leaders[1] or leaders[1] <= leaders[2]:
            continue
        out += factorial(m)*2**(u+v+w) // (
            factorial(a)*factorial(b)*factorial(c)*
            factorial(u)*factorial(v)*factorial(w))
    return out


def formula_rare(m):
    return 0 if m == 2 else 12*m*comb(m-1, (m-1)//2)


def formula_immediate_period2(m):
    F = factorial
    out = 0
    for a in range(1, m//2+1):
        for c in range(m-2*a+1):
            u = m - 2*a - c
            if 2*a+u > 2*c:
                out += 3*F(m)*2**u // (F(a)**2*F(c)*F(u))
    if m >= 3 and m % 2:
        out += formula_rare(m)
    return out


def next_profile(state):
    hist = [0, 0, 0]
    for a, b in state:
        hist[a] += 1
        hist[b] += 1
    output = []
    for a, b in state:
        tally = [hist[k] - (a == k) - (b == k) for k in range(3)]
        largest = max(tally)
        if tally.count(largest) == 1:
            winner = tally.index(largest)
            output.append((winner, winner))
        else:
            output.append((a, b))
    return tuple(output)


def exact_by_profiles(m):
    fixed = immediate_two = basin_two = 0
    classes = 0
    longest = 0
    for indices in combinations_with_replacement(range(6), m):
        q = [indices.count(i) for i in range(6)]
        multiplicity = factorial(m)*2**sum(q[3:])
        for count in q:
            multiplicity //= factorial(count)
        x = tuple(TYPES[i] for i in indices)
        seen = {}
        path = []
        while x not in seen:
            seen[x] = len(path)
            path.append(x)
            x = next_profile(x)
        depth = seen[x]
        p = len(path)-depth
        assert p in (1, 2)
        assert depth <= 2
        if p == 2:
            basin_two += multiplicity
            if depth == 0:
                immediate_two += multiplicity
        elif depth == 0:
            fixed += multiplicity
        longest = max(longest, depth)
        classes += 1
    return fixed, immediate_two, basin_two, longest, classes


if __name__ == '__main__':
    for m in range(2, 13):
        fixed, immediate, basin, depth, classes = exact_by_profiles(m)
        assert fixed == formula_fixed(m), (m, fixed, formula_fixed(m))
        assert basin == (formula_top_tie(m)+formula_rare(m)+formula_three_tie(m)), m
        assert immediate == formula_immediate_period2(m), m
        assert immediate % 2 == 0
        assert depth == (1 if m == 2 else 2), m
        print('m=%d classes=%d fixed=%d two_cycle_orbits=%d '
              'period2_basin=%d max_entry=%d' %
              (m, classes, fixed, immediate//2, basin, depth))
    print('WEIGHTED PROFILE VERIFICATION PASS')
