#!/usr/bin/env python3
"""Exact finite verification of minimal torsion for bidirected multipath complexes.
Standard-library only. Enumerates all unlabelled undirected graphs on at most five vertices.
Acyclic face-poset matchings and integer-unimodular row reductions certify torsion.
"""
import itertools
from collections import Counter, defaultdict, deque
from functools import lru_cache
from math import gcd


def graph_classes(n):
    edges = list(itertools.combinations(range(n), 2))
    locations = {edge: j for j, edge in enumerate(edges)}
    relabels = [tuple(locations[tuple(sorted((perm[u], perm[v])))] for u, v in edges)
                for perm in itertools.permutations(range(n))]
    seen = set()
    for mask in range(1 << len(edges)):
        if mask in seen:
            continue
        orbit = {sum(1 << relabel[j] for j in range(len(edges)) if (mask >> j) & 1)
                 for relabel in relabels}
        seen.update(orbit)
        yield mask, [e for j, e in enumerate(edges) if (mask >> j) & 1], len(orbit)
    assert len(seen) == 1 << len(edges)


def multipath_faces(n, undirected_edges):
    arcs = sorted((a, b) for u, v in undirected_edges for a, b in ((u, v), (v, u)))
    successors = [-1] * n
    predecessors = [-1] * n
    faces = [0]
    def rec(i, mask):
        if i == len(arcs):
            return
        u, v = arcs[i]
        rec(i + 1, mask)
        if successors[u] >= 0 or predecessors[v] >= 0:
            return
        w = v
        while successors[w] >= 0 and w != u:
            w = successors[w]
        if w == u:
            return
        successors[u], predecessors[v] = v, u
        faces.append(mask | (1 << i))
        rec(i + 1, mask | (1 << i))
        successors[u], predecessors[v] = -1, -1
    rec(0, 0)
    return arcs, faces


def direct_face_test(arcs, mask, n):
    successors = [-1] * n
    pred = [-1] * n
    for j, (u, v) in enumerate(arcs):
        if not (mask >> j) & 1:
            continue
        if successors[u] != -1 or pred[v] != -1:
            return False
        successors[u], pred[v] = v, u
    for u in range(n):
        seen = set()
        v = u
        while v != -1:
            if v in seen:
                return False
            seen.add(v)
            v = successors[v]
    return True


def matching(faces, size, descending=False):
    remaining = set(faces)
    pairs = []
    indices = range(size-1, -1, -1) if descending else range(size)
    for j in indices:
        bit = 1 << j
        for face in list(remaining):
            if not face & bit and face | bit in remaining:
                remaining.remove(face)
                remaining.remove(face | bit)
                pairs.append((face, face | bit))
    return pairs, remaining


def acyclicity(faces, pairs):
    # Incidence f -> f minus one vertex, reversed on matched face-pairs.
    indices = {f: i for i, f in enumerate(faces)}
    is_matched = set(pairs)
    adj = [[] for _ in faces]
    indeg = [0] * len(faces)
    h = 0
    for upper in faces:
        bits = upper
        while bits:
            bit = bits & -bits
            lower = upper ^ bit
            tail, head = (lower, upper) if (lower, upper) in is_matched else (upper, lower)
            adj[indices[tail]].append(indices[head])
            indeg[indices[head]] += 1
            h += 1
            bits -= bit
    q = deque(k for k, degree in enumerate(indeg) if degree == 0)
    count = 0
    while q:
        x = q.popleft()
        count += 1
        for y in adj[x]:
            indeg[y] -= 1
            if indeg[y] == 0:
                q.append(y)
    assert count == len(faces), (len(faces), count)
    return h


