#!/usr/bin/env python3
"""Independent finite checks of the friendship-network token-swapping theorem.

Requires Python >=3.9; no third-party packages or external files.
This is a finite diagnostic, not the proof for arbitrary network size.
"""
from collections import Counter, deque
from math import factorial, comb


def forbidden_free_matchings(t):
    """Inclusion-exclusion for matching avoidance of t disjoint edges."""
    def odd_double_factorial(v):
        value = 1
        for x in range(v, 0, -2):
            value *= x
        return value
    return sum((-1)**j * comb(t, j) * odd_double_factorial(2*(t-j)-1)
               for j in range(t + 1))


def eligible_far(s):
    n = len(s)
    if s[0] != 0:
        return False
    if any(s[i] == i or s[s[i]] != i for i in range(1, n)):
        return False
    return all((i - 1)//2 != (s[i] - 1)//2 for i in range(1, n))


def exhaust(t):
    n = 2*t+1
    edges = [(0, i) for i in range(1, n)]
    edges += [(2*i+1, 2*i+2) for i in range(t)]
    source = tuple(range(n))
    distances = {source: 0}
    queue = deque((source,))
    while queue:
        u = queue.popleft()
        for x, y in edges:
            v = list(u)
            v[x], v[y] = v[y], v[x]
            v = tuple(v)
            if v not in distances:
                distances[v] = distances[u] + 1
                queue.append(v)
    assert len(distances) == factorial(n), ('states', t)
    layers = Counter(distances.values())
    diameter = max(layers)
    far_states = {p for p, d in distances.items() if d == diameter}
    expected = 2 if t == 1 else 3*t
    assert diameter == expected, ('diameter', t, diameter, expected)
    if t >= 2:
        theoretical = forbidden_free_matchings(t)
        classified = {p for p in distances if eligible_far(p)}
        assert far_states == classified, ('antipodal-classification', t)
        assert len(far_states) == theoretical, ('antipode-count', t)
    else:
        theoretical = len(far_states)
    return t, n, len(distances), len(edges), diameter, theoretical, sorted(layers.items())

if __name__ == '__main__':
    for t in (1, 2, 3, 4):
        print('case', exhaust(t))
    print('PASS: every configuration and every edge from the identity was enumerated for t=1..4.')
    print('PASS: diameter and full antipodal classification agree for t=2..4.')
    print('LIMIT: finite checks do not establish claims for t>=5; all-order proof is in RESULT.md.')
