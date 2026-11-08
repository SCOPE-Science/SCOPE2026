"""Independent finite checks for the connected-support theorem on theta graphs."""
from itertools import combinations, product
from math import comb


def theta(arms):
    edges = [set(), set()]
    branches = []
    for count in arms:
        branch = tuple(range(len(edges), len(edges) + count))
        edges.extend(set() for _ in branch)
        walk = (0,) + branch + (1,)
        for x, y in zip(walk, walk[1:]):
            edges[x].add(y)
            edges[y].add(x)
        branches.append(branch)
    return edges, branches


def reachable(edges, x, y, excluded):
    seen, queue = {x}, [x]
    for v in queue:
        for w in edges[v]:
            if w not in excluded and w not in seen:
                seen.add(w)
                queue.append(w)
    return y in seen


def pairwise_test(edges, support):
    for x, y in combinations(support, 2):
        if not reachable(edges, x, y, set(support) - {x, y}):
            return False
    return True


def direct_test(edges, support):
    n = len(edges)
    patterns = {0}
    support_bits = sum(1 << x for x in support)
    for mask in range(1, 1 << n):
        start = (mask & -mask).bit_length() - 1
        reached, queue = {start}, [start]
        for x in queue:
            for y in edges[x]:
                if mask & (1 << y) and y not in reached:
                    reached.add(y)
                    queue.append(y)
        if len(reached) == mask.bit_count():
            patterns.add(mask & support_bits)
    return len(patterns) == (1 << len(support))


def predicted(branches, support):
    k = len(support)
    if k <= 3:
        return True
    if k >= 5:
        return False
    endpoints = len({0, 1}.intersection(support))
    counts = sorted(len(set(support).intersection(branch)) for branch in branches)
    return (endpoints == 1 and counts == [1, 1, 1]) or (endpoints == 0 and counts in ([0, 2, 2], [1, 1, 2]))


def coefficient_four(a, b, c):
    return (2 * a * b * c
            + comb(a, 2) * b * c + comb(b, 2) * a * c + comb(c, 2) * a * b
            + comb(a, 2) * comb(b, 2) + comb(a, 2) * comb(c, 2)
            + comb(b, 2) * comb(c, 2))


def run():
    direct_instances = 0
    for triple in product((1, 2, 3), repeat=3):
        edges, branches = theta(triple)
        if len(edges) > 10:
            continue
        for k in range(min(5, len(edges)) + 1):
            for support in combinations(range(len(edges)), k):
                observed = direct_test(edges, support)
                assert observed == predicted(branches, support), (triple, support)
                direct_instances += 1
    print('DIRECT_CONNECTED_SUBSETS_PASS', direct_instances)

    pair_instances = 0
    for triple in product(range(1, 5), repeat=3):
        edges, branches = theta(triple)
        tally = [0] * 6
        for k in range(6):
            for support in combinations(range(len(edges)), k):
                yes = pairwise_test(edges, support)
                assert yes == predicted(branches, support), (triple, support)
                tally[k] += yes
                pair_instances += 1
        n = len(edges)
        assert tally == [1, n, comb(n, 2), comb(n, 3), coefficient_four(*triple), 0], (triple, tally)
    print('ALL_THETA_ARMS_1_TO_4_PASS', pair_instances)
    print('THETA_CONNECTED_SHATTERING_PASS')


if __name__ == '__main__':
    run()
