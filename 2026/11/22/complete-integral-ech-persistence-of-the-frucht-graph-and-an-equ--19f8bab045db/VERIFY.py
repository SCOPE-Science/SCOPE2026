#!/usr/bin/env python3
"""Reproduce the integral Frucht-graph intrinsic Cech persistence computation.
Standard-library Python 3 only; execute: python3 VERIFY.py
"""
import json
from collections import Counter, defaultdict, deque
from functools import lru_cache
import heapq

N = 12
EDGES = [(0,1),(0,6),(0,7),(1,2),(1,7),(2,3),(2,8),(3,4),(3,9),
         (4,5),(4,9),(5,6),(5,10),(6,10),(7,11),(8,9),(8,11),(10,11)]

def vertices(mask):
    return [i for i in range(N) if mask & (1 << i)]

def signed_boundary(mask):
    return [(mask ^ (1 << v), (-1 if j % 2 else 1))
            for j, v in enumerate(vertices(mask))]

def boundary_of_chain(chain):
    out = defaultdict(int)
    for simplex, coef in chain.items():
        for face, sign in signed_boundary(simplex):
            if face: out[face] += coef * sign
    return {x: v for x, v in out.items() if v}

def graph_distances():
    graph = [set() for _ in range(N)]
    assert len(EDGES) == 18 and len(set(tuple(sorted(e)) for e in EDGES)) == 18
    for u, v in EDGES:
        graph[u].add(v); graph[v].add(u)
    assert all(len(neighbors) == 3 for neighbors in graph)
    bfs = []
    for source in range(N):
        ds = [-1] * N; ds[source] = 0
        q = deque([source])
        while q:
            v = q.popleft()
            for w in graph[v]:
                if ds[w] == -1:
                    ds[w] = ds[v] + 1; q.append(w)
        assert -1 not in ds
        bfs.append(ds)
    floyd = [[0 if u == v else (1 if v in graph[u] else 999)
              for v in range(N)] for u in range(N)]
    for k in range(N):
        for u in range(N):
            for v in range(N):
                floyd[u][v] = min(floyd[u][v], floyd[u][k] + floyd[k][v])
    assert bfs == floyd and max(max(row) for row in bfs) == 4
    return bfs

def all_faces(dist, radius):
    k = radius // 2
    if radius % 2:
        witnesses = {sum(1 << v for v in range(N)
                         if min(dist[u][v], dist[w][v]) <= k)
                     for u, w in EDGES}
    else:
        witnesses = {sum(1 << v for v in range(N) if dist[u][v] <= k)
                     for u in range(N)}
    # Subface enumeration and independent test of all 4095 nonempty vertex subsets.
    by_subfaces = set()
    for mask in witnesses:
        sub = mask
        while sub:
            by_subfaces.add(sub)
            sub = (sub - 1) & mask
    by_membership = {mask for mask in range(1, 1 << N)
                     if any((mask & witness) == mask for witness in witnesses)}
    assert by_subfaces == by_membership
    return by_membership

def morse_match(faces):
    remaining = set(faces)
    pairs = {}
    for vertex in range(N - 1, -1, -1):
        bit = 1 << vertex
        for low in sorted(x for x in remaining if not (x & bit) and (x | bit) in remaining):
            high = low | bit
            if low in remaining and high in remaining:
                remaining.remove(low); remaining.remove(high)
                pairs[low] = high
    assert len(faces) == 2 * len(pairs) + len(remaining)
    return pairs, remaining

def topological_order(faces, pairs):
    outgoing = {face: [] for face in faces}
    indegree = {face: 0 for face in faces}
    incidences = 0
    for high in faces:
        for low, _ in signed_boundary(high):
            if not low: continue
            if pairs.get(low) == high:
                source, dest = low, high
            else:
                source, dest = high, low
            outgoing[source].append(dest)
            indegree[dest] += 1
            incidences += 1
    heap = [x for x in faces if indegree[x] == 0]
    heapq.heapify(heap)
    ordered = []
    while heap:
        x = heapq.heappop(heap)
        ordered.append(x)
        for y in outgoing[x]:
            indegree[y] -= 1
            if indegree[y] == 0: heapq.heappush(heap, y)
    assert len(ordered) == len(faces), 'Acyclicity failure'
    return {face: i for i, face in enumerate(ordered)}, incidences

