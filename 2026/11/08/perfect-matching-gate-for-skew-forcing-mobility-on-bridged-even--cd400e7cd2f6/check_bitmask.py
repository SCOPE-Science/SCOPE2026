#!/usr/bin/env python3
"""Exhaustive finite checks of skew-forcing configurations of port-cycle cacti."""
from itertools import combinations
import json

CASES = [
    ("two_4_4", [4, 4], [(0, 1)], True),
    ("two_4_6", [4, 6], [(0, 1)], True),
    ("two_6_6", [6, 6], [(0, 1)], True),
    ("path_four_4", [4, 4, 4, 4], [(0, 1), (1, 2), (2, 3)], True),
    ("path_three_4", [4, 4, 4], [(0, 1), (1, 2)], False),
    ("star_four_4", [4, 4, 4, 4], [(0, 1), (0, 2), (0, 3)], False),
]

def run(name, lengths, tree_edges, matched):
    n = sum(lengths)
    starts = [sum(lengths[:i]) for i in range(len(lengths))]
    adj = [0] * n
    for s, m in zip(starts, lengths):
        for j in range(m):
            u, v = s + j, s + (j + 1) % m
            adj[u] |= 1 << v
            adj[v] |= 1 << u
    for i, j in tree_edges:
        u, v = starts[i], starts[j]
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    def forced(seed):
        blue = seed
        while True:
            new = 0
            for nbr in adj:
                white = nbr & ~blue
                if white and white & (white - 1) == 0:
                    new |= white
            if not (new & ~blue):
                return blue == (1 << n) - 1
            blue |= new

    k = len(lengths)
    # The disjoint alternating-cycle forts prove no set of size < k can work.
    # We also test every such candidate independently in the finite cases.
    for j in range(k):
        assert not any(forced(sum(1 << x for x in c)) for c in combinations(range(n), j))
    opt = {sum(1 << x for x in c) for c in combinations(range(n), k)
           if forced(sum(1 << x for x in c))}
    expected = {sum(1 << (s + p) for s, p in zip(starts, ps))
                for ps in __import__('itertools').product(*[range(1, m, 2) for m in lengths])}
    if matched:
        assert opt == expected, (name, len(opt), len(expected), opt ^ expected)
        jump = set()
        slide = set()
        for x in opt:
            for a in range(n):
                if not (x >> a) & 1:
                    continue
                for b in range(n):
                    if (x >> b) & 1:
                        continue
                    y = x ^ (1 << a) ^ (1 << b)
                    if y in opt:
                        jump.add(tuple(sorted((x, y))))
                        if (adj[a] >> b) & 1:
                            slide.add(tuple(sorted((x, y))))
        r = [m // 2 for m in lengths]
        assert len(jump) == len(opt) * sum(q-1 for q in r) // 2
        assert not slide
    else:
        assert not opt, (name, 'unexpected size-k forcing set')
        jump = set()
        slide = set()
    return {'case': name, 'n': n, 'cycle_count': k, 'tree_has_perfect_matching': matched,
            'skew_forcing_sets_below_k': 0, 'forcing_sets_at_k': len(opt),
            'predicted_count_if_matched': len(expected), 'token_exchange_edges':len(jump),
            'token_slide_edges':len(slide)}

if __name__ == '__main__':
    print(json.dumps([run(*case) for case in CASES], sort_keys=True, indent=2))
