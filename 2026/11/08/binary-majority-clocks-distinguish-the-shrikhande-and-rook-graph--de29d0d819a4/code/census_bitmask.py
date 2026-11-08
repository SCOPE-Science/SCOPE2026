#!/usr/bin/env python3
"""Complete binary-majority functional-graph census on two 16-vertex SRGs.

Python 3, standard library only. Each initial state is a 16-bit integer;
the update is synchronous strict open-neighbour majority, retaining ties.
The traversal visits every vertex of each 65536-state functional graph.
"""
from collections import Counter
import hashlib
import json

N = 16
TOTAL = 1 << N


def graph_masks(graph):
    masks = []
    for i in range(4):
        for j in range(4):
            if graph == 'rook':
                vertices = [(k, l) for k in range(4) for l in range(4)
                            if (k, l) != (i, j) and (k == i or l == j)]
            elif graph == 'shrikhande':
                shifts = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1))
                vertices = [((i + a) % 4, (j + b) % 4) for a, b in shifts]
            else:
                raise ValueError(graph)
            masks.append(sum(1 << (4 * k + l) for k, l in vertices))
    assert all(m.bit_count() == 6 for m in masks)
    assert all(((masks[i] >> j) & 1) == ((masks[j] >> i) & 1)
               for i in range(N) for j in range(N))
    assert all((masks[i] & masks[j]).bit_count() == 2
               for i in range(N) for j in range(i + 1, N))
    return masks


def step(x, masks):
    y = 0
    for i in range(N):
        k = (x & masks[i]).bit_count()
        if k > 3 or (k == 3 and (x & (1 << i))):
            y |= 1 << i
    return y


def census(masks):
    nxt = [step(x, masks) for x in range(TOTAL)]
    # A digest makes the entire labelled transition function reproducible.
    transition_digest = hashlib.sha256(b''.join(
        y.to_bytes(2, 'little') for y in nxt)).hexdigest()
    t = [-1] * TOTAL
    period = [0] * TOTAL
    cycles = Counter()
    for x in range(TOTAL):
        if t[x] >= 0:
            continue
        path = []
        position = {}
        z = x
        while t[z] < 0 and z not in position:
            position[z] = len(path)
            path.append(z)
            z = nxt[z]
        if z in position:
            beginning = position[z]
            orbit = path[beginning:]
            p = len(orbit)
            cycles[p] += 1
            for u in orbit:
                t[u] = 0
                period[u] = p
            path = path[:beginning]
        for u in reversed(path):
            t[u] = t[nxt[u]] + 1
            period[u] = period[nxt[u]]
    assert all(s >= 0 for s in t)
    assert all(p in (1, 2) for p in period)
    classes = Counter((t[x], period[x]) for x in range(TOTAL))
    fixed_weight = Counter(x.bit_count() for x in range(TOTAL)
                           if nxt[x] == x)
    alternating_weight = Counter(x.bit_count() for x in range(TOTAL)
                                 if nxt[x] != x and nxt[nxt[x]] == x)
    assert sum(classes.values()) == TOTAL
    assert cycles[1] == classes[(0, 1)]
    assert 2 * cycles[2] == classes[(0, 2)]
    return {'cycle_orbits': {str(k): cycles[k] for k in sorted(cycles)},
            'time_period': {f'{k[0]}:{k[1]}': v for k, v in sorted(classes.items())},
            'fixed_by_ones': {str(k): v for k, v in sorted(fixed_weight.items())},
            'primitive_2period_by_ones': {str(k): v for k, v in sorted(alternating_weight.items())},
            'max_entry_time': max(t),
            'transition_sha256_le16': transition_digest}


def main():
    result = {name: census(graph_masks(name))
              for name in ('rook', 'shrikhande')}
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