def morse_projection(pairs, critical):
    matched_upper = {high: low for low, high in pairs.items()}
    @lru_cache(None)
    def project(face):
        if face in critical: return {face: 1}
        if face in matched_upper: return {}
        assert face in pairs
        high = pairs[face]
        pivot = dict(signed_boundary(high))[face]
        out = defaultdict(int)
        for low, sign in signed_boundary(high):
            if low == face: continue
            for target, coef in project(low).items():
                out[target] -= pivot * sign * coef
        return {x: v for x, v in out.items() if v}
    return project

def lift_critical_cycle(face, pairs, topo, project):
    # Unit-incidence elementary expansions of the critical-cell generator.
    chain = {face: 1}
    for _ in range(10000):
        bd = boundary_of_chain(chain)
        if not bd:
            assert project_chain(chain, project) == {face: 1}
            return chain
        low = min(bd, key=lambda x: topo[x])
        assert low in pairs, ('Failed to lift cycle', face, low)
        high = pairs[low]
        assert high.bit_count() == face.bit_count()
        pivot = dict(signed_boundary(high))[low]
        chain[high] = chain.get(high, 0) - bd[low] * pivot
        if not chain[high]: del chain[high]
    raise AssertionError('Lift did not terminate')

def project_chain(chain, project):
    out = defaultdict(int)
    for simplex, coef in chain.items():
        for critical, value in project(simplex).items():
            out[critical] += coef * value
    return {x: v for x, v in out.items() if v}

def find_bounding_chain(cycle, target_pairs, target_topo):
    # Exact signed unit pivots; returns a checkable chain, not only a homology rank.
    residual = dict(cycle)
    bound = defaultdict(int)
    for _ in range(10000):
        if not residual:
            bound = {x: value for x, value in bound.items() if value}
            assert boundary_of_chain(bound) == cycle
            return bound
        low = min(residual, key=lambda x: target_topo[x])
        assert low in target_pairs, ('Residual contains unpaired cell', low)
        high = target_pairs[low]
        pivot = dict(signed_boundary(high))[low]
        coefficient = residual[low] * pivot
        bound[high] += coefficient
        for x, sign in signed_boundary(high):
            if x:
                residual[x] = residual.get(x, 0) - coefficient * sign
                if not residual[x]: del residual[x]
    raise AssertionError('Bounding reduction did not terminate')

def mod2_simplicial_betti(faces):
    # Completely separate boundary-matrix elimination on the original simplicial complex.
    cells = defaultdict(list)
    for face in faces:
        cells[face.bit_count() - 1].append(face)
    ranks = {0: 0}
    for dimension in range(1, max(cells) + 1):
        index = {face: i for i, face in enumerate(sorted(cells[dimension - 1]))}
        pivots = {}
        for upper in cells[dimension]:
            column = 0
            for lower, _ in signed_boundary(upper):
                column ^= 1 << index[lower]
            while column:
                top = column.bit_length() - 1
                if top not in pivots:
                    pivots[top] = column
                    break
                column ^= pivots[top]
        ranks[dimension] = len(pivots)
    return {dim: len(cells[dim]) - ranks.get(dim, 0) - ranks.get(dim + 1, 0)
            for dim in sorted(cells)}

