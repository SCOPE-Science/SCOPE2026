"""Exhaustive independent simulation of the positive-semidefinite color-change rule.

All vertices of a triangular graph are labeled by unordered pairs of [n].
This script enumerates every initial coloring for n=3,4,5,6.
"""
from itertools import combinations
from collections import Counter


def is_psd_forcing(incident):
    m = len(incident)
    adjacency = [0] * m
    for i in range(m):
        for j in range(m):
            if i != j and set(incident[i]) & set(incident[j]):
                adjacency[i] |= 1 << j
    def simulation(white):
        while white:
            unseen = white
            components = []
            while unseen:
                first = unseen & -unseen
                comp, stack = first, first
                unseen ^= first
                while stack:
                    vbit = stack & -stack
                    stack ^= vbit
                    v = vbit.bit_length() - 1
                    neighbors = adjacency[v] & unseen
                    unseen ^= neighbors
                    stack |= neighbors
                    comp |= neighbors
                components.append(comp)
            forced = 0
            for component in components:
                for v in range(m):
                    if white & (1 << v):
                        continue
                    candidates = adjacency[v] & component
                    if candidates.bit_count() == 1:
                        forced |= candidates
            if not forced:
                return False
            white &= ~forced
        return True
    return simulation


def white_is_forest_with_two_components(n, edges):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        parent[ra] = rb
    return len({find(v) for v in range(n)}) >= 2


def main():
    for n in range(3, 7):
        edges = list(combinations(range(n), 2))
        positive = Counter()
        mismatches = 0
        psd = is_psd_forcing(edges)
        for mask in range(1 << len(edges)):
            whites = [edge for i, edge in enumerate(edges) if mask & (1 << i)]
            actual = psd(mask)
            structural = white_is_forest_with_two_components(n, whites)
            if actual != structural:
                mismatches += 1
            if actual:
                positive[len(whites)] += 1
        assert mismatches == 0
        print(f'n={n} tested={1 << len(edges)} white_edge_counts={dict(sorted(positive.items()))} mismatches={mismatches}')
    print('PSD_COLOR_RULE_EXHAUSTIVE_PASS')


if __name__ == '__main__':
    main()
