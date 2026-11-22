#!/usr/bin/env python3
"""Exhaustive, dependency-free certificate for radius-two Petersen edge faults.

All graph distances are recomputed after deletions. Vertex i denotes the
lexicographically i-th two-subset of {0,1,2,3,4}. The undirected graph has
an edge when the two pairs are disjoint.
"""
from itertools import combinations, permutations
from collections import Counter

V = tuple(combinations(range(5), 2))
ID = {v: i for i, v in enumerate(V)}
E = tuple((i, j) for i, j in combinations(range(10), 2)
          if set(V[i]).isdisjoint(V[j]))
assert len(V) == 10 and len(E) == 15

# (representative deleted-edge triple, S5 orbit cardinality,
#  preferred vertex order, number of critical two-simplices)
CASES = (
    (((0, 7), (0, 8), (0, 9)), 10, None, None),
    (((0, 7), (0, 8), (1, 5)), 120, (8, 7, 3, 5, 1, 2, 9, 4, 0, 6), 0),
    (((0, 7), (0, 8), (1, 9)), 60, (8, 0, 4, 7, 9, 3, 6, 1, 5, 2), 0),
    (((0, 7), (0, 8), (2, 6)), 60, (3, 2, 0, 9, 8, 7, 4, 6, 1, 5), 0),
    (((0, 7), (0, 8), (2, 8)), 60, (7, 1, 4, 6, 2, 9, 0, 8, 5, 3), 0),
    (((0, 7), (1, 5), (2, 4)), 5, (3, 5, 8, 7, 1, 4, 6, 2, 9, 0), 4),
    (((0, 7), (1, 5), (2, 6)), 60, (7, 3, 0, 8, 5, 4, 9, 6, 2, 1), 1),
    (((0, 7), (1, 6), (2, 8)), 60, (5, 3, 4, 6, 7, 9, 1, 0, 2, 8), 0),
    (((0, 7), (1, 6), (5, 8)), 20, (9, 1, 6, 4, 0, 7, 3, 2, 5, 8), 0),
)

def graph(faults):
    adj = [set() for _ in range(10)]
    removed = set(faults)
    for a, b in E:
        if (a, b) not in removed:
            adj[a].add(b)
            adj[b].add(a)
    return adj

def metric(adj):
    D = []
    for src in range(10):
        d = [100] * 10
        d[src] = 0
        queue = [src]
        for u in queue:
            for v in adj[u]:
                if d[v] == 100:
                    d[v] = d[u] + 1
                    queue.append(v)
        D.append(tuple(d))
    return tuple(D)

def faces_at_two(D):
    faces = {}
    for face in range(1, 1 << 10):
        members = [v for v in range(10) if (face >> v) & 1]
        if all(D[a][b] <= 2 for a, b in combinations(members, 2)):
            faces[face] = len(members)
    return faces

def ordered_matching(faces, priority):
    remaining = set(faces)
    pairs = []
    for v in priority:
        bit = 1 << v
        for low in sorted(remaining):
            up = low | bit
            if not (low & bit) and up in remaining:
                assert low in remaining
                remaining.remove(low)
                remaining.remove(up)
                pairs.append((low, up))
    return remaining, pairs

def verify_acyclic(faces, pairs):
    """Check reversed matched Hasse edges form a DAG, not merely ranks."""
    assert len({x for a, b in pairs for x in (a, b)}) == 2 * len(pairs)
    pairset = set(pairs)
    for low, up in pairs:
        assert low in faces and up in faces
        assert low & up == low and up.bit_count() == low.bit_count() + 1
    incoming = {f: 0 for f in faces}
    outgoing = {f: [] for f in faces}
    for upper in faces:
        for v in range(10):
            if upper & (1 << v):
                lower = upper ^ (1 << v)
                if lower in faces:
                    # Ordinary face-arrow downward; matched arrow upward.
                    src, dst = ((lower, upper) if (lower, upper) in pairset
                                else (upper, lower))
                    incoming[dst] += 1
                    outgoing[src].append(dst)
    todo = [f for f, d in incoming.items() if d == 0]
    count = 0
    while todo:
        f = todo.pop()
        count += 1
        for dst in outgoing[f]:
            incoming[dst] -= 1
            if incoming[dst] == 0:
                todo.append(dst)
    assert count == len(faces), (count, len(faces))
    return sum(map(len, outgoing.values()))

