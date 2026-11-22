"""Finite checks for a degree-constrained adjacency trace growth formula.

Pure standard-library Python. Execute: python check.py
"""
from itertools import combinations
from math import comb


def layers(m, d):
    if m < 1 or d < 0:
        raise ValueError('m must be positive and d nonnegative')
    if d == 0:
        return 0, 0
    r = 0
    used = 0
    for j in range(1, m + 1):
        b = sum(comb(m - 1, i) for i in range(j))
        if b <= d:
            r, used = j, b
        else:
            break
    return r, d - used if r < m else 0


def bound(m, d):
    r, rho = layers(m, d)
    return 1 + sum(comb(m, j) for j in range(1, r + 1)) + (
        (m * rho) // (r + 1) if r < m and d else 0
    )


def balanced_family(m, k, count):
    """Select count distinct k-subsets with almost-equal vertex degrees.

    A local-exchange descent on sum of squared degrees.  The proof in
    RESULT.md establishes that the stopping state is always balanced.
    """
    available = list(combinations(range(m), k))
    assert 0 <= count <= len(available)
    chosen = set(available[:count])
    degrees = [0] * m
    for edge in chosen:
        for v in edge:
            degrees[v] += 1
    while degrees and max(degrees) - min(degrees) > 1:
        changed = False
        for high in sorted(range(m), key=lambda v: (-degrees[v], v)):
            for low in sorted(range(m), key=lambda v: (degrees[v], v)):
                if degrees[high] < degrees[low] + 2:
                    continue
                for e in sorted(chosen):
                    if high in e and low not in e:
                        new_edge = tuple(sorted((set(e) - {high}) | {low}))
                        if new_edge not in chosen:
                            chosen.remove(e)
                            chosen.add(new_edge)
                            degrees[high] -= 1
                            degrees[low] += 1
                            changed = True
                            break
                if changed:
                    break
            if changed:
                break
        assert changed, 'exchange lemma would be false'
    assert len(chosen) == count
    assert max(degrees, default=0) - min(degrees, default=0) <= 1
    return sorted(chosen)


def witness(m, d):
    r, rho = layers(m, d)
    family = [tuple(e) for j in range(1, r + 1)
              for e in combinations(range(m), j)]
    if d and r < m:
        count = m * rho // (r + 1)
        family.extend(balanced_family(m, r + 1, count))
    adj = [set() for _ in range(m + len(family))]
    for i, e in enumerate(family, m):
        for a in e:
            adj[i].add(a)
            adj[a].add(i)
    return adj, family


def trace_count(adj, marked):
    A = set(marked)
    return len({frozenset(nbrs & A) for nbrs in adj})



def minimum_host_witness(m, d):
    """Minimum-order extremizer with pairwise distinct marked traces."""
    if d == 0:
        return [set() for _ in range(m)]
    r, rho = layers(m, d)
    family = {tuple(e) for j in range(1, r + 1)
              for e in combinations(range(m), j)}
    if r < m:
        family.update(balanced_family(m, r + 1, m * rho // (r + 1)))
    family.add(())
    adj = [set() for _ in range(m)]
    marked_edges = []
    if r == 1:
        marked_edges = [(i, i + 1) for i in range(0, m - 1, 2)]
    elif m == 2:
        marked_edges = [(0, 1)]
    elif m == 3:
        marked_edges = [(0, 1), (1, 2), (0, 2)]
    elif m >= 4:
        marked_edges = [(i, i + 1) for i in range(m - 1)]
    for u, v in marked_edges:
        adj[u].add(v)
        adj[v].add(u)
    marked_traces = {tuple(sorted(adj[i])) for i in range(m)}
    assert len(marked_traces) == m
    assert marked_traces <= family
    for e in sorted(family - marked_traces):
        v = len(adj)
        adj.append(set(e))
        for u in e:
            adj[u].add(v)
    assert len(adj) == len(family) == bound(m, d)
    assert max(map(len, adj)) <= d
    assert trace_count(adj, range(m)) == bound(m, d)
    return adj


def minimum_host_check():
    ntests = 0
    for m in range(1, 13):
        for d in range(1, 50):
            minimum_host_witness(m, d)
            ntests += 1
    print('MINIMUM_HOSTS_OK', ntests)

def finite_family_check():
    for m in range(1, 10):
        for d in range(0, 25):
            g, family = witness(m, d)
            assert max(map(len, g)) <= d
            assert len(family) + 1 == bound(m, d)
            assert trace_count(g, range(m)) == bound(m, d)
    print('CONSTRUCTIONS_OK 225 parameter pairs')


def balanced_check():
    tests = 0
    for m in range(1, 9):
        for k in range(1, m + 1):
            for count in range(comb(m, k) + 1):
                balanced_family(m, k, count)
                tests += 1
    print('EQUITABLE_FAMILIES_OK', tests)


def family_budget_check():
    m = 4
    subsets = [s for s in range(1, 1 << m)]
    best = {d: 0 for d in range(0, 9)}
    for mask in range(1 << len(subsets)):
        degree = [0] * m
        number = 0
        for i, s in enumerate(subsets):
            if (mask >> i) & 1:
                number += 1
                for a in range(m):
                    degree[a] += (s >> a) & 1
        d = max(degree)
        for cap in range(d, 9):
            best[cap] = max(best[cap], number + 1)
    assert all(best[d] == bound(m, d) for d in best), (best, [bound(m, d) for d in best])
    print('ALL_4_MARK_FAMILIES_OK', 1 << len(subsets))


def graphs_check():
    cases = 0
    for n in range(1, 7):
        pairs = list(combinations(range(n), 2))
        for mask in range(1 << len(pairs)):
            adj = [set() for _ in range(n)]
            for i, (a, b) in enumerate(pairs):
                if mask & (1 << i):
                    adj[a].add(b)
                    adj[b].add(a)
            d = max(map(len, adj))
            for smask in range(1, 1 << n):
                marked = [a for a in range(n) if smask & (1 << a)]
                assert trace_count(adj, marked) <= bound(len(marked), d)
                cases += 1
    print('ALL_GRAPHS_THROUGH_6_OK', cases)


if __name__ == '__main__':
    finite_family_check()
    minimum_host_check()
    balanced_check()
    family_budget_check()
    graphs_check()
    print('ALL_CHECKS_OK')
