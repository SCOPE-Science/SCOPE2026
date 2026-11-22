#!/usr/bin/env python3
"""Exact, self-contained certificate for fifth-residue hyperbinary balance.

The finite transition closure, rather than a cutoff on the integer m, proves
coverage of every possible binary-index state by induction.
"""
import json
from collections import Counter, deque
from pathlib import Path


def shift(a):
    """Multiply by t in Z[t]/(t**4+t**3+t**2+t+1)."""
    x, y, z, w = a
    return (-w, x - w, y - w, z - w)


def plus(a, b):
    return tuple(x + y for x, y in zip(a, b))


def next_states(pair):
    a, b = pair
    e = plus(a, shift(shift(b)))
    return ((e, shift(b)), (shift(a), e))


def span(a):
    counts = (0,) + tuple(a)
    return max(counts) - min(counts)


def main():
    filename = Path(__file__).resolve().with_name('states.json')
    data = json.loads(filename.read_text(encoding='utf-8'))
    assert isinstance(data, list)
    states = [tuple(tuple(int(x) for x in v) for v in s) for s in data]
    assert len(states) == 120
    assert len(set(states)) == 120
    assert all(len(s) == 2 and all(len(v) == 4 for v in s) for s in states)
    assert states == sorted(states)
    base = ((0, 1, 0, 0), (1, 0, 0, 0))
    universe = set(states)
    assert base in universe
    # Two exact integer transitions for EVERY certified state.
    assert all(set(next_states(s)) <= universe for s in universe)
    seen, todo = {base}, deque([base])
    while todo:
        s = todo.popleft()
        for successor in next_states(s):
            if successor not in seen:
                seen.add(successor)
                todo.append(successor)
    assert seen == universe
    spreads = Counter(span(s[0]) for s in universe)
    assert spreads == Counter({0: 10, 1: 100, 2: 10}), spreads
    assert len({s[0] for s in universe}) == 31
    print('EXACT_120_STATE_CLOSURE_AND_REACHABILITY_PASS', len(universe))
    print('ALL_240_TRANSITIONS_CLOSED_PASS')
    print('FIFTH_RESIDUE_SPREAD_HISTOGRAM_PASS', dict(sorted(spreads.items())))
    # Independent coefficient-polynomial recurrence, not based on states.
    polys = [[1], [0, 1]]
    upper = 12000
    for m in range(2, upper + 1):
        if m % 2:
            polys.append([0] + polys[m // 2])
        else:
            one, two = polys[m // 2], [0, 0] + polys[m // 2 - 1]
            polys.append([(one[j] if j < len(one) else 0) +
                         (two[j] if j < len(two) else 0)
                         for j in range(max(len(one), len(two)))])
        bucket = [sum(c for j, c in enumerate(polys[m]) if j % 5 == r)
                  for r in range(5)]
        assert max(bucket) - min(bucket) <= 2, (m, bucket)
    assert polys[10] == [0, 0, 1, 2, 1, 1]
    assert [sum(c for j, c in enumerate(polys[10]) if j % 5 == r)
            for r in range(5)] == [1, 0, 1, 2, 1]
    print('INDEPENDENT_COEFFICIENT_RECURSION_PASS', upper + 1)
    print('SHARPNESS_AT_TEN_PASS')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
