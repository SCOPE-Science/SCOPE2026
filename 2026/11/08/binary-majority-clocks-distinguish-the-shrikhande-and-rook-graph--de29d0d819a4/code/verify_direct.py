#!/usr/bin/env python3
"""Independent coordinate-by-coordinate exhaustive majority verifier.

Neither a graph functional decomposition nor bitcount neighbour updates are used.
For every one of 2**16 inputs, classify the earliest t for which
F**t(x) equals either F**(t+1)(x) or F**(t+2)(x).
"""
from collections import Counter
import json


def coordinate_neighbors(kind):
    adjacency = {}
    for a in range(4):
        for b in range(4):
            node = (a, b)
            if kind == 'rook':
                adjacency[node] = tuple((c, d) for c in range(4) for d in range(4)
                                        if (c == a or d == b) and (c, d) != node)
            else:
                # The set of increments is the same six Cayley generators
                # specified by the standard Shrikhande graph construction.
                adjacency[node] = tuple(((a + u) % 4, (b + v) % 4)
                                        for u, v in ((1, 0), (0, 1), (-1, -1),
                                                     (-1, 0), (0, -1), (1, 1)))
    return adjacency


def dynamic(g):
    vertices = tuple((a, b) for a in range(4) for b in range(4))
    index = {v: i for i, v in enumerate(vertices)}
    neighbors = [[index[u] for u in g[v]] for v in vertices]

    def update(x):
        # Convert the integer into a list of 16 signed opinions.
        before = [1 if x & 1 << i else -1 for i in range(16)]
        after = []
        for i, neigh in enumerate(neighbors):
            vote = sum(before[j] for j in neigh)
            after.append(1 if vote > 0 else -1 if vote < 0 else before[i])
        return sum(1 << i for i, v in enumerate(after) if v > 0)
    return update


def census(graph):
    f = dynamic(coordinate_neighbors(graph))
    classes = Counter()
    weight1 = Counter()
    weight2 = Counter()
    witnesses = {}
    for x in range(1 << 16):
        cur = x
        found = False
        for t in range(16):
            one = f(cur)
            two = f(one)
            if cur == one or cur == two:
                p = 1 if cur == one else 2
                classes[(t, p)] += 1
                witnesses.setdefault((t, p), x)
                if t == 0:
                    if p == 1:
                        weight1[x.bit_count()] += 1
                    else:
                        weight2[x.bit_count()] += 1
                found = True
                break
            cur = one
        assert found, (graph, x)
    assert sum(classes.values()) == 65536
    assert classes[(0, 2)] % 2 == 0
    return {
        'cycle_orbits': {'1': classes[(0, 1)], '2': classes[(0, 2)] // 2},
        'time_period': {f'{t}:{p}': v for (t, p), v in sorted(classes.items())},
        'fixed_by_ones': {str(k): v for k, v in sorted(weight1.items())},
        'primitive_2period_by_ones': {str(k): v for k, v in sorted(weight2.items())},
        'max_entry_time': max(t for t, _ in classes),
        'witnesses': {f'{t}:{p}': w for (t, p), w in sorted(witnesses.items())},
    }


def main():
    print(json.dumps({name: census(name) for name in ('rook', 'shrikhande')},
                     sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
