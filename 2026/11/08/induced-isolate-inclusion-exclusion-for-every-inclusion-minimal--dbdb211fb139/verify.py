"""Exact checks of the structural formula for inclusion-minimal strong total covers.

Run: python3 verify.py
The direct oracle enumerates all subsets of vertices and edges independently.
"""
from collections import Counter
from itertools import combinations, product
from random import Random


def direct(n, edges):
    edges = sorted({tuple(sorted(e)) for e in edges})
    m = len(edges)
    result = Counter()
    for vm in range(1 << n):
        U = {v for v in range(n) if vm >> v & 1}
        for em in range(1 << m):
            Y = {e for j, e in enumerate(edges) if em >> j & 1}
            def covers(U, Y):
                return (all(v in U or any(v in e for e in Y)
                            for v in range(n)) and
                        all(e in Y or e[0] in U or e[1] in U
                            for e in edges))
            if not covers(U, Y):
                continue
            if any(covers(U - {v}, Y) for v in U):
                continue
            if any(covers(U, Y - {e}) for e in Y):
                continue
            result[len(U) + len(Y)] += 1
    return +result


def receiver_enumeration(n, edges):
    edges = {tuple(sorted(e)) for e in edges}
    V = set(range(n))
    output = Counter()
    for m in range(1 << n):
        W = {v for v in V if m >> v & 1}
        U = V - W
        EW = {e for e in edges if set(e) <= W}
        isolated = {w for w in W if not any(w in e for e in EW)}
        domains = [sorted(u for u in U if tuple(sorted((w, u))) in edges)
                   for w in sorted(isolated)]
        if any(not d for d in domains):
            continue
        for choices in product(*domains):
            f = dict(zip(sorted(isolated), choices))
            if any(not any(
                    u in e and w in e and (w not in isolated or f[w] != u)
                    for e in edges for w in W)
                   for u in set(choices)):
                continue
            output[n - len(W) + len(EW) + len(isolated)] += 1
    return +output


def inclusion_exclusion(n, edges):
    adjacency = [set() for _ in range(n)]
    for a, b in edges:
        adjacency[a].add(b)
        adjacency[b].add(a)
    V = set(range(n))
    output = Counter()
    for mask in range(1 << n):
        W = {v for v in V if mask >> v & 1}
        U = V - W
        I = {v for v in W if not (adjacency[v] & W)}
        eW = sum(len(adjacency[w] & W) for w in W) // 2
        d = {w: len(adjacency[w] & U) for w in I}
        R = [u for u in U if 0 < len(adjacency[u] & W)
             and (adjacency[u] & W) <= I]
        c = 0
        for sm in range(1 << len(R)):
            used = set()
            admissible = True
            sign = 1
            for j, u in enumerate(R):
                if sm >> j & 1:
                    sign = -sign
                    neighbors = adjacency[u] & W
                    if used & neighbors:
                        admissible = False
                        break
                    used.update(neighbors)
            if admissible:
                count = 1
                for w in I - used:
                    count *= d[w]
                c += sign * count
        assert c >= 0, (n, edges, W, c)
        output[n - len(W) + eW + len(I)] += c
    return +output


def run():
    cases = 0
    for n in range(1, 5):
        pairs = list(combinations(range(n), 2))
        for mask in range(1 << len(pairs)):
            E = [e for j, e in enumerate(pairs) if mask >> j & 1]
            expected = direct(n, E)
            assert expected == receiver_enumeration(n, E), (n, E)
            assert expected == inclusion_exclusion(n, E), (n, E)
            cases += 1
    print('ALL_LABELLED_GRAPHS_N1_TO_N4_OK', cases)

    r = Random(20261104)
    additional = 0
    for n, draws in ((5, 24), (6, 12)):
        pairs = list(combinations(range(n), 2))
        examples = [[e for e in pairs if r.randrange(3) == 0]
                    for _ in range(draws)]
        examples.extend([pairs, [(i, i + 1) for i in range(n-1)]])
        for E in examples:
            expected = direct(n, E)
            assert expected == receiver_enumeration(n, E), (n, E)
            assert expected == inclusion_exclusion(n, E), (n, E)
            additional += 1
    print('ADDITIONAL_GRAPHS_N5_N6_OK', additional)
    for n, E in ((6, [(i, (i+1) % 6) for i in range(6)]),
                 (7, [(i, (i+1) % 7) for i in range(7)]),
                 (8, list(combinations(range(8), 2)))):
        print('FORMULA_COUNT', n, dict(sorted(inclusion_exclusion(n, E).items())))
    print('VERIFY_OK')

if __name__ == '__main__':
    run()
