#!/usr/bin/env python3
"""Exact rational finite-coalition witness checks; no external dependencies."""
from fractions import Fraction as Q
from itertools import combinations

N = frozenset((0, 1, 2))
SUBSETS = [frozenset(t) for k in range(1, 4) for t in combinations(N, k)]
PARTITIONS = [
    (frozenset((0, 1, 2)),),
    (frozenset((0, 1)), frozenset((2,))),
    (frozenset((0, 2)), frozenset((1,))),
    (frozenset((1, 2)), frozenset((0,))),
    (frozenset((0,)), frozenset((1,)), frozenset((2,))),
]


def witness(d, e):
    assert 0 < d < 1 and 0 < e < d / 2
    weights = {(0, 1): (1 - d) / 2, (0, 2): e / 2, (1, 2): e / 2}
    def pair_sum(s):
        return sum((w for (i, j), w in weights.items() if i in s and j in s), Q(0))
    welfare = {
        frozenset((0,)): Q(0), frozenset((1,)): Q(0), frozenset((2,)): Q(0),
        frozenset((0, 1)): Q(1), frozenset((0, 2)): e, frozenset((1, 2)): e,
        N: 1 - d + 2 * e,
    }
    assert all(0 <= welfare[s] - 2 * pair_sum(s) <= d * welfare[s] for s in SUBSETS)
    assert welfare[frozenset((0, 1))] - 2 * pair_sum(frozenset((0, 1))) == d
    assert all(welfare[s] - 2 * pair_sum(s) == 0 for s in SUBSETS if s != frozenset((0, 1)))

    def utility(i, s):
        return sum((w for (a,b),w in weights.items() if (a == i and b in s) or (b == i and a in s)), Q(0))
    def stable(partition):
        for i in N:
            source = next(s for s in partition if i in s)
            baseline = utility(i, source)
            targets = list(partition) + [frozenset()]
            for target in targets:
                if target == source: continue
                if utility(i, target) > baseline: return False
        return True
    stable_set = [p for p in PARTITIONS if stable(p)]
    assert stable_set == [(N,)], stable_set
    worth = [sum((welfare[s] for s in p),Q(0)) for p in PARTITIONS]
    assert worth[1] == Q(1) and all(w < Q(1) for i,w in enumerate(worth) if i != 1),worth
    assert worth[0] == 1 - d + 2 * e
    assert worth[1] / worth[0] == Q(1) / (1 - d + 2 * e)
    assert 1 < worth[1] / worth[0] < Q(1)/(1-d)
    return worth[1] / worth[0]


def main():
    checked = 0
    for den in range(2, 35):
        for num in range(1, den):
            d = Q(num, den)
            for c in (Q(1, 4), Q(1, 10), Q(1, 100), Q(1, 1000)):
                r = witness(d, d * c)
                assert r > 1
                checked += 1
    assert witness(Q(2, 5), Q(1, 100)) == Q(50,31)
    print('PASS:',checked + 1,'exact rational witness instances; seven coalition slacks, all 5 partitions, all deviations each instance')
    print('At delta=2/5, epsilon=1/100: optimal welfare=1, unique stable welfare=31/50, ratio=50/31')

if __name__ == '__main__': main()
