"""Exhaustive certificate for five-square robust-clique complexes.

Requires networkx==3.6.1. Run: python verify.py.
Every elementary face and Hasse incidence is explicitly checked.
"""
import collections
import itertools
import networkx as nx


def extensions(graph):
    n = graph.number_of_nodes()
    for u, v in graph.edges():
        h = graph.copy()
        h.add_edges_from(((u, n), (n, n + 1), (n + 1, v)))
        yield h
    for y in graph.nodes():
        for u, v in itertools.combinations(graph.neighbors(y), 2):
            if not graph.has_edge(u, v):
                h = graph.copy()
                h.add_edges_from(((u, n), (v, n)))
                yield h


def representatives(length=5):
    reps = [nx.cycle_graph(4)]
    counts = [1]
    for _ in range(2, length + 1):
        bins = collections.defaultdict(list)
        for g in reps:
            for h in extensions(g):
                key = nx.weisfeiler_lehman_graph_hash(h)
                if not any(nx.is_isomorphic(h, other) for other in bins[key]):
                    bins[key].append(h)
        reps = [graph for block in bins.values() for graph in block]
        counts.append(len(reps))
    return reps, counts


def complex_faces(g, k=5):
    n = g.number_of_nodes()
    adj = [0] * n
    for u, v in g.edges():
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    forbidden = []
    for group in itertools.combinations(range(n), k):
        if all(not (adj[u] & (1 << v)) for u, v in itertools.combinations(group, 2)):
            forbidden.append(sum(1 << v for v in group))
    # Graphs are bipartite, so every set of 2k-1 vertices has an
    # independent k-subset. Thus all faces have at most 2k-2 vertices.
    faces = {0}
    for size in range(1, min(n, 2 * k - 2) + 1):
        for group in itertools.combinations(range(n), size):
            mask = sum(1 << v for v in group)
            if not any((mask & bad) == bad for bad in forbidden):
                faces.add(mask)
    return faces


def certify(g):
    n = g.number_of_nodes()
    assert nx.is_bipartite(g)
    faces = complex_faces(g)
    remaining = set(faces)
    pairs = []
    # Successive vertex toggles give a full matching on the augmented
    # face poset. The empty-face match is omitted to retain one 0-cell.
    for v in range(n):
        bit = 1 << v
        eligible = [f for f in remaining if not f & bit and f | bit in remaining]
        for f in eligible:
            remaining.remove(f)
            remaining.remove(f | bit)
            pairs.append((f, f | bit))
    assert (0, 1) in pairs
    pairs.remove((0, 1))
    remaining.add(1)
    remaining.discard(0)
    nonempty = faces - {0}
    assert 2 * len(pairs) + len(remaining) == len(nonempty)
    assert len(set(f for p in pairs for f in p)) == 2 * len(pairs)
    assert all(f.bit_count() in (1, 8) for f in remaining)
    assert sum(f.bit_count() == 1 for f in remaining) == 1
    lower_to_upper = dict(pairs)

    # Reverse matched cover relations in the complete Hasse diagram,
    # then verify acyclicity by Kahn's topological sort.
    indegree = {f: 0 for f in nonempty}
    outgoing = {f: [] for f in nonempty}
    for upper in nonempty:
        bits = upper
        while bits:
            bit = bits & -bits
            bits ^= bit
            lower = upper ^ bit
            if not lower:
                continue
            if lower_to_upper.get(lower) == upper:
                source, target = lower, upper
            else:
                source, target = upper, lower
            outgoing[source].append(target)
            indegree[target] += 1
    queue = collections.deque(f for f in nonempty if indegree[f] == 0)
    visited = 0
    while queue:
        u = queue.popleft()
        visited += 1
        for v in outgoing[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    assert visited == len(nonempty), 'A cyclic matching would invalidate the proof'
    beta = sum(f.bit_count() == 8 for f in remaining)
    # Independent Euler-characteristic consistency check, including empty face.
    redchi = sum((-1) ** (f.bit_count() - 1) for f in faces)
    assert redchi == -beta
    return len(nonempty), len(pairs), beta


def main():
    reps, sequence_counts = representatives()
    assert sequence_counts == [1, 2, 7, 29, 179]
    assert len(reps) == 179
    totals = collections.Counter()
    all_faces = all_pairs = 0
    for g in reps:
        nfaces, npairs, beta = certify(g)
        totals[beta] += 1
        all_faces += nfaces
        all_pairs += npairs
    assert sorted(totals.items()) == [(0, 67), (1, 27), (2, 34), (3, 16), (4, 2), (5, 33)]
    assert (all_faces, all_pairs) == (255727, 127616)
    print('PASS: square sequence isomorphism types:', sequence_counts)
    print('PASS: all 179 complete face-poset Hasse digraphs are acyclic')
    print('PASS: every matching has one critical 0-cell and only critical 7-cells')
    print('PASS: multiplicities:', sorted(totals.items()))
    print('PASS: total nonempty faces:', all_faces, 'total matched pairs:', all_pairs)


if __name__ == '__main__':
    main()
