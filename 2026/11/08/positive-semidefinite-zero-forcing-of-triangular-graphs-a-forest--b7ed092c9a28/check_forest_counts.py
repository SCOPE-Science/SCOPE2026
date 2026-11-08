"""Independent enumeration of the labeled-forest generating polynomial.

Method A: enumerate set partitions and weight each tree block by Cayley's formula.
Method B: enumerate edge sets, reject cycles with union-find; no forcing simulation.
"""
from collections import defaultdict
from itertools import combinations
from math import comb


def partition_forest_counts(n):
    profile = defaultdict(int)
    blocks = [[0]]
    def walk(v):
        if v == n:
            ways = 1
            for block in blocks:
                s = len(block)
                if s > 1:
                    ways *= s ** (s - 2)
            profile[n - len(blocks)] += ways
            return
        for block in blocks:
            block.append(v)
            walk(v + 1)
            block.pop()
        blocks.append([v])
        walk(v + 1)
        blocks.pop()
    walk(1)
    return dict(sorted(profile.items()))


def direct_forest_counts(n):
    edges = list(combinations(range(n), 2))
    counts = defaultdict(int)
    for mask in range(1 << len(edges)):
        parent = list(range(n))
        def root(x):
            while x != parent[x]:
                x = parent[x]
            return x
        good = True
        for i, (u, v) in enumerate(edges):
            if not (mask & (1 << i)):
                continue
            a, b = root(u), root(v)
            if a == b:
                good = False
                break
            parent[a] = b
        if good:
            counts[mask.bit_count()] += 1
    return dict(sorted(counts.items()))


def tree_count(s):
    return 1 if s == 1 else s ** (s - 2)


def main():
    for n in range(3, 9):
        profile = partition_forest_counts(n)
        if n <= 6:
            assert profile == direct_forest_counts(n)
        minimum_psd_sets = profile[n - 2]
        two_component_formula = sum(comb(n, a) * tree_count(a) * tree_count(n-a)
                                    for a in range(1, n)) // 2
        assert minimum_psd_sets == two_component_formula
        valid = {k: c for k, c in profile.items() if k <= n-2}
        print(f'n={n} forest_coefficients={valid} minimum_psd_sets={minimum_psd_sets}')
    print('FOREST_PARTITION_ENUMERATOR_PASS')


if __name__ == '__main__':
    main()
