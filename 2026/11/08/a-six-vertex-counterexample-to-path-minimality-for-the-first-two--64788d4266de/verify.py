#!/usr/bin/env python3
"""Exact checks for an exceptional first-fit colouring on six-vertex trees.

No random sampling or third-party packages. Two independent enumeration
strategies verify the six-vertex result, and Prüfer sequences check all
smaller labelled trees (hence all their isomorphism classes).
"""
from collections import defaultdict, Counter
from fractions import Fraction
from itertools import permutations, product
from math import factorial


def adjacency(n, edges):
    assert len(edges) == max(0, n-1)
    a = [set() for _ in range(n)]
    for u, v in edges:
        assert 0 <= u < n and 0 <= v < n and u != v
        a[u].add(v); a[v].add(u)
    return a


def first_fit(order, adj):
    colors = [0] * len(adj)
    for v in order:
        taken = {colors[w] for w in adj[v] if colors[w] != 0}
        c = 1
        while c in taken:
            c += 1
        colors[v] = c
    return colors


def by_permutations(adj):
    n = len(adj)
    counts = [0] * n
    histogram = Counter()
    sum_accepted = 0
    for order in permutations(range(n)):
        colors = first_fit(order, adj)
        for v in range(n):
            if colors[v] > 2:
                counts[v] += 1
        accepted = sum(c <= 2 for c in colors)
        histogram[accepted] += 1
        sum_accepted += accepted
    assert sum(histogram.values()) == factorial(n)
    assert sum(counts) + sum_accepted == n * factorial(n)
    return sum_accepted, tuple(counts), dict(sorted(histogram.items()))


def by_state_dp(adj):
    """Count all orders by merging identical labelled partial colourings."""
    n = len(adj)
    states = {(0, (0,) * n): 1}
    for step in range(n):
        nxt = defaultdict(int)
        for (mask, col), mult in states.items():
            for v in range(n):
                if mask & (1 << v):
                    continue
                taken = {col[w] for w in adj[v] if col[w] != 0}
                c = 1
                while c in taken:
                    c += 1
                colors = list(col); colors[v] = c
                nxt[(mask | (1 << v), tuple(colors))] += mult
        states = nxt
        assert sum(states.values()) == factorial(n) // factorial(n - step - 1)
    counts = [0] * n
    sum_accepted = 0
    hist = Counter()
    for (mask, colors), multiplicity in states.items():
        assert mask == 2 ** n - 1
        accepted = sum(x <= 2 for x in colors)
        sum_accepted += accepted * multiplicity
        hist[accepted] += multiplicity
        for v in range(n):
            if colors[v] > 2:
                counts[v] += multiplicity
    return sum_accepted, tuple(counts), dict(sorted(hist.items()))


def prufer_tree(seq):
    n = len(seq) + 2
    degree = [1] * n
    for x in seq:
        degree[x] += 1
    edges = []
    for x in seq:
        leaf = next(i for i in range(n) if degree[i] == 1)
        edges.append((leaf, x))
        degree[leaf] -= 1
        degree[x] -= 1
    i, j = (x for x in range(n) if degree[x] == 1)
    edges.append((i, j))
    return edges


def main():
    path = [(i, i + 1) for i in range(5)]
    fork = [(0, 1), (1, 2), (0, 3), (3, 4), (0, 5)]
    a_path = adjacency(6, path)
    a_fork = adjacency(6, fork)
    paths = by_permutations(a_path)
    forks = by_permutations(a_fork)
    assert paths == by_state_dp(a_path)
    assert forks == by_state_dp(a_fork)
    assert paths == (3970, (0, 71, 104, 104, 71, 0), {5: 350, 6: 370})
    assert forks == (3930, (174, 108, 0, 108, 0, 0), {4: 30, 5: 330, 6: 360})
    assert Fraction(paths[0], 720) == Fraction(397, 72)
    assert Fraction(forks[0], 720) == Fraction(131, 24)
    assert Fraction(paths[0] - forks[0], 720) == Fraction(1, 18)
    print('P6 first-two count per vertex for colour >=3:', paths[1])
    print('T6 first-two count per vertex for colour >=3:', forks[1])
    print('P6 accepted-count histogram:', paths[2])
    print('T6 accepted-count histogram:', forks[2])
    print('Expected first-two: P6 = 397/72, T6 = 131/24, gap = 1/18')
    for n in range(1, 6):
        p = adjacency(n, [(i, i + 1) for i in range(n - 1)])
        path_avg = Fraction(by_permutations(p)[0], factorial(n))
        if n == 1:
            edge_lists = [[]]
        elif n == 2:
            edge_lists = [[(0, 1)]]
        else:
            edge_lists = [prufer_tree(seq) for seq in product(range(n), repeat=n - 2)]
        smallest = None
        equal = 0
        for edges in edge_lists:
            avg = Fraction(by_permutations(adjacency(n, edges))[0], factorial(n))
            if smallest is None or avg < smallest:
                smallest = avg
            if avg == path_avg:
                equal += 1
        assert smallest == path_avg
        print(f'n={n}: path expectation={path_avg}; minimum={smallest}; labelled trees tested={len(edge_lists)}; equal-labelled={equal}')
    print('All exact checks passed; no finite observation is extrapolated to larger tree orders.')


if __name__ == '__main__':
    main()
