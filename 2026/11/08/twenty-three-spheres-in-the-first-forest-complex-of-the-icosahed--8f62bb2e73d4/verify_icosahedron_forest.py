#!/usr/bin/env python3
"""Exhaustive reproducibility certificate for an icosahedral forest complex.

Runs with Python 3 standard library only. The graph is supplied as an explicit edge list.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
import json

N = 12
EDGES = (
    (0,1),(0,5),(0,7),(0,8),(0,11),
    (1,2),(1,5),(1,6),(1,8),
    (2,3),(2,6),(2,8),(2,9),
    (3,4),(3,6),(3,9),(3,10),
    (4,5),(4,6),(4,10),(4,11),
    (5,6),(5,11),
    (7,8),(7,9),(7,10),(7,11),
    (8,9),(9,10),(10,11)
)


def edge_neighbors():
    neighbor = [0] * N
    for a,b in EDGES:
        assert 0 <= a < b < N
        neighbor[a] |= 1 << b
        neighbor[b] |= 1 << a
    assert len(set(EDGES)) == 30
    assert all(row.bit_count() == 5 for row in neighbor)
    # All edges belong to two triangles, as for the regular icosahedron.
    assert all((neighbor[a] & neighbor[b]).bit_count() == 2 for a,b in EDGES)
    return neighbor


def valid_by_degree(mask, neighbor):
    return all((mask & neighbor[v]).bit_count() <= 1
               for v in range(N) if mask & (1 << v))


def valid_by_edges(mask):
    used = 0
    for a,b in EDGES:
        if mask & (1 << a) and mask & (1 << b):
            if used & ((1 << a) | (1 << b)):
                return False
            used |= (1 << a) | (1 << b)
    return True


def boundary(face):
    # Canonical increasing vertex order, with all signs in integers.
    return [(face ^ (1 << v), -1 if (face & ((1 << v) - 1)).bit_count()%2 else 1)
            for v in range(N) if face & (1 << v)]


def matching(faces, order):
    rest = set(faces) - {0}
    pairs = []
    for v in order:
        for low in sorted(tuple(rest)):
            upper = low | (1 << v)
            if not (low & (1 << v)) and upper in rest:
                pairs.append((low, upper))
                rest.remove(low)
                rest.remove(upper)
    return pairs, rest


def topological_test(faces, pairs):
    paired = dict(pairs)
    indegree = defaultdict(int)
    outgoing = defaultdict(list)
    incidences = 0
    for low in faces:
        for v in range(N):
            if low & (1 << v):
                continue
            upper = low | (1 << v)
            if upper not in faces:
                continue
            incidences += 1
            a,b = ((low,upper) if paired.get(low) == upper else (upper,low))
            outgoing[a].append(b)
            indegree[b] += 1
    q = deque(s for s in faces if indegree[s] == 0)
    visited = 0
    while q:
        a = q.popleft()
        visited += 1
        for b in outgoing[a]:
            indegree[b] -= 1
            if indegree[b] == 0:
                q.append(b)
    assert visited == len(faces), f'Directed cycle detected: visited {visited}/{len(faces)}'
    return incidences


def critical_boundary(critical, pairs):
    # Discrete Morse chain projection. For a matched lower cell l<->t,
    # 0 = projection(d t) determines projection(l) recursively.
    paired_lower = dict(pairs)
    paired_upper = set(paired_lower.values())
    critical_two = sorted(s for s in critical if s.bit_count() == 3)
    critical_three = sorted(s for s in critical if s.bit_count() == 4)

    @lru_cache(None)
    def project(face):
        if face in critical:
            return {face: 1}
        if face in paired_upper:
            return {}
        upper = paired_lower[face]
        b = boundary(upper)
        eps = next(e for lo,e in b if lo == face)
        result = defaultdict(int)
        for lo,sgn in b:
            if lo == face:
                continue
            for other, coeff in project(lo).items():
                result[other] -= eps*sgn*coeff
        return {s:k for s,k in result.items() if k}

    matrix = [[sum(sign*project(low).get(row, 0) for low,sign in boundary(col))
               for col in critical_three] for row in critical_two]
    assert len(matrix) == 2 and all(len(r) == 22 for r in matrix)
    # A two-by-two determinant of +-1 proves integral surjectivity.
    minors = [(i,j,matrix[0][i]*matrix[1][j]-matrix[0][j]*matrix[1][i])
              for i in range(22) for j in range(i+1,22)]
    witness = next(((i,j,v) for i,j,v in minors if abs(v) == 1), None)
    assert witness is not None
    return critical_two, critical_three, matrix, witness


def modp_rank(columns, p):
    # Independently reduce the unreduced signed simplicial boundary over F_p.
    pivots = {}
    for column in columns:
        work = {r:(a % p) for r,a in column.items() if a%p}
        while work:
            pivot = min(work)
            if pivot not in pivots:
                factor = pow(work[pivot], -1, p)
                pivots[pivot] = {r:(a*factor)%p for r,a in work.items()}
                break
            factor = work[pivot]
            for r,a in pivots[pivot].items():
                z = (work.get(r,0)-factor*a)%p
                if z:work[r] = z
                else:work.pop(r,None)
    return len(pivots)


def full_modp_boundary_ranks(faces, p):
    ranks = []
    for size in range(2, 5):
        rows = sorted(s for s in faces if s.bit_count() == size-1)
        cols = sorted(s for s in faces if s.bit_count() == size)
        index = {s:i for i,s in enumerate(rows)}
        columns = [{index[lo]:coeff for lo,coeff in boundary(t)} for t in cols]
        ranks.append(modp_rank(columns,p))
    return ranks


def main():
    nb = edge_neighbors()
    faces = {s for s in range(1 << N) if valid_by_degree(s, nb)}
    assert faces == {s for s in range(1 << N) if valid_by_edges(s)}
    assert len(faces) == 324
    fvector = [sum(s.bit_count() == size for s in faces) for size in range(1, 5)]
    assert fvector == [12, 66, 140, 105]
    facets = {s for s in faces if not any((s | (1 << v)) in faces
                                             for v in range(N) if not (s & (1 << v)))}
    assert len(facets) == 105 and all(s.bit_count() == 4 for s in facets)
    out = {'vertices':N, 'graph_edges':len(EDGES), 'faces_including_empty':len(faces),
           'face_vector_nonempty':fvector, 'facets':len(facets),
           'reduced_euler_characteristic': sum((-1)**i*fvector[i] for i in range(4))-1,
           'matchings': []}
    for order in (list(range(N)), list(range(N-1, -1, -1))):
        pairs, crit = matching(faces, order)
        assert len(pairs) == 149 and len(crit) == 25
        dimensions = dict(sorted(Counter(s.bit_count()-1 for s in crit).items()))
        assert dimensions == {0:1,2:2,3:22}
        assert topological_test(faces-{0},pairs) == 972
        rows, cols, matrix, witness = critical_boundary(crit, pairs)
        # Check chain formula: 2x22 matrix and unit determinant ⇒ H2=0,H3=Z^20.
        out['matchings'].append({'order': 'ascending' if order[0] == 0 else 'descending',
                                 'matched_pairs':len(pairs), 'critical_dimensions':dimensions,
                                 'hasse_incidences':972,
                                 'critical_2_cell_masks':rows,'critical_3_cell_masks':cols,
                                 'morse_boundary_3_to_2':matrix,
                                 'unit_minor_column_indices':list(witness[:2]),
                                 'unit_minor_determinant':witness[2]})
    out['unreduced_boundary_ranks_mod2']=full_modp_boundary_ranks(faces,2)
    out['unreduced_boundary_ranks_mod3']=full_modp_boundary_ranks(faces,3)
    assert out['unreduced_boundary_ranks_mod2'] == [11,55,85]
    assert out['unreduced_boundary_ranks_mod3'] == [11,55,85]
    assert out['reduced_euler_characteristic'] == -20
    out['integral_homotopy_type']='wedge of 20 three-spheres'
    print(json.dumps(out, sort_keys=True, separators=(',',':')))
    print('ICOSAHEDRAL_FIRST_FOREST_WEDGE_20_S3_VERIFIED')

if __name__ == '__main__':
    main()