def gf2_betti(faces):
    """Independent rank calculation, checking the matching's prediction."""
    bysize = {k: sorted(f for f in faces if faces[f] == k) for k in range(1, 11)}
    ranks = {1: 0, 11: 0}
    for k in range(2, 11):
        idx = {f: i for i, f in enumerate(bysize[k-1])}
        pivots = {}
        for f in bysize[k]:
            col = 0
            for v in range(10):
                if f & (1 << v):
                    col ^= 1 << idx[f ^ (1 << v)]
            while col:
                p = col.bit_length() - 1
                if p in pivots:
                    col ^= pivots[p]
                else:
                    pivots[p] = col
                    break
        ranks[k] = len(pivots)
    betti = {k - 1: len(bysize[k]) - ranks[k] - ranks[k + 1]
             for k in range(1, 11)}
    betti[0] -= 1
    return {k: b for k, b in betti.items() if b}

def apply_perm(triple, pv):
    return tuple(sorted(tuple(sorted((pv[a], pv[b]))) for a, b in triple))

def main():
    automorphisms = []
    for p in permutations(range(5)):
        pv = tuple(ID[tuple(sorted((p[a], p[b])))] for a, b in V)
        assert set(apply_perm(E, pv)) == set(E)
        automorphisms.append(pv)
    assert len(set(automorphisms)) == 120
    alltriples = set(combinations(E, 3))
    covered = set()
    results = Counter()
    for rep, size, priority, count2 in CASES:
        assert tuple(sorted(rep)) == rep
        orbit = {apply_perm(rep, p) for p in automorphisms}
        assert len(orbit) == size
        assert not orbit & covered
        covered.update(orbit)
        D = metric(graph(rep))
        if count2 is None:
            assert all(any(100 in row for row in metric(graph(F))) for F in orbit)
            results['disconnected'] += size
            print('orbit', rep, 'size', size, 'disconnected')
            continue
        assert all(100 not in row for row in D)
        faces = faces_at_two(D)
        assert tuple(sorted(priority)) == tuple(range(10))
        critical, pairs = ordered_matching(faces, priority)
        covers = verify_acyclic(faces, pairs)
        crit = Counter(faces[f] for f in critical)
        assert crit == ({1: 1, 3: count2} if count2 else {1: 1})
        assert gf2_betti(faces) == ({2: count2} if count2 else {})
        results[count2] += size
        counts = [sum(1 for f in faces if faces[f] == k) for k in range(1, 11)]
        print('orbit', rep, 'size', size, 'facets-by-cardinality',
              tuple(x for x in counts if x), 'critical', dict(crit),
              'matched-pairs', len(pairs), 'Hasse-arrows', covers,
              'acyclic', True, 'mod2', gf2_betti(faces))
    assert covered == alltriples and len(covered) == 455
    # Independently exhaust all smaller fault patterns to establish the
    # sharp first topology-change threshold using a cone vertex.
    cone_counts = []
    for t in range(3):
        tested = 0
        for faults in combinations(E, t):
            D = metric(graph(faults))
            assert all(100 not in row for row in D)
            assert any(max(row) <= 2 for row in D), (t, faults)
            tested += 1
        cone_counts.append(tested)
    assert cone_counts == [1, 15, 105]
    assert results == {0: 380, 1: 60, 4: 5, 'disconnected': 10}
    print('SMALL FAULTS: t=0,1,2 cone certificates', cone_counts)
    print('THREE-FAULT RESULTS:', dict(results), '; 455/455 cases covered')
    print('PASS: exact orbit partition, graph distances, complete face posets,')
    print('      valid acyclic matchings, integral homotopy types,')
    print('      independent mod-2 checks and sharp threshold')

if __name__ == '__main__':
    main()
