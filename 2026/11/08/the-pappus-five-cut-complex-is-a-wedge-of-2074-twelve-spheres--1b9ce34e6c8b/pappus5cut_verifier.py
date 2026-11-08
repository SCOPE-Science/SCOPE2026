#!/usr/bin/env python3
"""Exact finite verification of the ordinary five-cut complex of the Pappus graph.

Run with Python 3 (stdlib only): python3 pappus5cut_verifier.py
No external datasets, packages, or prior computations are required.
"""
from collections import Counter, deque
from math import comb

N = 18
FULL = (1 << N) - 1
OFFSETS = (5, 7, -7, 7, -7, -5) * 3
EDGES = sorted({tuple(sorted((i, (i+1)%N))) for i in range(N)} |
               {tuple(sorted((i, (i+OFFSETS[i])%N))) for i in range(N)})
assert len(EDGES) == 27
ADJ = [0] * N
for a,b in EDGES:
    ADJ[a] |= 1 << b
    ADJ[b] |= 1 << a
assert [a.bit_count() for a in ADJ] == [3]*N


def girth():
    shortest = N+1
    for root in range(N):
        dist = [-1]*N
        parent = [-1]*N
        dist[root] = 0
        q = deque([root])
        while q:
            i = q.popleft()
            for j in range(N):
                if not (ADJ[i] >> j & 1): continue
                if dist[j] == -1:
                    dist[j] = dist[i]+1; parent[j] = i; q.append(j)
                elif parent[i] != j:
                    shortest = min(shortest, dist[i]+dist[j]+1)
    return shortest

assert girth() == 6


def connected(mask):
    """Connectivity of the graph induced by a nonempty vertex mask."""
    assert mask != 0
    seen = mask & -mask
    while True:
        front = seen
        neighbors = 0
        while front:
            bit = front & -front
            front -= bit
            neighbors |= ADJ[bit.bit_length()-1]
        updated = seen | (neighbors & mask)
        if updated == seen:
            return seen == mask
        seen = updated


def is_six_cycle(mask):
    if mask.bit_count() != 6: return False
    if not connected(mask): return False
    return all((ADJ[i] & mask).bit_count() == 2
               for i in range(N) if mask >> i & 1)


def main():
    disconnected5 = []
    connected5 = []
    cycles6 = []
    for mask in range(1 << N):
        c = mask.bit_count()
        if c == 5:
            (connected5 if connected(mask) else disconnected5).append(mask)
        if c == 6 and is_six_cycle(mask):
            cycles6.append(mask)
    assert len(connected5) == 324 and len(disconnected5) == 8244
    assert len(cycles6) == 18
    facets = [FULL ^ m for m in disconnected5]
    assert len(set(facets)) == 8244

    # First enumeration: down-closure of maximal faces.
    # Enumerate the full face set by breadth-first downclosure.
    face = bytearray(1 << N)
    face[0] = 1
    todo = deque()
    for f in facets:
        if not face[f]:
            face[f] = 1; todo.append(f)
    while todo:
        parent = todo.popleft()
        bits = parent
        while bits:
            bit = bits & -bits; bits -= bit
            child = parent ^ bit
            if not face[child]:
                face[child] = 1; todo.append(child)

    # Second enumeration: upward Boolean zeta transform of disconnected five-sets.
    has_bad5 = bytearray(1 << N)
    for m in disconnected5: has_bad5[m] = 1
    for i in range(N):
        bit = 1 << i
        for m in range(1 << N):
            if m & bit and has_bad5[m ^ bit]: has_bad5[m] = 1
    assert all(bool(face[m]) == bool(has_bad5[FULL ^ m])
               for m in range(1 << N))

    f = Counter(m.bit_count()-1 for m in range(1 << N) if face[m])
    assert sum(f.values()) == 257754
    assert f[12] == 8244 and f[11] == 18546 and f[10] == comb(18,11)
    assert sum((1 if d%2==0 else -1)*v for d,v in f.items()) == 2074
    missing_complements = {m for m in range(1 << N)
                           if m.bit_count() == 6 and not face[FULL ^ m]}
    assert missing_complements == set(cycles6)

    # Stage-by-stage toggling with the vertices in increasing order; all faces
    # are first matched in the augmented face poset, including the empty face.
    available = face[:]
    mate = [-1] * (1 << N)
    pair_count = 0
    for i in range(N):
        bit = 1 << i
        for lo in range(1 << N):
            if not (lo & bit) and available[lo] and available[lo | bit]:
                hi = lo | bit
                available[lo] = available[hi] = 0
                mate[lo] = hi
                mate[hi] = lo
                pair_count += 1
    assert pair_count == 127840
    assert mate[0] == 1 and mate[1] == 0
    assert all((mate[m] == -1 or mate[mate[m]] == m)
               for m in range(1 << N))
    # Remove empty face and its pair, leaving one ordinary critical vertex.
    mate[0] = mate[1] = -1
    critical = Counter(m.bit_count()-1 for m in range(1, 1 << N)
                       if face[m] and mate[m] == -1)
    assert critical == {0: 1, 12: 2074}, critical

    # Exhaustively verify acyclicity of the directed Hasse graph:
    # each unmatched incidence upper -> lower, each matched incidence lower -> upper.
    indeg = [0]*(1 << N)
    hasse = 0
    for lower in range(1, 1 << N):
        if not face[lower]: continue
        missing = FULL ^ lower
        while missing:
            bit = missing & -missing; missing -= bit
            higher = lower | bit
            if face[higher]:
                hasse += 1
                if mate[lower] == higher: indeg[higher] += 1
                else: indeg[lower] += 1
    queued = deque(m for m in range(1, 1 << N) if face[m] and indeg[m] == 0)
    processed = 0
    while queued:
        current = queued.popleft()
        processed += 1
        # Matched up-edge, when this face is lower.
        partner = mate[current]
        if partner > current:
            indeg[partner] -= 1
            if indeg[partner] == 0: queued.append(partner)
        # Unmatched down-edges to codimension-one faces, excluding empty.
        bits = current
        while bits:
            bit = bits & -bits; bits -= bit
            smaller = current ^ bit
            if smaller and mate[current] != smaller:
                indeg[smaller] -= 1
                if indeg[smaller] == 0: queued.append(smaller)
    assert processed == sum(face)-1, (processed, sum(face)-1)
    assert all(indeg[m] == 0 for m in range(1, 1 << N) if face[m])
    assert 2074 == comb(17,4)-len(connected5)+len(cycles6)
    print('GRAPH_VERTICES', N)
    print('GRAPH_EDGES', len(EDGES))
    print('GRAPH_GIRTH', girth())
    print('CONNECTED_FIVE_SETS', len(connected5))
    print('DISCONNECTED_FIVE_SETS', len(disconnected5))
    print('INDUCED_SIX_CYCLES', len(cycles6))
    print('FACE_COUNTS_BY_DIMENSION', sorted(f.items()))
    print('ALL_SUBSETS_CROSS_CHECKED', 1 << N)
    print('MISSED_12_VERTEX_FACES', len(missing_complements))
    print('AUGMENTED_MORSE_PAIRS', pair_count)
    print('ORDINARY_CRITICAL_CELLS', sorted(critical.items()))
    print('HASSE_INCIDENCES_CHECKED', hasse)
    print('DIRECTED_HASSE_VERTICES_PROCESSED', processed)
    print('ACYCLIC', True)
    print('EULER_CORRECTION', comb(17,4), '-', len(connected5), '+', len(cycles6), '=', 2074)
    print('PAPPUS_FIVE_CUT_VERIFIED')

if __name__ == '__main__': main()
