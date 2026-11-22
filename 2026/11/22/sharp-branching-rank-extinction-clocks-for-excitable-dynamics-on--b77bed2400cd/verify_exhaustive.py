#!/usr/bin/env python3
"""Independent finite-state checks for sharp excitation extinction on finite trees.
Python 3 with NetworkX installed. Reads no input files.
"""
from functools import lru_cache
import networkx as nx


def branching_height(g, theta):
    @lru_cache(maxsize=None)
    def height(v, parent):
        hs = sorted((height(u, v) for u in g.neighbors(v) if u != parent), reverse=True)
        return 1 + hs[theta - 1] if len(hs) >= theta else 0
    return max(height(v, -1) for v in g.nodes())


def transitions(g, theta, colors):
    neighbors = tuple(tuple(g.neighbors(v)) for v in g.nodes())
    bases = [colors ** j for j in g.nodes()]
    out = [0] * (colors ** len(g))
    for state in range(len(out)):
        xs = tuple((state // base) % colors for base in bases)
        next_val = 0
        for v, z in enumerate(xs):
            if z == 0:
                z_new = int(sum(xs[u] == 1 for u in neighbors[v]) >= theta)
            else:
                z_new = (z + 1) % colors
            next_val += bases[v] * z_new
        out[state] = next_val
    return out


def maximum_hitting_time(next_state):
    N = len(next_state)
    times = [-1] * N
    times[0] = 0
    for start in range(1, N):
        if times[start] >= 0:
            continue
        path = []
        seen = set()
        x = start
        while times[x] < 0 and x not in seen:
            seen.add(x)
            path.append(x)
            x = next_state[x]
        assert x not in seen, 'Unexpected periodic nonzero state'
        for y in reversed(path):
            times[y] = times[next_state[y]] + 1
    return max(times)


def main():
    configs = 0
    graphs = 0
    cases = 0
    scenarios = ((2, 3, 9), (2, 4, 7), (3, 3, 8), (3, 4, 7), (4, 3, 8))
    for theta, colors, nmax in scenarios:
        maxima = []
        for n in range(1, nmax + 1):
            largest = 0
            for raw in nx.nonisomorphic_trees(n):
                g = nx.convert_node_labels_to_integers(raw)
                H = branching_height(g, theta)
                expected = colors - 1 + H
                actual = maximum_hitting_time(transitions(g, theta, colors))
                assert actual == expected, (theta, colors, n, H, actual)
                largest = max(largest, actual)
                graphs += 1
                cases += 1
                configs += colors ** n
            maxima.append(largest)
        print('theta=%d colors=%d up_to_n=%d extrema=%s' % (theta, colors, nmax, maxima))
    print('PASS all_nonisomorphic_trees=%d graph_parameter_cases=%d state_checks=%d' % (graphs, cases, configs))

if __name__ == '__main__':
    main()