def graded_critical_and_boundaries(crit, pairs):
    upper_of = dict(pairs)
    graded = {k: sorted(x for x in crit if x.bit_count() - 1 == k)
              for k in set(x.bit_count() - 1 for x in crit)}

    @lru_cache(None)
    def reduce(lower):
        if lower in crit:
            return {lower: 1}
        if lower not in upper_of:
            return {}
        upper = upper_of[lower]
        marked_bit = upper ^ lower
        eps = (-1) ** ((upper & (marked_bit - 1)).bit_count())
        result = defaultdict(int)
        bits = upper
        while bits:
            bit = bits & -bits
            bits -= bit
            if bit == marked_bit:
                continue
            sgn = (-1) ** ((upper & (bit - 1)).bit_count())
            for generator, coeff in reduce(upper ^ bit).items():
                result[generator] -= eps * sgn * coeff
        return {x: y for x, y in result.items() if y}

    def bd(face):
        result = defaultdict(int)
        bits = face
        while bits:
            bit = bits & -bits
            bits -= bit
            sign = (-1) ** ((face & (bit - 1)).bit_count())
            for generator, coeff in reduce(face ^ bit).items():
                result[generator] += sign * coeff
        return {x: y for x, y in result.items() if y}

    maps = {k: [bd(x) for x in graded[k]] for k in graded if k > 0}
    return graded, maps


def eliminate_unit_entries(columns, rows):
    # All operations are integral elementary unimodular row/column operations.
    # Every removed unit pivot is exactly one SNF invariant equal to 1.
    dense = {row: {j: val for j, col in enumerate(columns)
                   if (val := col.get(row, 0)) != 0} for row in rows}
    pivots = 0
    while True:
        pivot = next(((row, j, val) for row, entries in dense.items()
                      for j, val in entries.items() if abs(val) == 1), None)
        if pivot is None:
            break
        row, col, unit = pivot
        pivotrow = dense.pop(row)
        for current in dense.values():
            if col in current:
                mul = current[col] * unit
                for j, value in pivotrow.items():
                    v = current.get(j, 0) - mul * value
                    if v:
                        current[j] = v
                    else:
                        current.pop(j, None)
        for current in dense.values():
            current.pop(col, None)
        pivots += 1
    residual = [entry for row in dense.values() for entry in row.values()]
    return pivots, dense, residual


def inspect(n, edges, reverse=False):
    arcs, faces = multipath_faces(n, edges)
    assert len(faces) == len(set(faces))
    pairs, critical = matching(faces, len(arcs), descending=reverse)
    incidences = acyclicity(faces, pairs)
    graded, boundaries = graded_critical_and_boundaries(critical, pairs)
    ranks = {}
    torsion = {}
    unit_total = 0
    matrix_summaries = {}
    for k, cols in boundaries.items():
        rows = graded.get(k-1, [])
        units, resid_matrix, residual = eliminate_unit_entries(cols, rows)
        unit_total += units
        if residual:
            # In this complete finite census, the sole nonunit block must be a
            # single-row matrix with nonzero entries of gcd 2. Verify the shape.
            active_rows = [row for row, entries in resid_matrix.items() if entries]
            assert n == 5 and set(edges) == {(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4)}, (n, edges, k)
            assert k == 2 and len(active_rows) == 1
            g = 0
            for x in residual:
                g = gcd(g, abs(x))
            assert g == 2, residual
            ranks[k] = units + 1
            torsion[k-1] = [g]
        else:
            ranks[k] = units
        if cols:
            matrix_summaries[k] = {'shape':[len(rows),len(cols)], 'unit_pivots':units, 'residual':residual}
    betti = {k:len(graded[k]) - ranks.get(k, 0) - ranks.get(k+1, 0)
             for k in graded if k >= 0}
    assert all(x >= 0 for x in betti.values()), betti
    return {'faces':len(faces), 'face_vector': dict(Counter(x.bit_count()-1 for x in faces)),
            'pairs':len(pairs), 'critical':{k:len(v) for k,v in graded.items()},
            'Hasse_incidences':incidences, 'ranks':ranks, 'torsion':torsion,
            'betti':betti, 'matrices':matrix_summaries, 'arcs':arcs, 'face_masks':faces}


