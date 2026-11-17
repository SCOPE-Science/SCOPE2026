#!/usr/bin/env python3
"""Exact finite subgroup-chain orbit and elementary-collapse certificate.

Run: python3 verify.py [certificate.json]
Standard library only; every group operation and every collapse is checked.
"""
import itertools
import json
import sys
from collections import Counter, defaultdict


def analyze(n, even):
    perms = list(itertools.permutations(range(n)))
    if even:
        perms = [p for p in perms if sum(p[i] > p[j] for i in range(n)
                                            for j in range(i + 1, n)) % 2 == 0]
    ind = {p: i for i, p in enumerate(perms)}
    m = len(perms)
    e = ind[tuple(range(n))]
    mul = [[ind[tuple(x[y[i]] for i in range(n))] for y in perms] for x in perms]
    inv = [next(j for j in range(m) if mul[i][j] == e) for i in range(m)]

    def generated(H, g):
        known = set(H)
        queue = list(H)
        if g not in known:
            queue.append(g)
            known.add(g)
        k = 0
        while k < len(queue):
            a = queue[k]
            for b in tuple(queue):
                c = mul[a][b]
                if c not in known:
                    known.add(c)
                    queue.append(c)
            k += 1
        return frozenset(known)

    groups = [frozenset((e,))]
    seen = set(groups)
    for H in groups:
        for g in range(m):
            if g not in H:
                K = generated(H, g)
                if K not in seen:
                    groups.append(K)
                    seen.add(K)
    # Independently validate closure and inversion of each enumerated subgroup.
    for H in groups:
        assert e in H
        assert all(inv[a] in H for a in H)
        assert all(mul[a][b] in H for a in H for b in H)
    proper = [H for H in groups if 1 < len(H) < m]
    loc = {H: i for i, H in enumerate(proper)}
    conjugates = [[loc[frozenset(mul[mul[g][h]][inv[g]] for h in K)]
                   for g in range(m)] for K in proper]

    def canon(flag):
        return min(tuple(conjugates[v][g] for v in flag) for g in range(m))

    sup = [[j for j, K in enumerate(proper) if h < K]
           for h in proper]
    flags = []
    for d in range(n):
        if d == 0:
            fs = {canon((i,)) for i in range(len(proper))}
        else:
            fs = {canon(f + (j,)) for f in flags[-1] for j in sup[f[-1]]}
        if not fs:
            break
        flags.append(sorted(fs))
    indices = [{f: i for i, f in enumerate(level)} for level in flags]
    faces = [[]]
    for d in range(1, len(flags)):
        faces.append([tuple(indices[d-1][canon(f[:i] + f[i+1:])]
                            for i in range(len(f))) for f in flags[d]])
        assert all(len(set(row)) == d + 1 for row in faces[d])
        # Face boundaries of an oriented chain have square zero, over Z.
        if d >= 2:
            for row in faces[d]:
                signed = Counter()
                for i, u in enumerate(row):
                    for j, v in enumerate(faces[d-1][u]):
                        signed[v] += (-1) ** (i + j)
                assert all(k == 0 for k in signed.values())

    active = [set(range(len(level))) for level in flags]
    pairs = []
    while True:
        choice = None
        for d in range(len(flags)-1, 0, -1):
            cofaces = defaultdict(list)
            for high in sorted(active[d]):
                for low in faces[d][high]:
                    assert low in active[d-1]
                    cofaces[low].append(high)
            for low in sorted(cofaces):
                highs = cofaces[low]
                if (len(highs) == 1 and (d+1 == len(flags) or
                        all(highs[0] not in faces[d+1][upper] for upper in active[d+1]))):
                    choice = (d, low, highs[0])
                    break
            if choice:
                break
        if choice is None:
            break
        d, low, high = choice
        assert low in active[d-1] and high in active[d]
        assert sum(low in faces[d][v] for v in active[d]) == 1
        assert d+1 == len(flags) or all(high not in faces[d+1][v]
                                            for v in active[d+1])
        active[d-1].remove(low)
        active[d].remove(high)
        pairs.append([d, low, high])
    # Check face closure of terminal complex.
    for d in range(1, len(flags)):
        assert all(all(v in active[d-1] for v in faces[d][u]) for u in active[d])

    verts = lambda f: tuple(indices[0][canon((v,))] for v in f)
    edges = {j: tuple(sorted(verts(flags[1][j]))) for j in active[1]}
    assert all(len(set(v)) == 2 for v in edges.values())
    assert len(set(edges.values())) == len(edges), 'Repeated edges after collapse'
    assert len(active[-1]) == 0 or len(flags) <= 3

    if even:
        assert len(groups) == 59
        assert [len(x) for x in flags] == [7, 8, 1]
        assert len(pairs) == 3
        assert [len(x) for x in active] == [5, 5, 0]
        degree = Counter(v for a,b in edges.values() for v in (a,b))
        assert set(degree.values()) == {2} and len(degree) == len(active[0])
        # A four-cycle, hence S1.
        adj = defaultdict(set)
        for a,b in edges.values():
            adj[a].add(b); adj[b].add(a)
        visit = {next(iter(active[0]))}
        for _ in range(5):
            visit.update(w for v in tuple(visit) for w in adj[v])
        assert visit == active[0]
        conclusion = 'circle'
    else:
        assert len(groups) == 156
        assert [len(x) for x in flags] == [17, 49, 41, 7]
        assert len(pairs) == 26
        assert [len(x) for x in active] == [12, 30, 20, 0]
        assert all(len(set(verts(flags[2][j]))) == 3 for j in active[2])
        triangles = {tuple(sorted(verts(flags[2][j]))) for j in active[2]}
        assert len(triangles) == len(active[2]), 'Repeated triangles'
        # Every edge belongs to two triangles, each vertex has one circular link.
        edge_by_pair = {pair: k for k, pair in edges.items()}
        incidence = Counter()
        links = defaultdict(list)
        for tri in triangles:
            a,b,c = tri
            for edge in ((a,b),(a,c),(b,c)):
                incidence[edge_by_pair[edge]] += 1
            for v in tri:
                other = tuple(x for x in tri if x != v)
                links[v].append(other)
        assert set(incidence) == active[1]
        assert set(incidence.values()) == {2}
        assert set(links) == active[0]
        for v, link_edges in links.items():
            adj = defaultdict(set)
            for a,b in link_edges:
                adj[a].add(b)
                adj[b].add(a)
            assert len(adj) >= 3
            assert all(len(x) == 2 for x in adj.values())
            reachable = {next(iter(adj))}
            while True:
                nxt = reachable | {w for u in reachable for w in adj[u]}
                if reachable == nxt:
                    break
                reachable = nxt
            assert len(reachable) == len(adj), f'Disconnected link at {v}'
        # Connectedness of two-dimensional terminal complex.
        adj = defaultdict(set)
        for a,b in edges.values():
            adj[a].add(b); adj[b].add(a)
        reached = {next(iter(active[0]))}
        while True:
            nxt = reached | {w for u in reached for w in adj[u]}
            if reached == nxt:
                break
            reached = nxt
        assert reached == active[0]
        assert len(active[0]) - len(active[1]) + len(active[2]) == 2
        conclusion = 'sphere'

    return {
        'group': 'A5' if even else 'S5',
        'order': m,
        'subgroup_count_including_endpoints': len(groups),
        'subgroup_order_histogram': {str(j): sum(len(K) == j for K in groups)
                                     for j in sorted(set(map(len, groups)))},
        'quotient_cell_counts': list(map(len, flags)),
        'collapse_pairs': pairs,
        'remaining_cell_counts': [len(x) for x in active],
        'remaining_cells': [sorted(x) for x in active],
        'homotopy_type': conclusion
    }


def main():
    a = analyze(5, True)
    s = analyze(5, False)
    result = {'schema_version': 1, 'method': 'full subgroup enumeration and chain-orbit collapse checks',
              'cases': [a,s]}
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r', encoding='utf8') as handle:
            expected = json.load(handle)
        assert expected == result, 'The supplied certificate differs from exact recomputation'
    print('VERIFY_OK')
    for entry in result['cases']:
        print(entry['group'], entry['subgroup_count_including_endpoints'],
              entry['quotient_cell_counts'], len(entry['collapse_pairs']),
              entry['remaining_cell_counts'], entry['homotopy_type'])
    return result


if __name__ == '__main__':
    main()