def main():
    distances = graph_distances()
    expected_faces = (12, 30, 109, 423, 2084, 4095)
    expected_critical = (
        {0: 12}, {0: 1, 1: 7}, {0: 1, 1: 3, 2: 1},
        {0: 1, 2: 2, 3: 2}, {0: 1, 3: 2, 4: 1})
    stages = {}
    report = {'graph_order': 12, 'graph_edges': 18, 'graph_diameter': 4,
              'faces_including_empty': [n+1 for n in expected_faces],
              'stages': {}, 'maps': {}}
    for r in range(6):
        faces = all_faces(distances, r)
        assert len(faces) == expected_faces[r]
        if r == 5:
            assert (1 << N) - 1 in faces
            continue
        pairs, critical = morse_match(faces)
        topo, incidences = topological_order(faces, pairs)
        projected = morse_projection(pairs, critical)
        critical_by_dim = dict(sorted(Counter(x.bit_count()-1 for x in critical).items()))
        assert critical_by_dim == expected_critical[r]
        # The reduced integral Morse boundary is identically zero.
        boundary_entries = 0
        for face in critical:
            if face.bit_count() <= 1: continue
            out = defaultdict(int)
            for low, sign in signed_boundary(face):
                if low:
                    for target, value in projected(low).items():
                        out[target] += sign * value
            boundary_entries += sum(value != 0 for value in out.values())
        assert boundary_entries == 0
        raw_betti = mod2_simplicial_betti(faces)
        assert {dim: count for dim, count in raw_betti.items() if count} == expected_critical[r]
        stages[r] = (faces, pairs, critical, topo, projected)
        report['stages'][str(r)] = {
            'nonempty_faces': len(faces), 'paired_faces': 2*len(pairs),
            'critical_by_dimension': critical_by_dim,
            'Hasse_incidences_checked': incidences,
            'independent_mod2_Betti': raw_betti,
            'integral_Morse_boundary_nonzero_entries': boundary_entries}
    assert all(stages[r][0] <= stages[r+1][0] for r in range(4))

    # Inclusion on first homology r=1 -> 2 in the integral Morse critical-cell bases.
    old, new = stages[1], stages[2]
    src = sorted(x for x in old[2] if x.bit_count() == 2)
    dst = sorted(x for x in new[2] if x.bit_count() == 2)
    matrix_columns = []
    for source in src:
        cycle = lift_critical_cycle(source, old[1], old[3], old[4])
        coefficients = project_chain(cycle, new[4])
        matrix_columns.append([coefficients.get(target, 0) for target in dst])
    assert matrix_columns == [[0,0,0],[1,0,0],[0,0,0],[0,0,0],
                              [0,-1,0],[0,0,1],[0,0,0]]
    # Three unit pivots produce a split integral surjection (kernel rank four).
    report['maps']['H1_1_to_2'] = {'matrix_by_source_columns': matrix_columns,
                                   'integral_rank': 3, 'unit_minor': 1}

    # The radius-two 2-cycle is explicitly the boundary of three tetrahedra at scale 3.
    old, new = stages[2], stages[3]
    src = sorted(x for x in old[2] if x.bit_count() == 3)
    assert len(src) == 1
    cycle = lift_critical_cycle(src[0], old[1], old[3], old[4])
    assert not project_chain(cycle, new[4])
    bound = find_bounding_chain(cycle, new[1], new[3])
    assert len(bound) == 3 and all(x.bit_count() == 4 for x in bound)
    report['maps']['H2_2_to_3'] = {
        'matrix_by_source_columns': [[0,0]],
        'source_critical_mask': src[0],
        'bounding_3_chain': [[vertices(x), coef] for x, coef in sorted(bound.items())]}

    # Both independent degree-three generators born at 3 are 4-simplex boundaries at 4.
    old, new = stages[3], stages[4]
    src = sorted(x for x in old[2] if x.bit_count() == 4)
    dst = sorted(x for x in new[2] if x.bit_count() == 4)
    assert len(src) == len(dst) == 2
    bounding_chains = []
    for source in src:
        cycle = lift_critical_cycle(source, old[1], old[3], old[4])
        assert all(coef == 0 for coef in project_chain(cycle, new[4]).values())
        bound = find_bounding_chain(cycle, new[1], new[3])
        assert len(bound) == 1 and next(iter(bound)).bit_count() == 5
        bounding_chains.append({'source_mask': source,
                                'target_4_chain': [[vertices(x), coef]
                                                   for x, coef in sorted(bound.items())]})
    report['maps']['H3_3_to_4'] = {
        'matrix_by_source_columns': [[0,0],[0,0]],
        'explicit_boundary_witnesses': bounding_chains}
    report['integral_reduced_barcodes'] = {
        'H0': [[0,1,11]],
        'H1': [[1,2,4],[1,3,3]],
        'H2': [[2,3,1],[3,4,2]],
        'H3': [[3,4,2],[4,5,2]],
        'H4': [[4,5,1]]}
    report['marker'] = 'FRUCHT_GRAPH_CECH_INTEGRAL_PERSISTENCE_VERIFIED'
    print(json.dumps(report, ensure_ascii=False, sort_keys=True, separators=(',',':')))

if __name__ == '__main__': main()
