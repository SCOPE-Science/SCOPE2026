#!/usr/bin/env python3
"""Reproduce finite homotopy certificate for the first forest complex of the Fano incidence graph."""
from collections import Counter, deque
from itertools import combinations


def graph():
    points = range(1, 8)
    lines = sorted({tuple(sorted((a, b, a ^ b))) for a in points for b in points if a < b})
    assert len(lines) == 7 and all(len(set(L)) == 3 for L in lines)
    adj = [0] * 14
    for j, line in enumerate(lines):
        for a in line:
            u, v = a - 1, j + 7
            adj[u] |= 1 << v
            adj[v] |= 1 << u
    assert all(x.bit_count() == 3 for x in adj)
    assert sum(x.bit_count() for x in adj) == 42
    return lines, adj


def build_faces(adj):
    forbidden = set()
    for center in range(14):
        neighbours = [v for v in range(14) if adj[center] & (1 << v)]
        for a, b in combinations(neighbours, 2):
            forbidden.add((1 << center) | (1 << a) | (1 << b))
    assert len(forbidden) == 42

    # Independent face predicates: induced vertex degrees versus prohibited triples.
    faces = set()
    for mask in range(1 << 14):
        by_degree = all((adj[u] & mask).bit_count() <= 1 for u in range(14) if mask & (1 << u))
        by_triples = all((mask & triple) != triple for triple in forbidden)
        assert by_degree == by_triples, ('face disagreement', mask)
        if by_degree:
            faces.add(mask)
    return faces, forbidden


def toggle_matching(faces, order):
    remaining = set(faces)
    remaining.discard(0)  # Ordinary CW matching: leave a vertex, not an augmented empty face.
    pairs = []
    for vertex in order:
        bit = 1 << vertex
        for lower in sorted(s for s in remaining if not (s & bit)):
            upper = lower | bit
            if lower in remaining and upper in remaining:
                pairs.append((lower, upper))
                remaining.remove(lower)
                remaining.remove(upper)
    return pairs, remaining


def verify_acyclic(faces, pairs):
    cells = faces - {0}
    matching = set(pairs)
    assert len(matching) == len(pairs)
    assert all(a and a in cells and b in cells and b.bit_count() == a.bit_count() + 1 and a & b == a for a, b in pairs)
    covered = [x for a, b in pairs for x in (a, b)]
    assert len(covered) == len(set(covered))
    incoming = {c: 0 for c in cells}
    outgoing = {c: [] for c in cells}
    incidences = 0
    for large in cells:
        bits = large
        while bits:
            bit = bits & -bits
            bits -= bit
            small = large ^ bit
            if not small:
                continue
            if (small, large) in matching:
                a, b = large, small
            else:
                a, b = small, large
            outgoing[a].append(b)
            incoming[b] += 1
            incidences += 1
    q = deque(x for x in cells if incoming[x] == 0)
    visited = 0
    while q:
        v = q.popleft()
        visited += 1
        for w in outgoing[v]:
            incoming[w] -= 1
            if incoming[w] == 0:
                q.append(w)
    assert visited == len(cells), ('cyclic matching', visited, len(cells))
    return incidences


def mod2_ranks(faces):
    levels = {}
    for s in faces - {0}:
        levels.setdefault(s.bit_count() - 1, []).append(s)
    for v in levels.values():
        v.sort()
    ranks = {}
    for dim in sorted(levels):
        if dim == 0:
            ranks[0] = 0
            continue
        index = {s: j for j, s in enumerate(levels[dim - 1])}
        echelon = {}
        for face in levels[dim]:
            bits = face
            column = 0
            while bits:
                bit = bits & -bits
                bits -= bit
                column ^= 1 << index[face ^ bit]
            while column:
                pivot = column.bit_length() - 1
                if pivot in echelon:
                    column ^= echelon[pivot]
                else:
                    echelon[pivot] = column
                    break
        ranks[dim] = len(echelon)
    betti = {d: len(levels[d]) - ranks[d] - ranks.get(d + 1, 0) for d in levels}
    betti[0] -= 1
    return ranks, {d: v for d, v in betti.items() if v}


def main():
    lines, adj = graph()
    faces, forbidden = build_faces(adj)
    assert len(faces) == 2257
    fv = dict(sorted(Counter(s.bit_count() - 1 for s in faces).items()))
    assert fv == {-1:1,0:14,1:91,2:322,3:651,4:728,5:392,6:58}
    facets = [s for s in faces if all((s | (1 << v)) not in faces for v in range(14) if not (s & (1 << v)))]
    assert Counter(x.bit_count() - 1 for x in facets) == {5:70, 6:58}
    output = []
    for name, order in [('ascending', range(14)), ('descending', range(13,-1,-1))]:
        pairs, critical = toggle_matching(faces, order)
        histogram = dict(sorted(Counter(s.bit_count() - 1 for s in critical).items()))
        assert len(pairs) == 1121 and histogram == {0:1, 5:13}
        incidences = verify_acyclic(faces, pairs)
        output.append((name, len(pairs), histogram, incidences))
    assert output[0][3] == output[1][3]
    ranks, betti = mod2_ranks(faces)
    assert betti == {5:13}
    reduced_euler = sum((1 if s.bit_count() % 2 else -1) for s in faces)
    assert reduced_euler == -13
    print('Fano incidence lines:', lines)
    print('Vertices: 14; edges: 21; forbidden induced three-vertex paths:', len(forbidden))
    print('Faces, including empty:', len(faces))
    print('Face dimensions and counts:', fv)
    print('Facet dimensions and counts:', dict(sorted(Counter(x.bit_count()-1 for x in facets).items())))
    for name, pairs_count, crit, incidences in output:
        print('Morse', name, ': pairs', pairs_count, 'critical', crit, 'Hasse incidences', incidences, 'acyclic PASS')
    print('Independent original mod-two boundary ranks:', dict(sorted(ranks.items())))
    print('Reduced mod-two Betti numbers:', betti)
    print('Reduced Euler characteristic:', reduced_euler)
    print('HEAWOOD_FIRST_FOREST_FANO_INCIDENCE_WEDGE13_S5_PASS')


if __name__ == '__main__':
    main()