def raw_witness_chain_checks(arcs, faces):
    # Independent unreduced simplicial chain matrices built directly from sorted faces.
    graded = {k: sorted(x for x in faces if x.bit_count() - 1 == k)
              for k in range(4)}
    boundaries = {}
    for k in (1, 2, 3):
        row_index = {x:j for j,x in enumerate(graded[k-1])}
        columns = []
        for upper in graded[k]:
            bits = [1<<i for i in range(len(arcs)) if upper>>i&1]
            columns.append({row_index[upper^b]: (-1)**index
                            for index, b in enumerate(bits)})
        boundaries[k] = columns
    for k in (2,3):
        for column in boundaries[k]:
            composite = defaultdict(int)
            for middle, weight in column.items():
                for lower, sign in boundaries[k-1][middle].items():
                    composite[lower] += weight * sign
            assert not any(composite.values())

    def rank_mod(columns, p):
        basis = {}
        for original in columns:
            vector = {row:val%p for row,val in original.items() if val%p}
            while vector:
                pivot = min(vector)
                if pivot not in basis:
                    factor = pow(vector[pivot],-1,p)
                    basis[pivot] = {r:(v*factor)%p for r,v in vector.items() if (v*factor)%p}
                    break
                factor = vector[pivot]
                for row, value in basis[pivot].items():
                    current = (vector.get(row, 0) - factor*value) % p
                    if current:
                        vector[row] = current
                    else:
                        vector.pop(row,None)
        return len(basis)
    for prime, expected in [(2,{1:13,2:40,3:12}),(3,{1:13,2:41,3:12})]:
        ranks = {k:rank_mod(columns,prime) for k,columns in boundaries.items()}
        assert ranks == expected, (prime,ranks)
        print('INDEPENDENT_RAW_BOUNDARY_RANKS_MOD',prime,ranks)
    print('RAW_BOUNDARY_SQUARE_ZERO_VERIFIED')


def verify():
    classes = {}
    exceptions = []
    for n in range(1, 6):
        c = 0
        total_orbits = 0
        for code, graph, orbit in graph_classes(n):
            c += 1
            total_orbits += orbit
            result = inspect(n, graph)
            if result['torsion']:
                exceptions.append((n, code, graph, orbit, result))
        classes[n] = c
        assert total_orbits == 1 << (n*(n-1)//2)
    assert classes == {1:1,2:2,3:4,4:11,5:34}, classes
    assert len(exceptions) == 1
    n, code, graph, orbit, witness = exceptions[0]
    assert (n, code, orbit) == (5, 127, 10)
    assert witness['torsion'] == {1:[2]} and witness['betti'] == {1:0,2:7}
    assert witness['faces'] == 141
    # Independent complete subset enumeration, without recursive face generation.
    arcs = witness['arcs']
    by_direct = {mask for mask in range(1<<len(arcs)) if direct_face_test(arcs,mask,n)}
    assert by_direct == set(witness['face_masks'])
    raw_witness_chain_checks(arcs,witness['face_masks'])
    reverse = inspect(n,graph,True)
    assert reverse['torsion']==witness['torsion']
    assert reverse['betti']==witness['betti']
    assert reverse['face_vector']==witness['face_vector']
    print('ISOMORPHISM_CLASS_COUNTS',classes)
    print('TOTAL_LABELED_GRAPHS',sum(1<<(n*(n-1)//2) for n in range(1,6)))
    print('UNIQUE_TORSION_GRAPH','K_{1,1,3}','n',n,'edge_mask',code,'labeled_orbit_size',orbit)
    print('WITNESS_EDGE_LIST',graph)
    print('WITNESS_F_VECTOR',dict(sorted(witness['face_vector'].items())))
    for label,x in [('ASCENDING',witness),('DESCENDING',reverse)]:
        print(label,'faces',x['faces'],'matched_pairs',x['pairs'],'critical_cells',x['critical'],
              'Hasse_incidences',x['Hasse_incidences'],'boundary_data',x['matrices'])
    print('REDUCED_INTEGRAL_HOMOLOGY','H_1=Z/2; H_2=Z^7; all others zero')
    print('SHARP_MINIMAL_BIDIRECTED_MULTIPATH_TORSION_VERIFIED')

if __name__ == '__main__':
    verify()
