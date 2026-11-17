#!/usr/bin/env python3
"""Exhaustive, standard-library-only certificate for open triangular-graph traces.

For an edge support H in K_n, its open J(n,2) trace at xy is the cut
of H with exactly one endpoint in {x,y}. For H with v nonisolated base
vertices, two fresh vertices suffice to represent every possible cut.
"""
from itertools import combinations
from math import factorial, comb


def vertices(edges):
    return 0 if not edges else 1 + max(max(e) for e in edges)


def adjacency(edges):
    v = vertices(edges)
    adj = [0] * v
    for a, b in edges:
        adj[a] |= 1 << b
        adj[b] |= 1 << a
    return adj


def isomorphisms(a, b, count_all=False):
    if len(a) != len(b) or vertices(a) != vertices(b):
        return 0
    aa, bb = adjacency(a), adjacency(b)
    v = len(aa)
    da = [t.bit_count() for t in aa]
    db = [t.bit_count() for t in bb]
    if sorted(da) != sorted(db):
        return 0
    order = sorted(range(v), key=lambda x: (-da[x], x))
    choices = [[j for j in range(v) if db[j] == da[x]] for x in range(v)]
    mapping = [-1] * v
    found = 0

    def walk(i, used):
        nonlocal found
        if i == v:
            found += 1
            return
        x = order[i]
        for y in choices[x]:
            if used & (1 << y):
                continue
            if any(bool(aa[x] & (1 << z)) != bool(bb[y] & (1 << mapping[z]))
                   for z in order[:i]):
                continue
            mapping[x] = y
            walk(i + 1, used | (1 << y))
            mapping[x] = -1
            if found and not count_all:
                return

    walk(0, 0)
    return found


def graph_types(max_edges=5):
    """Generate all unlabelled graphs with k edges and no isolated vertices."""
    levels = [[()]]
    for k in range(1, max_edges + 1):
        types = []
        for edges in levels[-1]:
            v = vertices(edges)
            for a, b in combinations(range(v + 2), 2):
                if b >= v and not ((a < v and b == v) or (a == v and b == v + 1)):
                    continue
                if (a, b) in edges:
                    continue
                candidate = tuple(sorted(edges + ((a, b),)))
                if not any(isomorphisms(candidate, prior) for prior in types):
                    types.append(candidate)
        levels.append(types)
    return levels


def cut_traces(edges, n):
    assert n >= vertices(edges)
    return {
        sum((1 << i) for i, (u, v) in enumerate(edges)
            if (u in (x, y)) != (v in (x, y)))
        for x, y in combinations(range(n), 2)
    }


def shattered(edges, n):
    return len(cut_traces(edges, n)) == (1 << len(edges))


def predicted(n):
    if n < 2:
        raise ValueError('the domain has no vertices')
    fall = lambda r: factorial(n)//factorial(n-r) if n >= r else 0
    s1 = comb(n, 2) if n >= 3 else 0
    s2 = comb(comb(n, 2), 2) if n >= 5 else 0
    s3 = (2 * fall(4) // 3 + fall(5) // 4) if n >= 6 else 0
    s4 = (25 * fall(5) // 24 if n >= 7 else 0)
    if n >= 8:
        s4 += fall(6) // 8
    return [1, s1, s2, s3, s4]


def type_counts(levels, n):
    counts = [1]
    for k in range(1, 6):
        acc = 0
        for e in levels[k]:
            v = vertices(e)
            if n >= v and shattered(e, n):
                acc += (factorial(n) // factorial(n-v)) // isomorphisms(e, e, True)
        counts.append(acc)
    return counts


def exhaustive_direct(n):
    """Independent labelled-support test; no graph-isomorphism reduction."""
    all_edges = list(combinations(range(n), 2))
    N = len(all_edges)
    rows = [sum(1 << j for j, other in enumerate(all_edges)
                if len(set(center).intersection(other)) == 1)
            for center in all_edges]
    counts = [1]
    for k in range(1, min(4, N) + 1):
        seen_shattered = 0
        for idx in combinations(range(N), k):
            traces = set()
            for row in rows:
                t = 0
                for j, i in enumerate(idx):
                    t |= ((row >> i) & 1) << j
                traces.add(t)
                if len(traces) == 1 << k:
                    seen_shattered += 1
                    break
        counts.append(seen_shattered)
    counts += [0] * (5-len(counts))
    return counts


def main():
    levels = graph_types(5)
    assert [len(x) for x in levels] == [1, 1, 2, 5, 11, 26]
    expected_three = [(4, 2, 6), (4, 2, 2), (5, 1, 4)]
    for k in range(1, 6):
        accepted = []
        for e in levels[k]:
            v = vertices(e)
            statuses = [shattered(e, v + r) for r in (0, 1, 2)]
            assert statuses == sorted(statuses), (k, e, statuses)
            if any(statuses):
                r = statuses.index(True)
                accepted.append((v, r, isomorphisms(e, e, True), e))
        assert len(accepted) == {1:1,2:2,3:3,4:4,5:0}[k]
        if k == 3:
            assert sorted((v, r, aut) for v, r, aut, e in accepted) == sorted(expected_three)
        if k == 4:
            assert sorted((v, r, aut) for v, r, aut, e in accepted) == sorted([
                (5,2,24), (5,2,2), (5,2,2), (6,2,8)])
        if k == 5:
            assert len(accepted) == 0
        print('MOTIFS', k, 'total', len(levels[k]), 'shattered_types',
              [(v, r, aut, e) for v,r,aut,e in accepted], flush=True)
    for n in range(2, 13):
        counts = type_counts(levels, n)
        assert counts == predicted(n) + [0], (n,counts,predicted(n))
        if n <= 10:
            direct = exhaustive_direct(n)
            assert direct == predicted(n), (n,direct,predicted(n))
            print('DIRECT', n, direct, flush=True)
    print('ALL_OPEN_TRIANGULAR_GRAPH_CHECKS_PASS 26 five-edge motifs, 2..12 motif counts, 2..10 labelled graphs', flush=True)


if __name__ == '__main__':
    main()
